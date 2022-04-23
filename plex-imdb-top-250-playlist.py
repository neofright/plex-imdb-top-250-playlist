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
    # creating instance of IMDb
    ia = Cinemagoer()
    
    # getting top 250 movies
    search = ia.get_top250_movies()

    imdbtop250ids = []
    for imdb250movie in search:
        imdbtop250ids.append(imdb250movie.movieID)
    #######################################
    to_playlist = []
    movies = plex.library.section(os.environ.get('plex_library'))
    for movie in movies.searchMovies():
        for guid in movie.guids:
            if 'imdb' in guid.id:
                clean_id = guid.id.replace('imdb://tt','')
                if clean_id in imdbtop250ids:
                    #print(movie.title + ' is in the IMDb Top 250 Movies list.')
                    to_playlist.append(movie)

    movies.createPlaylist("IMDb Top 250 Movies", to_playlist)