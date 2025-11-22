import httpx
import base64

# wordpress credentials
username = 'SeoMind'
password = 'ZNBi dbiK B5fu zQ04 WA97 K5w6'
credential = f'{username}:{password}'
token = base64.b64encode(credential.encode())
wp_header = {'Authorization':f'Basic {token.decode("utf-8")}'}
url_endpoint = 'https://seoz.wuaze.com/wp-json/wp/v2/media'


# Image Path
# rb = file is read in byte mode
file_path = open('images/image_0.webp', 'rb') 
img_files = {'file':file_path}

res = httpx.post(url_endpoint, files=img_files, headers=wp_header)
print(res)