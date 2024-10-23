import requests
from bs4 import BeautifulSoup
from pprint import pprint
URL = "https://www.thebluealliance.com/"
page = requests.get(URL)


def getRegionalData():
    soup = BeautifulSoup(page.content, "html.parser")
    results = soup.find("table")
    events = results.find_all("tr")
    result = []
    for event in events:
        data = event.find("td")
        if data: 
            a = data.find("a")
            direction = data.find("small")
            result.append({"event":a["title"],"url":URL+a["href"][1:],"direction":direction.text})
    return result


