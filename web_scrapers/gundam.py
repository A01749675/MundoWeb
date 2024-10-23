import requests
from bs4 import BeautifulSoup

URL = "https://gundam.fandom.com/wiki/Mobile_Suit_Gundam:_Char%27s_Counterattack"
page = requests.get(URL)


def getGundamContent():
    soup = BeautifulSoup(page.content, "html.parser")
    raw = soup.find("p")
    values = raw.find_all("i")
    result = []
    for val in values:
        result.append(val.text)
    return result

print(getGundamContent())

#page_elements = results.find_all("div", class_ = "mw-parser-output")

#for page_text in page_elements:
    #text_element = page_text.find("p")
    #print(text_element.text.strip())

#for job_element in job_elements:
    #title_element = job_element.find("h2", class_ = "title")
    #company_element = job_element.find("h3", class_ = "company")
    #location_element = job_element.find("p", class_ = "location")
    #print(title_element.text.strip())
    #print(company_element.text.strip())
    #print(location_element.text.strip())
    #print()

#python_jobs = results.find_all("h2", string = lambda text: "python" in text.lower())
#print(python_jobs)

#python_job_elements = [
    #h2_element.parent.parent.parent for h2_element in python_jobs
#]

#for job_element in python_job_elements:
    #title_element = job_element.find("h2", class_ = "title")
    #company_element = job_element.find("h3", class_ = "company")
    #location_element = job_element.find("p", class_ = "location")
    #print(title_element.text.strip())
    #print(company_element.text.strip())
    #print(location_element.text.strip())
    #print()

    #links = job_element.find_all("a")
    #for link in links:
        #link_url = link["href"]
        #print(f"Apply here: {link_url}\n")

#print(page.text)
#print(results.prettify())
