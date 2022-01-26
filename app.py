from flask import Flask
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import streamlit as st
import pickle
import pandas as pd
import requests
import webbrowser


st.set_page_config(layout="wide")
# st.title('Movie Recommender Sysytem')
st.markdown("<h1 style='text-align: center; color: white;'>Movie Recommender System</h1>", unsafe_allow_html=True)


import base64
def get_base64(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

def set_background(png_file):
    bin_str = get_base64(png_file)
    page_bg_img = '''
    <style>
.stApp {
  background-image: url("data:image/png;base64,%s");
 background-repeat: no-repeat;
 background-size: 100%;
}
</style>
    ''' % bin_str
    st.markdown(page_bg_img, unsafe_allow_html=True)

set_background('images/background.jpg')



movies = pd.read_csv('data/train_data.csv')
tfv = TfidfVectorizer()
vectors = tfv.fit_transform(movies['tags'])
similarity = cosine_similarity(vectors)

def fetch_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=7b1b1790f6bb91e3707a67fdcb875a9f&language=en-US".format(movie_id)
    data = requests.get(url)
    data = data.json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path

def recommend(movie):
    recommended_movie_names = []
    recommended_movie_posters=[]
    recommended_movie_overview = []
    recommended_movie_runtime = []
    recommended_movie_status = []
    recommended_movie_rating= []
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])),reverse=True,key = lambda x: x[1])
    for i in distances[1:6]:
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movie_posters.append(fetch_poster(movie_id))
        recommended_movie_names.append(movies.iloc[i[0]].title)
        recommended_movie_overview.append(movies.iloc[i[0]].overview_2)
        recommended_movie_runtime.append(movies.iloc[i[0]].runtime)
        recommended_movie_status.append(movies.iloc[i[0]].status)
        recommended_movie_rating.append(movies.iloc[i[0]].vote_average)
    return recommended_movie_names,recommended_movie_posters,recommended_movie_overview,recommended_movie_runtime,recommended_movie_status,recommended_movie_rating

col6,col7,col8 = st.columns(3)
with col7:
    input = st.selectbox(label='Enter a movie title',options = movies['title'])
    butt = st.button('Show Recommendations')
st.text("")
st.text("")
st.text("")
st.text("")
st.text("")
if butt:
    recommended_movie_names,recommended_movie_posters,recommended_movie_overview,recommended_movie_runtime,recommended_movie_status,recommended_movie_rating= recommend(input)
    
    
    col1, col2,col3,col4,col5 = st.columns(5)    
    
    
    
    with col1:
        st.subheader(recommended_movie_names[0])
        st.text("")
        st.image(recommended_movie_posters[0])
        st.write('**Overview:**')
        st.markdown(recommended_movie_overview[0])
        st.text(recommended_movie_runtime[0])
        st.text(recommended_movie_status[0])
        st.write('**Rating:**')
        st.text(recommended_movie_rating[0])

    with col2:
        st.subheader(recommended_movie_names[1])
        st.text("")
        st.image(recommended_movie_posters[1])
        st.write('**Overview:**')
        st.markdown(recommended_movie_overview[1])
        st.text(recommended_movie_runtime[1])
        st.text(recommended_movie_status[1])
        st.write('**Rating:**')
        st.text(recommended_movie_rating[1])
         
    with col3:
        st.subheader(recommended_movie_names[2])
        st.text("")
        st.image(recommended_movie_posters[2])
        st.write('**Overview:**')
        st.markdown(recommended_movie_overview[2])
        st.text(recommended_movie_runtime[2])
        st.text(recommended_movie_status[2])
        st.write('**Rating:**')
        st.text(recommended_movie_rating[2])

    with col4:
        st.subheader(recommended_movie_names[3])
        st.text("")
        st.image(recommended_movie_posters[3])
        st.write('**Overview:**')
        st.markdown(recommended_movie_overview[3])
        st.text(recommended_movie_runtime[3])
        st.text(recommended_movie_status[3])
        st.write('**Rating:**')
        st.text(recommended_movie_rating[3])

    with col5:
        st.subheader(recommended_movie_names[4])
        st.text("")
        st.image(recommended_movie_posters[4])
        st.write('**Overview:**')
        st.markdown(recommended_movie_overview[4])
        st.text(recommended_movie_runtime[4])
        st.text(recommended_movie_status[4])
        st.write('**Rating:**')
        st.text(recommended_movie_rating[4])



footer="""<style>
a:link , a:visited{
color: red;
background-color: transparent;
}
a:hover,  a:active {
color: white;
background-color: transparent;
text-decoration: underline;
}
.footer {
position: fixed;
left: 0;
bottom: 0;
width: 100%;
background-color: black;
color: white;
text-align: center;
}
</style>
<div class="footer">
<p>Developed by <a style='display: block; text-align: center;' href="https://www.linkedin.com/in/makhaildynchan/" target="_blank">Khaildyn Chan</a></p>
</div>
"""
st.markdown(footer,unsafe_allow_html=True)
