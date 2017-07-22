# movie-network

Movie Network is a personal movie library website. Currently, it's possible to give a list of movie names. The code will automatically extract the movie poster and trailer urls and generates an HTML page containing those movies.

Run
---
To be able to run the code you need API keys for The Movie DB and Youtube Data APIs. You should create a file named keys in the project's root directory and paste those keys inside that file given the example template provided in this repo inside the keys_template file.

Afterwards, you can easily run the main.py from the project's root directory and the HTML webpage fresh_tomatos.html will be automatically opened with the movies' posters and trailers.

In order to change the list of movies you can modify the MOVIES_NAMES list inside the main.py


License
-------
Movie Network uses the MIT License.

About MovieDB
-------------
<img src="resources/moviedb.png" alt="moviedb" style="width: 120px;"/> 

The projects uses the MovieDB API to extract and download movie's metadata.