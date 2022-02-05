import requests
import json
import datetime
class GeoAPI:
	

	API_KEY = "d81015613923e3e435231f2740d5610b"
	LAT = "-35.836948753554054"
	LON = "-61.870523905384076"
	
	@classmethod
	def is_hot_in_pehuajo(self,cls):

		if cls > 28:
			respuesta= True
		else:
			respuesta= False
		return respuesta
try:		
	geoAPI =  GeoAPI()
	url = "https://api.openweathermap.org/data/2.5/weather"
	querystring = {"lat":geoAPI.LAT,"lon":geoAPI.LON,"appid":geoAPI.API_KEY}
	headers = {
	    'Cache-Control': 'no-cache'
	    }
	response = requests.request("GET", url, headers=headers, params=querystring)
	data = json.loads(response.content)
	cls = data['main']['temp']

	respuesta = geoAPI.is_hot_in_pehuajo(cls)

	print(respuesta)
except Exception as x:
	print(False)