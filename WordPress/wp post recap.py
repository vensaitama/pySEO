import httpx
import base64

endpoint_url = 'https://seoz.wuaze.com/wp-json/wp/v2/'

def wp_create(type_of_creation, data):
    wp_user = 'SeoMind'
    wp_password = 'ZNBi dbiK B5fu zQ04 WA97 K5w6'
    wp_credential = f'{wp_user}:{wp_password}'
    token = base64.b64encode(wp_credential.encode())
    wp_headers = {'Authorization':f'Basic {token.decode("utf-8")}'}
    res = httpx.post(f'{endpoint_url}{type_of_creation}', json=data, headers=wp_headers)
    

para = 'The Block Editor is a modern paradigm for WordPress site building and publishing. It uses a modular system of blocks to compose and format content and is designed to create rich and flexible layouts for websites and digital products.'
post_data = {
        'title' : 'This is a demo title',
        'content': para,
        'categories' : 176
    }

post = wp_create('posts', post_data)
print(f'{post} posted')