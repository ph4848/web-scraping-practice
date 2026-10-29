import requests
from bs4 import BeautifulSoup

url = "https://www.python.org/"
response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")
#print(soup)

context_events = soup.select("div.medium-widget.event-widget.last ul li a")
for item in context_events:
    print(item.get_text())
    print('-' * 28)

context_events_time = soup.select("div.medium-widget.event-widget.last ul li time")
for item in context_events_time:
    print(item.get_text())
    print('-' * 35)


'''
context = soup.select_one("div.medium-widget.applications-widget.last")
#print(context)
for item in context:
    print(item.get_text())
    print('-' * 27)


latests_news = soup.find("div", attrs={"class": "medium-widget blog-widget"})
#print(latests_news)

times = latests_news.find_all("time")

for item in times:
    print(item.get_text())
    print("-" * 20)
#--------------------------------
titles = latests_news.find_all("a")
#print(titles)

for item in titles:
    print(item.get_text())
    print("-" * 20)
'''