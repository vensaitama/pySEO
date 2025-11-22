from httpx import get
from pprint import pprint
base_url = 'https://prospectengine.com/wp-json/wp/v2'

post_api_url = f'{base_url}/posts?per_page=100'
r = get(post_api_url).json()

for i in r:
    try:
        print(i.get('link'))
    except:
        print("Posts not Found")