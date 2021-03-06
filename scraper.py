import requests
from scraperwiki import sqlite
from transform import to_entries

content = requests.get("http://www.bbc.co.uk/radio1/chart/singles/print")
data = to_entries(content.content)

print("Importing %d rows" % len(data))

sqlite.save(unique_keys=['date', 'position'], data=data, table_name="chart")
