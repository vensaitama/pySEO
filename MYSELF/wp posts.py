from httpx import get
base_url = 'https://rawznaturalpetfood.com/wp-json/wp/v2'
headers = {
    'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/141.0.0.0 Safari/537.36'
}
page = 1
while True:
    api_url = f'{base_url}/posts?page={page}'
    request = get(api_url, headers = headers, timeout = 60.0)
    data = request.json()

    if not data or request.status_code != 200:
        break

    for posts in data:
        try:
            print(posts.get('link'))
        except:
            print("Urls not found")
    
    page += 1