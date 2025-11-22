import httpx
import base64
username = 'SeoMind'
password = '7U9D Bum7 hiZH oLJ3 Z5mM fYHu'
credential = f'{username}:{password}'
token = base64.b64encode(credential.encode())
wp_header = {'Authorization':f'Basic {token.decode("utf-8")}'}

wp_data = {
    'name' :'Top-countries',
    'slug' : 'top-countries',
    'description' : 'This is a demo categories.'
}

api_endpoint = 'https://seoz.wuaze.com/wp-json/wp/v2/categories'

req = httpx.post(api_endpoint, data=wp_data, headers=wp_header)
if req.status_code == 201:
    print('Category Created')
else:
    print('Something went wrong!')