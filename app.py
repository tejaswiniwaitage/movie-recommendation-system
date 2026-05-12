import streamlit as st
import pandas as pd
import pickle

# Load processed data (IMPORTANT)
movies = pickle.load(open("movies.pkl", "rb"))
similarity = pickle.load(open("similarity.pkl", "rb"))

st.title("🎬 Movie Recommendation System")

# Movie list
movie_list = movies['title'].values
selected_movie = st.selectbox("Choose a movie", movie_list)


# Recommendation function
def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = similarity[index]

    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []
    for i in movies_list:
        recommended_movies.append(movies.iloc[i[0]].title)

    return recommended_movies


# Button
if st.button("Recommend Movies"):
    recommendations = recommend(selected_movie)

    st.subheader("Recommended Movies:")
    for movie in recommendations:
        st.write("🎬", movie)