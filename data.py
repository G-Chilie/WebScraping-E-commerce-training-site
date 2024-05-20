import requests
import pandas as pd
from bs4 import BeautifulSoup

url = "https://ticker.finology.in/market/52-week-high"
r = requests.get(url)

soup = BeautifulSoup(r.text, "lxml")

table = soup.find("table", class_ = "table table-sm table-hover screenertable")
headers = table.find_all("th")

titles = []
for i in headers:
    title = i.text
    titles.append(title)

    df = pd.DataFrame(columns=title)

    rows = table.find_all("tr")

for i in rows[1:]:
    data = i.find_all("td")
    ##print(data)
    row = [tr.text for tr in data]
    print(row)
    l = len(df)
    df.loc[l] = row

print(df)    


URL = "https://uk.indeed.com/jobs?q&l=Norwich%2C%20Norfolk&vjk=139a4549fe3cc48b"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")

results = soup.find(id="ResultsContainer")

job_elements = results.find_all("div", class_="resultContent")

python_jobs = results.find_all("h2", string="Python")

for job_element in job_elements:
    title_element = job_element.find("h2", class_="jobTitle")
    company_element = job_element.find("span", class_="companyName")
    location_element = job_element.find("div", class_="companyLocation")
    print(title_element)
    print(company_element)
    print(location_element)
    print()