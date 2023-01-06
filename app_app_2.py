import streamlit as st
import pandas as pd
import pickle
import numpy as np

st.title('Movie Recommendation System') 

# movies_data = r"C:\Users\CELESTINE TYJC\Desktop\Michael python file\Recommend System\recom_sys_siddhardhan\movies_data.pkl"
# similarity_file = "https://github.com/michaelonyedika/pt2-Ai-movie-recommendation-system/blob/main/similarity.pkl"


movie_df = pickle.load(open('movies_data.pkl', 'rb'))
similarity = pickle.load(open('similarity.pkl', 'rb'))
list_of_movie = np.array(movie_df['title'])

option = st.selectbox(
    'Select Movie',
    list_of_movie
)


def recommend_system(movie):
    index = movie_df[movie_df['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])

    l = []
    for i in distances[1:6]:
        l.append('{}'.format(movie_df.iloc[i[0]].title))

    return l


def show_url(movie):
    index = movie_df[movie_df['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x:x[1])
    x = []
    for i in distances[1:6]:
        x.append(movie_df.iloc[i[0]].homepage)
    return x


if st.button('Recommend me'):
    st.write('Movies Recommended for you are:')
    df = pd.DataFrame({
        'Movie Recommendation': recommend_system(option),
        'Movie link': show_url(option)
    })
    st.table(df)
