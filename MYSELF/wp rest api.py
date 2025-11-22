from httpx import get

base_url = 'https://prospectengine.com/wp-json/wp/v2/posts'
page = 1 #Starts from the first page

while True:
    response = get(f'{base_url}?page={page}', timeout=30.0)
    data = response.json()

    if not data or response.status_code !=200:
        break

    for posts in data:
        try:
            print(posts.get('slug'))
        except:
            print('posts not found')
    page += 1



