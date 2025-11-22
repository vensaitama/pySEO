import httpx 
url = 'https://seoz.wuaze.com/wp-json/wp/v2/categories?hide_empty=False'

res = httpx.get(url)
if res.status_code == 200:
    data = res.json()
    categories = {}
    for d in data:
        categories[d['name']] = d['id']
print(categories)