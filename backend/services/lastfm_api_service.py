import requests

class LastfmAPIService(object):

	def __init__(self):
		self.BASE_URL = 'http://ws.audioscrobbler.com/2.0/?method='
		self.API_KEY = '4a9b74c6b6c51b18a1f08442554256c4'
		self.SIMILARITY_LIMIT = '100'

	def get_top_artists(self, user_name, number_of_artists):
		url_to_be_requested = self.BASE_URL + "user.gettopartists&user=" + user_name + "&api_key=" +\
								self.API_KEY + "&format=json&limit=" + str(number_of_artists)

		response = requests.get(url_to_be_requested)

		return response.content


	def get_similar_artists(self, artist_name):
		url_to_be_requested = self.BASE_URL + "artist.getsimilar&artist=" + artist_name + "&api_key=" +\
								self.API_KEY + "&format=json&limit" + self.SIMILARITY_LIMIT

		response = requests.get(url_to_be_requested)

		return response.content 


