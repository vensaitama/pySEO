api = {
"status": "success",
"country": "Canada",
"countryCode": "CA",
"region": "Qc",
"regionName": "Quebec",
"city": "Montreal",
"zip": "H3V",
"lat": 45.4998,
"lon": -73.6087,
"timezone": "Americe/Toronto",
"isp": "Le Groupe Videotron Ltee",
"org": "videotron Ltee",
"as": "ASS769 Videotron Telecon Ltee",
"query": "24.48.0.1"
}

# 24.48.0.1 IP address is located in Canada. Its longitude and latitude is ... ...

ip_address = api.get("query")
country_address = api.get("country")
latitude = api.get("lat")
longitude = api.get("lon")
sentence = f'{ip_address} IP address is located in {country_address}. Its longitude and latitude is {longitude} , {latitude}'

print(sentence)