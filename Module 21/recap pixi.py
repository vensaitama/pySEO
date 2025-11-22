import httpx
from pprint import pprint
api ='52999339-bbb9ecedbdf4261e28b2e5861'
keyword = input('Search for images__ ').strip().replace(' ','+')
url =f'https://pixabay.com/api/?key={api}&q={keyword}&image_type=photo&per_page=5'
response = httpx.get(url)
data = response.json()
hits = data.get('hits')
#pprint(hits)

img_id = 0
for image in hits:
    img_url = image.get('largeImageURL')
    res = httpx.get(img_url, timeout=3600.0)
    if res.status_code == 200:
        with open(f'images/image_{img_id}.webp', 'wb') as file:
            file.write(res.content)
    img_id += 1