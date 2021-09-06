import spotipy
import spotipy.oauth2 as oauth2
from spotipy.oauth2 import  SpotifyClientCredentials
from pprint import pprint
import json
from youtubesearchpython import VideosSearch
import concurrent.futures
import time
import os
import pafy
from zipfile import ZipFile

auth_manager = SpotifyClientCredentials(client_id="32568dfa826a42619a4ba6cdd55a4d66", client_secret="67c44f1f60b7427298935835a01bd6a5")
sp = spotipy.Spotify(auth_manager=auth_manager)
playlist_title = ""
def spotlist(url):
    tracks = []
    playlist = sp. playlist_tracks(url, fields=None, limit=100, offset=0, market=None, additional_types=('track', ))
    total_songs = playlist['total']

    for i, item in enumerate(playlist['items']):
        tracks.append(item['track']['name'] + ' - ' + item['track']['artists'][0]['name'] + ' - ' + item['track']['album']['name'])
        if i >= 99:
            playlist = sp. playlist_tracks(url, fields=None, limit=total_songs-100, offset=100, market=None, additional_types=('track', ))
            for item in playlist['items']:
                tracks.append(item['track']['name'] + ' - ' + item['track']['artists'][0]['name'] + ' - ' + item['track']['album']['name'])
    return tracks

def get_title(url):
    title = sp.playlist(url, fields="name")
    return title["name"]

def getSong(song):
    videosSearch = VideosSearch(song, limit = 1)
    resultlink = videosSearch.result()['result'][0]['link']
    video = pafy.new(resultlink)
    songdown = video.getbestaudio()
    songdown.download("\Downloaded\{}\{}.m4a".format(playlist_title,song))

# finallist = spotlist("https://open.spotify.com/playlist/37i9dQZF1DWVq1SXCH6uFn")

def threadinitiate(finallist):
    downloadedpath = "Downloaded"
    if not os.path.exists(downloadedpath):
        os.makedirs(downloadedpath)
    path = "Downloaded\{}".format(playlist_title)
    if not os.path.exists(path):
        os.makedirs(path)
    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as executor:
        executor.map(getSong, finallist)
    downloaded = "{}.zip".format(playlist_title)
    files = os.listdir("Downloaded\{}".format(playlist_title))
    print(files)
    with ZipFile(downloaded, 'w') as  zip:
        for file in files:
            zip.write("Downloaded\{}\{}".format(playlist_title,file), arcname="/{}/{}".format(playlist_title,file))
            os.remove("Downloaded\{}\{}".format(playlist_title,file))


# end = time.time()
# print(end-start)