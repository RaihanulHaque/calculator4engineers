from math import floor, sqrt
import json
import base64
import requests
from primeFactorVisualizer import generateImages
import random


def authenticate():
    user = "Rahi"
    password = "t5nC 34nz obVc BUzM c1Nt KQnK"
    creds = user + ':' + password
    cred_token = base64.b64encode(creds.encode())
    header = {'Authorization': 'Basic ' + cred_token.decode('utf-8')}
    return header


def isPrime(n):
    if (n <= 1):
        return False
    for i in range(2, int(sqrt(n))+1):
        if (n % i == 0):
            return False
    return True


def nearestPrime(n):
    if (n & 1):
        n -= 2
    else:
        n -= 1
    i, j = 0, 3
    for i in range(n, 2, -2):
        if (i % 2 == 0):
            continue
        while (j <= floor(sqrt(i)) + 1):
            if (i % j == 0):
                break
            j += 2
        if (j > floor(sqrt(i))):
            return i
    # It will only be executed when n is 3
    return 2


def wp_h2(text):
    return f"<!-- wp:heading {{\"level\":2}} --><h2>{text}</h2><!-- /wp:heading -->"


def wp_h3(text):
    return f"<!-- wp:heading {{\"level\":3}} --><h3>{text}</h3><!-- /wp:heading -->"


def wp_h4(text):
    return f"<!-- wp:heading {{\"level\":4}} --><h4>{text}</h4><!-- /wp:heading -->"


def image_upload(path):
    media = {'file': open(path, 'rb')}
    image = requests.post(url+'/media', headers=header, files=media)
    post_id = json.loads(image.content.decode('utf-8'))['id']
    image_link = image.json()['guid']['rendered']
    locString = f"<!-- wp:image {{\"id\":{str(post_id)},\"sizeSlug\":\"full\",\"linkDestination\":\"none\" }} -->"
    locString += f"<figure class=\"wp-block-image size-full\"><img src=\"{image_link}\" alt=\"\" class=\"wp-image-{str(post_id)}\"/></figure>"
    locString += "<!-- /wp:image -->"
    code = locString
    return code


def featured_image_upload(path):
    media = {'file': open(path, 'rb')}
    image = requests.post(url+'/media', headers=header, files=media)
    post_id = json.loads(image.content.decode('utf-8'))['id']
    return post_id


# header = authenticate()
# url = 'https://calculator4engineers.com/wp-json/wp/v2'

n = 179753
# image_list = generateImages(n)[len(generateImages(n))-1]
# random_image = random.choice(image_list)
# content = wp_h2("Baka Rahi")
# post = {
#     'title': "Rahi senpai",
#     # 'slug': postslug,
#     'content': content,
#     'status': 'publish',
#     # 'author':'235',
#     'publish': 'standard',
#     'categories': '3',
#     'featured_media': str(featured_image_upload(random_image))
# }
# wprequest = requests.post(url + '/posts', headers=header, json=post)
# print(wprequest)
print(nearestPrime(n))
