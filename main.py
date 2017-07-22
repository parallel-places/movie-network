from movie_network.data_extractor.connection import Connection
from fresh_tomatoes import open_movies_page


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
open_movies_page(movies)
