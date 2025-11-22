import httpx 
import base64

url = 'https://seoz.wuaze.com/wp-json/wp/v2/categories?per_page=100'

agent_headers = {
    'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36'
}
res = httpx.get(url, headers=agent_headers, timeout=60.0)
if res.status_code == 200:
    data = res.json()
    categories = {}
    for d in data:
        categories[d["name"]] = d['id']

all_ids = list(categories.values())


def wp_create(url, data):
    wp_user = 'SeoMind'
    wp_password = 'ZNBi dbiK B5fu zQ04 WA97 K5w6'
    wp_credential = f'{wp_user}:{wp_password}'
    token = base64.b64encode(wp_credential.encode())
    wp_headers = {'Authorization':f'Basic {token.decode("utf-8")}'}
    res = httpx.post(url, json=data, headers=wp_headers)
    return res.status_code

end_points = 'https://seoz.wuaze.com/wp-json/wp/v2/categories'

for id in all_ids:
    cat_endpoints = f'{end_points}/{id}'
    #print(cat_endpoints)
    res = httpx.get(cat_endpoints)
    data = res.json()
    cat_name = data.get('name') + ' places'
    cat_slug = data.get('slug') + '-places'
    cat_data = {'name':cat_name, 'slug':cat_slug}
    wp_create(cat_endpoints, cat_data)
