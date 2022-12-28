import pandas as pd

scraper = pd.read_html('https://www.mtggoldfish.com/archetype/pioneer-mono-white-humans#paper')

for index, table in enumerate(scraper):
    print('*************')
    print(index)
    print(table)

print(scraper[0])