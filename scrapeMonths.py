import requests
import json
from bs4 import BeautifulSoup

page = requests.get("https://nettime.org/Lists-Archives/")
soup = BeautifulSoup(page.text, 'html.parser')

nettime_block = soup.find("strong", string="nettime-lat").parent
monthLinks = []
for link in nettime_block.find_all('a'):
    monthLinks.append(link.get('href'))

monthPages = []
for month in monthLinks:
    monthSoup = BeautifulSoup(requests.get("https://nettime.org/Lists-Archives/" + month).text, 'html.parser')

    monthObj = {}
    monthObj['link'] = "https://nettime.org/Lists-Archives/" + month
    monthObj['date'] = monthSoup.find('title').get_text()[12:]
    monthObj['messages'] = []

    for message in monthSoup.select('strong a'):
        monthObj['messages'].append(message.get('href'))

    monthPages.append(monthObj)


with open('data.json', 'w') as outfile:
    json.dump(monthPages, outfile)