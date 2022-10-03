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

# Math
# user = "WP SEO Geeks"
# password = "e4gB PSHR pLnB qLFL SFDz ITmO"
# Physicsmaniac
# user = "Rahi_"
# password = "rbId ChMZ bHPk 1aFL ibOX 1mwc"


header = authenticate()
url = 'https://calculator4engineers.com/wp-json/wp/v2'

posttitle = "Automation test 101"
postslug = "automation_test_101"
postcontent = "This post is created by python script for testing purpose"
content = "Baka<h2>Rahi</h2><a href="'#'">I am Ironman</a>"
post = {
    'title': posttitle,
    'slug': postslug,
    'content': content,
    'status': 'publish',
    # 'author':'235',
    'publish': 'standard',
    'categories': '3',
    'featured_media': '542'
}
# media = {
#  "file": open(f"images/100_banner_simple.jpg", "rb"),
#  "caption": "caption",
#  "description": "description",
#  "alt_text": "Custom Alt Text",
#  }
# upload_image = requests.post(url + "/media", headers=header, files=media)

wprequest = requests.post(url + '/posts', headers=header, json=post)
print(wprequest)
