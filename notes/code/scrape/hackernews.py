import requests
from bs4 import BeautifulSoup

response = requests.get("https://news.ycombinator.com/newest")
html = BeautifulSoup(response.content, "html.parser")

for link in html.find_all(class_="storylink"):
    print link['href'], link.text
