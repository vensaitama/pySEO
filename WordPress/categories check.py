import httpx 
from pprint import pprint

url_endpoint = 'https://seoz.wuaze.com/wp-json/wp/v2/categories'

respond = httpx.get(url_endpoint)
if respond.status_code == 200:
    data = respond.json()
    for categories in data:
        pprint(categories)