# plex-imdb-top-250-playlist

Python script to create a Plex playlist of movies in your library that are in the IMDB Top 250 Movies list.

Plex playlists don't allow filtering by watched status so a collection might be nicer...

## TODO:

- Print missing movies from your library so you can choose to add them.
- Order playlist entries by rating and not name. Shawshank Redemption should be listed before 12 Angry men...


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



