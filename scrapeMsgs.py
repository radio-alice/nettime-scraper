import json
import requests
from bs4 import BeautifulSoup

with open("data.json", "r") as read_file:
    data = json.load(read_file)

for month in data:
    link = month["link"][:-12]
    filename = month["date"].replace(" ", "") + ".txt"
    #messageObjs = []
    with open(filename, 'w+') as outfile:
        for message in month["messages"]:
            messageSoup = BeautifulSoup(requests.get(link + message).text, 'html.parser')
            header = messageSoup.select('b font')[0].get_text()
            outfile.write("date: " + header[-26:-6].encode('UTF-8', 'xmlcharrefreplace') + "\n")
            outfile.write("sender: " + header[:-30].encode('UTF-8', 'xmlcharrefreplace') + "\n")
            if len(messageSoup.find_all('pre')) > 1:
                text = messageSoup.find_all('pre')[1].get_text()
            else:
                text = messageSoup.find_all('pre')[0].get_text()
            outfile.write("body: " + text.encode('UTF-8', 'xmlcharrefreplace') + "\n")
            #messageObjs.append(messageObj)
            outfile.write("---------\n\n")




