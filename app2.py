from flask import Flask, render_template, request
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd
import pickle
import streamlit as st
import requests

def fetch_poster(id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=7b1b1790f6bb91e3707a67fdcb875a9f&language=en-US".format(id)
    data = requests.get(url)
    data = data.json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path

def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_movie_names = []
    recommended_movie_posters = []
    for i in distances[1:6]:
        # fetch the movie poster
        id = movies.iloc[i[0]].id
        recommended_movie_posters.append(fetch_poster(id))
        recommended_movie_names.append(movies.iloc[i[0]].title)

    return recommended_movie_names,recommended_movie_posters

st.markdown("<h1 style='text-align: center; color: black;'>Movie Recommender System</h1>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align: center; color: black;'>Find a similar movie from a dataset of 5,000 movies!</h4>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align: center; color: black;'>Web App created by Sagar Bapodara</h4>", unsafe_allow_html=True)

movies = pd.read_csv('data/train_data.csv')
tfv = TfidfVectorizer()
vectors = tfv.fit_transform(movies['tags'])
similarity = cosine_similarity(vectors)

# movies = pickle.load(open('data/movies.pkl','rb'))
# similarity = pickle.load(open('data/similarity.pkl','rb'))

movie_list = movies['title'].values
selected_movie = st.selectbox(
    "Type or select a movie you like :",
    movie_list
)

if st.button('Show Recommendation'):
    st.write("Recommended Movies based on your interests are :")
    recommended_movie_names,recommended_movie_posters = recommend(selected_movie)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(recommended_movie_names[0])
        st.image(recommended_movie_posters[0])
    with col2:
        st.text(recommended_movie_names[1])
        st.image(recommended_movie_posters[1])

    with col3:
        st.text(recommended_movie_names[2])
        st.image(recommended_movie_posters[2])
    with col4:
        st.text(recommended_movie_names[3])
        st.image(recommended_movie_posters[3])
    with col5:
        st.text(recommended_movie_names[4])
        st.image(recommended_movie_posters[4])

st.title(" ")

