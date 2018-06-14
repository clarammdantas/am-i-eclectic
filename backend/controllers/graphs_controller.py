import sys
import os
sys.path.append(os.path.realpath('../services'))

from flask import Flask
from lastfm_api_service import LastfmAPIService

app = Flask(__name__)
lastfmAPI = LastfmAPIService()

@app.route("/")
def hello():
	return lastfmAPI.get_top_artists("clarammd", 50)

if __name__ == '__main__':
	app.run(debug = True)	
