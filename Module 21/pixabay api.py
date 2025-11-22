import httpx
from pprint import pprint
keyword = input('Search for images..').replace(' ','+')
api = '52999339-bbb9ecedbdf4261e28b2e5861'
url = f'https://pixabay.com/api/?key={api}&q={keyword}&image_type=photo'
response = httpx.get(url)
data = response.json()
hits = data.get('hits')

image_id = 0
for image in hits:
    image_url = image.get('largeImageURL')
    res = httpx.get(image_url)
    if res.status_code == 200:
        with open(f'downloaded_img_{image_id}.jpg', 'wb') as file:
            file.write(res.content)
    image_id += 1