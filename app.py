import pickle
import streamlit as st
import requests
from requests.exceptions import RequestException
from retry import retry

def fetch_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US".format(movie_id)
    response = requests.get(url)
    response.raise_for_status()  # Raise an HTTPError on bad responses
    data = response.json()
    poster_path = data.get('poster_path')
    if poster_path:
        full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
        return full_path
    else:
        return None

def recommend(movie):
    try:
        index = movies[movies['title'] == movie].index[0]
        distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
        recommended_movie_names = []
        recommended_movie_posters = []
        for i in distances[1:6]:
            movie_id = movies.iloc[i[0]].movie_id
            poster = fetch_poster(movie_id)
            if poster:
                recommended_movie_posters.append(poster)
                recommended_movie_names.append(movies.iloc[i[0]].title)
        return recommended_movie_names, recommended_movie_posters
    except Exception as e:
        # Instead of showing an error, retry fetching recommendations up to 3 times
        for _ in range(3):
            try:
                recommended_movie_names, recommended_movie_posters = recommend(movie)
                return recommended_movie_names, recommended_movie_posters
            except Exception as e:
                pass
        # If retries fail, return empty recommendations
        return [], []

st.header('Movie Recommendation System')
movies = pickle.load(open('movie_list.pkl', 'rb'))
similarity = pickle.load(open('similarity.pkl', 'rb'))

movie_list = movies['title'].values
selected_movie = st.selectbox(
    "Type or select a movie from the dropdown",
    movie_list
)

if st.button('Show Recommendation'):
    recommended_movie_names, recommended_movie_posters = recommend(selected_movie)
    if recommended_movie_names:
        cols = st.columns(5)
        for idx, col in enumerate(cols):
            if idx < len(recommended_movie_names):
                col.text(recommended_movie_names[idx])
                col.image(recommended_movie_posters[idx])
    else:
        st.write("No recommendations available.")
