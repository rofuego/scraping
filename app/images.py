import os

import requests
from bs4 import BeautifulSoup

url = "https://scryfall.com/sets/mat"

response = requests.get(url)

soup = BeautifulSoup(response.content, 'html.parser')

img_tags = soup.find_all('img')

if not os.path.exists('images'):
    os.makedirs('images')

for img in img_tags:
    img_url = img['src']
    filename = os.path.join('images', img['alt'] + '.jpg')
    with open(filename, 'wb') as f:
        f.write(requests.get(img_url).content)
