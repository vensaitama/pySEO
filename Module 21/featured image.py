import httpx
import base64

# WordPress URLs
base_url = 'https://seoz.wuaze.com/wp-json/wp/v2'
post_url = f'{base_url}/posts'
media_url = f'{base_url}/media'

# wordpress credentials
username = 'SeoMind'
password = 'ZNBi dbiK B5fu zQ04 WA97 K5w6'
credential = f'{username}:{password}'
token = base64.b64encode(credential.encode())
wp_header = {'Authorization':f'Basic {token.decode("utf-8")}'}

# Uploading Image File
file_path = open('images/image_2.webp', 'rb')
wp_img = {'file':file_path}
res = httpx.post(media_url, files=wp_img, headers=wp_header)
media_id = res.json().get('id')

data = {
    'title' : 'This is a demo title',
    'status' : 'publish',
    'content' : 'Thiiiiiiis isss a demo content',
    'featured_media': media_id
}

post_response = httpx.post(post_url, headers=wp_header, json=data)
print(post_response)