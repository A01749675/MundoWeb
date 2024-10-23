import requests
from bs4 import BeautifulSoup
from pprint import pprint
URL = "https://www.thebluealliance.com/"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")

print(soup.prettify())
results = soup.find("table")

events = results.find_all("tr")

result = {}

for event in events:
    
    data = event.find("td")
    if data: 
        print("_________________--")
        print(data)
        a = data.find("a")
        direction = data.find("small")
        result[a["title"]] = (a["title"],URL+a["href"][1:],direction.text)

for r in result:
    print(f"Event: {result[r][0]}, URL: {result[r][1]}, Direction: {result[r][2]}")
        


