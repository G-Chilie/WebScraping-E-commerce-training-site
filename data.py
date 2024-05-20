import requests
import pandas as pd
from bs4 import BeautifulSoup

url = "https://ticker.finology.in/market/52-week-high"

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
    data = table.find_all("td")
    print(data)