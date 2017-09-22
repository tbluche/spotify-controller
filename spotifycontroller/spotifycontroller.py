# -*-: coding utf-8 -*-
""" Skeleton Snips skill. """
import os
import sys
import spotipy
from spotipy.oauth2 import SpotifyOAuth

class SpotifyController:
    """ Skeleton Snips skill. """

    def __init__(self, client_id, secret_id, redirect_uri, tts_service=None):
        """
        """
        self.client_id = client_id
        self.secret_id = secret_id
        self.redirect_url = redirect_uri
        self.tts = tts_service
        # self.hostname = hostname
        # self.light_ids = light_ids

    def __get_access_token(self):
        scope = 'user-modify-playback-state user-read-playback-state'
        auth = SpotifyOAuth(
            self.client_id, self.secret_id, self.redirect_url,
            scope=scope, cache_path='/home/pi/.cache--snipscontroller'
        )
        token = auth.get_cached_token()
        if token is None:
            auth_url = auth.get_authorize_url()
            try:
                import webbrowser
                webbrowser.open(auth_url)
                print("Opened %s in your browser" % auth_url)
            except:
                self.tts.speak("Please navigate here: %s" % auth_url)
                print("Please navigate here: %s" % auth_url)
                print

            response = raw_input("Enter the URL you were redirected to: ")
            code = auth.parse_response_code(response)
            token = auth.get_access_token(code)
        else:
            if auth.is_token_expired(token):
                token = auth.refresh_access_token(token['refresh_token'])

        return token['access_token']


    def stop_playing(self):
        """ Turn on something. """
        sp = spotipy.Spotify(auth=self.__get_access_token())
        sp.pause_playback()

    def resume_playing(self):
        """ Turn of something. """
        sp = spotipy.Spotify(auth=self.__get_access_token())
        sp.start_playback()

    def next_track(self):
        """ Turn of something. """
        sp = spotipy.Spotify(auth=self.__get_access_token())
        sp.next_track()
