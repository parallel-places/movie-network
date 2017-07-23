"""
This module has a list of movie names, uses the Connection class to extract
their information as Movie class instances and pass them to fresh_tomatos module
to generate an HTML page.
"""
from movie_network.data_extractor.connection import Connection
from fresh_tomatoes import open_movies_page

# MOVIE_NAMES is a list that contains movie names in string format
# Chage the list to have a webpage with your desried movies
MOVIE_NAMES = ['Matrix',
               'Inception',
               'Toy Story',
               'The Founder',
               'Social Network',
               'Gone Girl']

connection = Connection()
movies = list()
for movie_name in MOVIE_NAMES:
    movies.append(connection.movie_search(movie_name))
# open_movies_page function generates the fresh_tomatos.html page of movies
open_movies_page(movies)
