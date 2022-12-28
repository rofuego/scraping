import pandas as pd
import requests
from bs4 import BeautifulSoup

url = 'https://www.mtggoldfish.com/archetype/pioneer-mono-white-humans#paper'

scraper = pd.read_html(url)

response = requests.get(url)
bs = BeautifulSoup(response.text, "html.parser")
title = bs.find(class_="title").text.split("\n")[1]
format = bs.find(class_="deck-container-information").text.split("\n")[1]

""" for index, table in enumerate(scraper):
    print('*************')
    print(index)
    print(table) """

print("Deck: " + title)
print(format)
print(scraper[0])
