from httpx import get
page = 1
base_url = 'https://prospectengine.com/wp-json/wp/v2'
api_url =f'{base_url}/posts?page={page}'

while True:
    req = get(api_url, timeout=30.0)
    if req.status_code == 200:
        data = req.json()

        for posts in data:
            post = posts.get('link')
            print(post)

    page += 1