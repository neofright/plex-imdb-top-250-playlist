# plex-imdb-top-250-playlist

Python script to create a Plex playlist of movies in your library that are in the IMDB Top 250 Movies list.

Plex playlists don't allow filtering by watched status so a collection might be nicer...

## TODO:

- Prevent iterating over entire plex library for each imdb movie (this is done to preserver ordering).
- Rewrite to use a plex collection instead of a playlist.


## Usage:

Create a .env file with the following contents (substituting real values):



    plex_server = ''

    plex_username = ''

    plex_password = ''

    plex_library = 'Movies'



Note that `plex_server` is the server _name_ and not the URL.



## Requirements:

cinemagoer



plexapi



python-dotenv



