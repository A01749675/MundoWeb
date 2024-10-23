import requests
from bs4 import BeautifulSoup
from pprint import pprint
URL = "https://www.thebluealliance.com/"
page = requests.get(URL)


def getRegionalData()->dict:
    soup = BeautifulSoup(page.content, "html.parser")
    results = soup.find("table")
    events = results.find_all("tr")
    result = {}
    for event in events:
        data = event.find("td")
        if data: 
            a = data.find("a")
            direction = data.find("small")
            result[a["title"]] = (a["title"],URL+a["href"][1:],direction.text)
    return result


