import httpx
import base64

# WordPress Urls
base_url = 'https://pyseo.ct.ws/wp-json/wp/v2'
post_url = f'{base_url}/posts'
media_url = f'{base_url}/media'

# WordPress Credentials
username = 'pySeo_ws'
password = 'cJ4u k9mA b8tK X6RO HFKY k4vP'
credential = f'{username}:{password}'
token = base64.b64encode(credential.encode())
wp_header = {'Authorization':f'Basic {token.decode("utf-8")}'}

# Uploading the image
def image_uploader(img_path, img_alt):
    img_open = open(img_path, 'rb')
    img_file = {'file':img_open}
    img_upload = httpx.post(media_url, files=img_file, headers=wp_header)
    media_data = img_upload.json()
    img_id = media_data.get('id')
    img_src = media_data.get('guid').get('rendered')
    code = f'<!-- wp:image {{"id":{img_id},"sizeSlug":"large","linkDestination":"none","align":"center"}} --><figure class="wp-block-image aligncenter size-large"><img src="{img_src}" alt="{img_alt}" class="wp-image-{img_id}"/><figcaption class="wp-element-caption">The Cloudy weather and The birds on the Tree</figcaption></figure><!-- /wp:image -->'
    return code, img_id

first_img, image_first_id = image_uploader('images/image_0.webp', 'Mobile Phone')
second_img, image_second_id = image_uploader('images/image_1.webp', 'Mobile Phone')
third_img, image_third_id = image_uploader('images/image_2.webp', 'Mobile Phone')
fourth_img, image_fourth_id = image_uploader('images/image_3.webp', 'Mobile Phone')
fifth_img, image_fifth_id = image_uploader('images/image_4.webp', 'Mobile Phone')

text = '<!-- wp:paragraph --><p>This is a demo text.</p><!-- /wp:paragraph -->'

content = first_img + text + second_img + text + third_img + text + fourth_img + text + fifth_img
post_data = {
    'title' : 'This is a New Demo Post Title',
    'status' : 'publish',
    'content' : content,
    'featured_media' : image_fifth_id
}

respond = httpx.post(post_url, json=post_data, headers=wp_header, timeout=360.0)
print(respond)