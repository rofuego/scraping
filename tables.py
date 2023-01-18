import pandas as pd

url = 'https://www.mtggoldfish.com/format-staples/standard/full/lands'

sc = pd.read_html(url)

for index, table in enumerate(sc):
    print('*************')
    print(index)
    print(table)
