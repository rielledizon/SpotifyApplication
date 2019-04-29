import sys
import spotipy
import spotipy.util as util
import os

def show_tracks(tracks):
    for i, item in enumerate(tracks['items']):
        track = item['track']
        print("   %d %32.32s %s" % (i, track['artists'][0]['name'],
            track['name']))


if __name__ == '__main__':
    username = input("Enter your username: ")
    try:
        os.remove(".cache-"+username)
    except:
        pass
    token = util.prompt_for_user_token(username, client_id='d1eebb993a9849288e221d27b95158f5',
    client_secret='0115f96419b848c0a5e2e28d1257618e',redirect_uri='http://www.google.com')

    if token:
        sp = spotipy.Spotify(auth=token)
        playlists = sp.user_playlists(username)
        for playlist in playlists['items']:
            if playlist['owner']['id'] == username:
                print()
                print(playlist['name'], playlist['uri'])
                print('  total tracks', playlist['tracks']['total'])
                results = sp.user_playlist(username, playlist['id'],
                    fields="tracks,next")
                tracks = results['tracks']
                show_tracks(tracks)
                while tracks['next']:
                    tracks = sp.next(tracks)
                    show_tracks(tracks)
    else:
        print("Can't get token for", username)
