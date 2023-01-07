import streamlit as st
import pandas as pd
import pickle
import numpy as np
import difflib

st.title('Movie Recommendation System')


movie_df = pickle.load(open('movies_data.pkl', 'rb'))
similarity = pickle.load(open('similarity.pkl', 'rb'))
list_of_movie = np.array(movie_df['title'])

option = st.text_input('Enter Movie Name', placeholder='Movie Name')
find_match_title = difflib.get_close_matches(option, list_of_movie)


def recommend():
    close_match = find_match_title[0]
    index_of_title = movie_df[movie_df['title'] == close_match]['index'].values[0]

    similarity_score = list(enumerate(similarity[index_of_title]))

    sorted_similar_movie = sorted(similarity_score, key=lambda x: x[1], reverse=True)

    l = []
    for i in sorted_similar_movie[1:6]:
        l.append('{}'.format(movie_df.iloc[i[0]].title))
    return l


def show_url():
    close_match = find_match_title[0]
    index = movie_df[movie_df['title'] == close_match].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x:x[1])
    x = []
    for i in distances[1:6]:
        x.append(movie_df.iloc[i[0]].homepage)
    return x


if st.button('Recommend me'):
    if len(find_match_title) >= 1:
        st.write('Movies Recommended for you are:')
        df = pd.DataFrame({
            'Movie Recommendation': recommend(),
            'Movie link': show_url()
        })
        st.table(df)
    else:
        st.warning('''
        ### Sorry movie not found, in our database,
        Enter the correct movie name
         
        ''')

st.write('P.S: Thanks to MovieLens, the datasets is from MovieLens, it contains movies from January 09, 1995 to November 21, 2019')
