"""
This module contains the Movie class.
"""
class Movie():
    """
    Movie class provides properties to store the movies metadata and
    corresponding methods.
    """
    def __init__(self, title, poster, trailer_url):
        self.title = title
        self.poster = poster
        self.trailer_url = trailer_url
