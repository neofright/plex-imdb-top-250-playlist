#!/usr/bin/env python3
from dotenv import load_dotenv
import os
import plexapi
from plexapi.myplex import MyPlexAccount
from imdb import Cinemagoer
   
## https://codereview.stackexchange.com/a/257530
def input_yes_no(prompt: str) -> bool:
    full_prompt = f'{prompt} ([Y]/N): '
    while True:
        answer = input(full_prompt).strip()
        if answer == '':
            return True

        answer = answer[0].lower()
        if answer == 'y':
            return True
        if answer == 'n':
            return False
        print('ERROR')

if __name__ == "__main__":
    load_dotenv()
    #######################################
    mfa_enabled = input_yes_no('Does your Plex account use 2FA?')
    if mfa_enabled:
        mfa_token = input('Enter Plex TOTP token: ')
    else:
        mfa_token = ""
    #######################################
    account = MyPlexAccount(os.environ.get('plex_username'), os.environ.get('plex_password') + mfa_token)
    plex = account.resource(os.environ.get('plex_server')).connect()  # returns a PlexServer instance
    #######################################
    ia = Cinemagoer()
    imdb_top_250_movies = ia.get_top250_movies()
    #######################################
    plex_movies = plex.library.section(os.environ.get('plex_library'))

    playlist_title = "IMDb Top 250 Movies"
    #movies.createPlaylist(playlist_title, None)
    my_playlist = plex.playlist(playlist_title)

    print('Missing: ')
    plex_movie_search = plex_movies.searchMovies()
    for imdb_top_250_movie in imdb_top_250_movies:
        movie_found = False
        for plex_movie in plex_movie_search:
            for guid in plex_movie.guids:
                if 'imdb' in guid.id:
                    clean_id = guid.id.replace('imdb://tt','')
                    if clean_id == imdb_top_250_movie.movieID:
                        my_playlist.addItems(plex_movie)
                        movie_found = True
                
        if movie_found == False:
            print(imdb_top_250_movie)
