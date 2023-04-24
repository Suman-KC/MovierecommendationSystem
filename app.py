import pandas as pd
import pickle
import streamlit as st
import difflib as df
import requests

def fetch_poster(movie_id):
    response=requests.get("https://api.themoviedb.org/3/movie/{}?api_key=ec0f32aac64a405993a6c9476a8038d5".format(movie_id))
    data=response.json()
    #st.text(data)
    #st.text("https://api.themoviedb.org/3/movie/{}?api_key=ec0f32aac64a405993a6c9476a8038d5".format(movie_id))
    return "https://image.tmdb.org/t/p/w500/"+data['poster_path']

def recommend(movie_name):
    # Creating a list with all the movie names given in the dataset
    #movie_index=movies[movies['title']==movie].index[0]
    #distances=similarity[movie_index]
    list_of_all_titles = movies['title'].tolist()
    # print(list_of_all_titles)
    # finding the close match for the movie name give by the user
    find_close_match = df.get_close_matches(movie_name, list_of_all_titles)
    # print(find_close_match)
    # finding the index of the movie with title
    close_match = find_close_match[0]
    index_of_the_movie = movies[movies.title == close_match]['index'].values[0]
    # print(index_of_the_movie)
    # getting a list of similar movies
    similarity_score = list(enumerate(similarity[index_of_the_movie]))
    # print(similarity_score)
    #len(similarity_score)
    # sorting the movies based on their similarity score
    sorted_similar_movie = sorted(similarity_score, key=lambda x: x[1], reverse=True)[1:11]
    # print the similar movies based on the index
    recommended_movies_poster=[]
    st.subheader('Moives suggested for you:\n')
    recommended_movies=[]
    for movie in sorted_similar_movie:
        index = movie[0]
        movie_id=movies.iloc[movie[0]].id
        recommended_movies.append(movies[movies.index==index]['title'].values[0])
        #fetch posters from api
        recommended_movies_poster.append(fetch_poster(movie_id))
    return recommended_movies,recommended_movies_poster

        #index = movie[0]
        #title_from_index = movies[movies.index == index]['title'].values[0]
       # if(i<10):
        #    print(i, '.', title_from_index)
           # i += 1


movies_list=pickle.load(open('movies_dict.pkl','rb'))
movies=pd.DataFrame(movies_list)
similarity=pickle.load(open('similarity.pkl','rb'))
st.header('Welcome')
st.title("Movie Recommender System")
selected_movie_name=st.selectbox('You can watch awesome movies here',movies['title'].values)
if st.button('Recommend'):
   #destructuring
   names,posters= recommend(selected_movie_name)
   col1,col2,col3,col4,col5=st.columns(5)
   col6,col7,col8,col9,col10= st.columns(5)
   with col1:
       st.text(names[0])
       st.image(posters[0])
   with col2:
       st.text(names[1])
       st.image(posters[1])
   with col3:
       st.text(names[2])
       st.image(posters[2])
   with col4:
       st.text(names[3])
       st.image(posters[3])
   with col5:
       st.text(names[4])
       st.image(posters[4])
   with col6:
       st.text(names[5])
       st.image(posters[5])
   with col7:
       st.text(names[6])
       st.image(posters[6])
   with col8:
       st.text(names[7])
       st.image(posters[7])
   with col9:
       st.text(names[8])
       st.image(posters[8])
   with col10:
       st.text(names[9])
       st.image(posters[9])

st.subheader("This online movie recommendation system is developed by Suman K.C,Kamal Mahara and Yogesh Subedi.")









