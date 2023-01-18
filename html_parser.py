from bs4 import BeautifulSoup
import requests

url = 'https://www.mtggoldfish.com/format-staples/standard/full/lands'

response = requests.get(url)

soup = BeautifulSoup(response.text, 'html5lib')

print(soup.prettify())
