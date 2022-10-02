import random
import json
import base64
import requests


def authenticate():
    user = "Rahi"
    password = "t5nC 34nz obVc BUzM c1Nt KQnK"
    creds = user + ':' + password
    cred_token = base64.b64encode(creds.encode())
    header = {'Authorization': 'Basic ' + cred_token.decode('utf-8')}
    return header


def wp_paragraph(text):
    return f"<!-- wp:paragraph -->{text}<!-- /wp:paragraph -->"


def wp_heading(text):
    return f"<!-- wp:heading -->{text}<!-- /wp:heading -->"


content = []

url = 'https://calculator4engineers.com/wp-json/wp/v2'
header = authenticate()

for i in range(3):
    for j in range(3):
        var1 = i
        var2 = j
        outline = {
            'title': {
                '1st title', '2nd title', '3rd title'
            },
            'intro': {
                'This is the 1st intro', 'This is the 2nd intro', 'This is the 3rd intro'
            },
            'header1': {
                f'First header with Stark {var1}', f' First header with saitama {var1}', f'First header with genos {var1}'
            },
            'header1-content': {
                'Upper content 1', 'Upper content 2', 'Upper content 3'
            },
            'header2': {
                f'First header with Hulk {var2}', f' First header with Yami {var2}', f'First header with Luminus {var2}'
            },
            'header2-content': {
                'Lower content 1', 'Lower content 2', 'Lower content 3'
            }
        }
        # data = random.choice(
        # list(outline['title'])) + random.choice(list(outline['intro']))+random.choice(list(outline['header1']))+random.choice(list(outline['header1-content']))+random.choice(list(outline['header2']))+random.choice(list(outline['header2-content']))

        # content1 = f"{random.choice(list(outline['header1']))} {random.choice(list(outline['header1-content']))} {random.choice(list(outline['header2']))}  {random.choice(list(outline['header2-content']))}"

        content_dict = {
            'intro': wp_paragraph(f"<p>{random.choice(list(outline['intro']))}</p>"),
            'header1': wp_heading(f"<h2>{random.choice(list(outline['header1']))}</h2>"),
            'header1-content': wp_paragraph(f"<p>{random.choice(list(outline['header1-content']))}</p>"),
            'header2': wp_heading(f"<h2>{random.choice(list(outline['header2']))}</h2>"),
            'header2-content': wp_paragraph(f"<p>{random.choice(list(outline['header2-content']))}</p>")
        }
        content = content_dict['intro']+content_dict['header1'] + \
            content_dict['header1-content'] + \
            content_dict['header2']+content_dict['header2-content']

        post = {
            'title': random.choice(list(outline['title'])),
            # 'slug': postslug,
            'content': content,
            'status': 'publish',
            # 'author':'235',
            'publish': 'standard',
            'categories': '3'
        }
        wprequest = requests.post(url + '/posts', headers=header, json=post)
#Rahi