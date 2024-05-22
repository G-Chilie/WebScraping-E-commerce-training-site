import requests
from bs4 import BeautifulSoup

for i in range(2,11):
    url = "https://www.flipkart.com/mobiles/pr?sid=tyy%2C4io&p%5B%5D=facets.brand%255B%255D%3DOPPO&param=1001&ctx=eyJjYXJkQ29udGV4dCI6eyJhdHRyaWJ1dGVzIjp7InRpdGxlIjp7Im11bHRpVmFsdWVkQXR0cmlidXRlIjp7ImtleSI6InRpdGxlIiwiaW5mZXJlbmNlVHlwZSI6IlRJVExFIiwidmFsdWVzIjpbIk9wcG8gc21hcnRwaG9uZXMiXSwidmFsdWVUeXBlIjoiTVVMVElfVkFMVUVEIn19fX19&wid=21.productCard.PMU_V2_20"
    r = requests.get(url)
    print(r)

    soup = BeautifulSoup(r.text, "lxml")

    np = soup.find("a", class_ = "_1LKTO3").get("href")
    cnp = "https://www.flipkart.com"+np
    print(cnp)
    
