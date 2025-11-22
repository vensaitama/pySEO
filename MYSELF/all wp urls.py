from httpx import get
base_url = 'https://rawznaturalpetfood.com/wp-json/wp/v2/posts'
page = 1

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}

while True:
    response = get(f'{base_url}?page={page}', headers=headers, timeout=60.0)
    data = response.json()
    if not data or response.status_code != 200:
        break
    for posts in data:
        try:
            print(posts.get('slug'))
        except:
            print('Page not Found')
    page += 1
    