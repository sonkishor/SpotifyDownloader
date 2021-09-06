from facts import getFacts
from flask import Flask 
from flask import redirect
from flask import render_template, request
from flask import url_for
from flask import send_file
import spotifyd
import time
from jyserver import Server
import jyserver.Flask as jsf
import randfacts
import json

app = Flask(__name__)

@app.route('/', methods = ['POST', 'GET'])
def home():
    factlist = getFacts()
    if request.method == "POST":
        link = request.form['link']G:\Python\SpotiWeb\env\Scripts\python.exe
        spotifyd.playlist_title = spotifyd.get_title(link).replace(" ", "")
        print(spotifyd.playlist_title)
        tracks = spotifyd.spotlist(link)
        spotifyd.threadinitiate(tracks)
        time.sleep(4)
        linkp = link[:24] + "/embed/" + link[25:]
        print(linkp)
        return(redirect(url_for('downloading', playlist_title=spotifyd.playlist_title, linkp=linkp)))
    
    return(render_template('index.html', firstfact = randfacts.getFact(), factlist = factlist))

@app.route('/downloading/<playlist_title>', methods = ['POST', 'GET'])
def downloading(playlist_title): 
    if request.method == "POST":
        return(send_file("{}.zip".format(playlist_title)))
    return(render_template('downloaded.html', playlist_title = json.dumps(playlist_title)))


if __name__ == '__main__':
    app.run(debug=True)