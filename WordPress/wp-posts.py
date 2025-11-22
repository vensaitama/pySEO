from httpx import get
from pprint import pprint

headers = {
    'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36'
}

page = 1
base_url = 'https://www.tantan.com/wp-json/wp/v2'

while True:
    api_endpoint = f'{base_url}/pages?page={page}'
    response = get(api_endpoint, headers=headers, timeout=360.0)
    data = response.json()

    if not data or response.status_code != 200:
        break

    for posts in data:
        try:
            print(posts.get('link'))
        except:
            print('Urls not found')

    page += 1