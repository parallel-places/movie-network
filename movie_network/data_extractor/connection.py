"""
Module contains the class Connection that provides methods for extracting movie
metadata MovieDB.
"""
import os
import requests
from apiclient.discovery import build
from movie_network.data.media import Movie


class Connection():
    """
    Connection class has methods for extracting movie data from MovieDB API.
    """

    YOUTUBE_API_SERVICE_NAME = "youtube"
    YOUTUBE_API_VERSION = "v3"

    def __init__(self, keys=None):
        self.movie_db_base_url = 'https://api.themoviedb.org/3'
        if keys is None:
            self.keys = Connection.read_keys()
        else:
            self.keys = keys

    @staticmethod
    def read_keys(path='keys'):
        """
        Reads the API key from the default file that contains the key.
        """
        path = os.path.abspath(path)
        file_handle = open(path, 'r')
        file_content = file_handle.readlines()
        keys = dict()
        for content in file_content:
            index = content.index(':')
            keys[content[0:index]] = content[(index+1):].split()[0]
        return keys

    def get_youtube_vid_id(self, query, max_results=10):
        """
        Makes a request to youtube API with a search query and returns the
        corresponding video's id.
        :param query: search query of type string to be used for
                      searching youtube.
        :param max_results: The maximum results returned by searching youtube
        :returns: The movie id of the first video came up in the youtube search
        """
        youtube = build(Connection.YOUTUBE_API_SERVICE_NAME,
                        Connection.YOUTUBE_API_VERSION,
                        developerKey=self.keys['google'])

        search_response = youtube.search().list(
            q=query,
            part="id,snippet",
            maxResults=max_results
        ).execute()

        for search_result in search_response.get("items", []):
            if search_result["id"]["kind"] == "youtube#video":
                return search_result["id"]["videoId"]
        else:
            return None

    def get_trailer_url(self, title):
        """
        Extracts the video id of the corresponding video found in youtube by
        searching the title.
        :param title: Title of the movie that we want get its trailer
                      from youtube
        :returns: URL of the video on Youtube
        """
        query = title + " trailer"
        movie_id = self.get_youtube_vid_id(query)
        return "https://www.youtube.com/watch?v=" + movie_id

    @staticmethod
    def create_poster_path(poster_path):
        """
        Gets the poster_path from movieDB adds url prefix and returns the url
        """
        return "https://image.tmdb.org/t/p/w500" + poster_path

    def get_movie_instance(self, title, poster_path):
        """
        Receives the movie title and its poster_path extracted from MovieDB and
        creates urls to the movie's trailer and poster. Then it creates an
        object of Movie class and returns it.
        :param title: title of the movie returned by moviedb
        :param poster_path: poster path of the movie on moviedb
        :returns: returns a movie instance
        """
        trailer_url = self.get_trailer_url(title)
        poster_url = Connection.create_poster_path(poster_path)
        movie = Movie(title=title,
                      poster=poster_url,
                      trailer_url=trailer_url)
        return movie

    def get_first_movie(self, data):
        """
        Receives request's results from movieDB and creates and returns a
        Movie instance.
        :param data: data in JSON format extracted from moviedb
        :returns: a Movie instance
        """
        results = data['results']
        if results:
            first_result = results[0]
            title = first_result['title']
            poster_path = first_result['poster_path']
            return self.get_movie_instance(title, poster_path)
        return None

    def movie_search(self, text):
        """
        Receives the name of a movie and creates a Movie object by extracting
        metadata from Youtube and MovieDB.
        :param text: Name of a movie.
        :returns: A Movie instance.
        """
        movie_search_path = "search/movie"
        url = os.path.join(self.movie_db_base_url, movie_search_path)
        parameters = {
            'api_key': self.keys['movie_db'],
            'query': text
            }
        request = requests.get(url, parameters)
        if request.status_code == 200:
            return self.get_first_movie(request.json())
        else:
            print("The request to MovieDB was unsuccessful.")
            exit(1)
