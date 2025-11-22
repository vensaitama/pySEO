api = {
"status": "success",
"country": "Canada",
"countryCode": "CA",
"region": "QC",
"regionName": "Quebec" ,
"City": "Montreal",
"zip": "H3V",
"Lat": 45.4998,
"Lon": - 73.6087,
"timezone": "America/Toronto" ,
"isp": "Le Groube Videotron Ltee",
"org": "Videotron Ltee",
"as": "AS5769 Videotron Telecom Ltee",
"query": "24.48.0.1"
}

# 24.48.0.1 IP Adress is located in Canada. It's longitute and letitude is ----

ip_address = api.get("query")
country = api.get("country")
longitude = api.get("Lat")
letitude = api.get("Lon")

sentence = f'{ip_address} IP Adress is located in {country}. Its longitute and letitude is {longitude}, {letitude} respectively.'

print(sentence)
