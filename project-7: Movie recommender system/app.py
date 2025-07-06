import streamlit as st
import pickle
import pandas as pd
import requests

movie_list = pickle.load(open('movies.pkl', 'rb'))
movie = movie_list['title_x'].values

cosine_similarity = pickle.load(open('similarity.pkl', 'rb'))

def fetch_poster(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}"
    
    headers = {
        "accept": "application/json",
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI1NWY5ODNlOTU3M2QyOWE0MTEzYmFhZWY3YTBhMjlhNyIsIm5iZiI6MTc1MTgyMjM0MS41NTMsInN1YiI6IjY4NmFiMDA1MTRhM2VhOTE3MGE5NTQ3MCIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.pfOMhQwdfhbTJcrHnHTVtY7FmXEivND5UZJdVqro9jU"
    }
    
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        poster_path = data.get('poster_path')
        if poster_path:
            return f"https://image.tmdb.org/t/p/w500{poster_path}"
    return None 


def recommend(movie):
    movie_index = movie_list [movie_list ['title_x'] == movie].index[0]
    distance = cosine_similarity[movie_index]
    movies_list_sorted = sorted(list(enumerate(distance)), reverse = True, key = lambda x:x[1])[1:6]

    recommended_movies = []
    recommended_ids = []
    for i in movies_list_sorted:
        recommended_movies.append(movie_list.iloc[i[0]]['title_x'])
        recommended_ids.append(movie_list.iloc[i[0]]['id']) 

    return recommended_movies, recommended_ids 

st.title("Movie :red[Recommmendation] app", anchor="movie-recommendation-app")
st.subheader("Find your next favorite movie! 👇")
st.write("Simply select a movie from the list below, and we'll recommend similar films for you to enjoy.")


st.markdown(
    """
    <div style="text-align: center;">
        <img src="https://media4.giphy.com/media/v1.Y2lkPTc5MGI3NjExdGZxejZqZjhpcHkxbGR2dHRzZDhtNmdlbWw1bXI4NG1zOWw2MGMzayZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/l1J9GIXk9w7OYsd5S/giphy.gif"
             style="width: 800px; object-fit: cover;">
    </div>
    """,
    unsafe_allow_html=True
)

movie_selected = st.selectbox(
    "Select a movie",
    movie,
    index=None,
    placeholder="Movie...",
)

st.write("You selected:", movie_selected )

if st.button("Recommend") and movie_selected:
    recommended_movies, recommended_ids = recommend(movie_selected)

    # Create 5 columns for 5 movie posters
    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        st.image(fetch_poster(recommended_ids[0]))
        st.text(recommended_movies[0])

    with col2:
        st.image(fetch_poster(recommended_ids[1]))
        st.text(recommended_movies[1])

    with col3:
        st.image(fetch_poster(recommended_ids[2]))
        st.text(recommended_movies[2])

    with col4:
        st.image(fetch_poster(recommended_ids[3]))
        st.text(recommended_movies[3])

    with col5:
        st.image(fetch_poster(recommended_ids[4]))
        st.text(recommended_movies[4])



