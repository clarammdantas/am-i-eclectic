import requests

class MusicDataRequests(object):
	BASE_URL = 'http://ws.audioscrobbler.com/2.0/?method='
	API_KEY = '4a9b74c6b6c51b18a1f08442554256c4'
	SIMILARITY_LIMIT = 100

	def get_top_artists(user_name, number_of_artists):
		url_to_be_requested = BASE_URL + "user.gettopartists&user=" + user_name + "&api_key=" +
								API_KEY + "&format=json&limit=" + number_of_artists

		response = requests.get(url_to_be_requested)

		return response.content


	def get_similar_artists(artist_name):
		url_to_be_requested = BASE_URL + "artist.getsimilar&artist=" + artist_name + "&api_key=" +
								API_KEY + "&format=json&limit" + SIMILARITY_LIMIT

		response = requests.get(url_to_be_requested)

		return response.content 


