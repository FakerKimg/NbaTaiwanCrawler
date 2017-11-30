import requests
from bs4 import BeautifulSoup
from datetime import datetime
import json

response = requests.get("https://nba.udn.com/nba/index?gr=www")
soup = BeautifulSoup(response.text, "html.parser")
hrefs = [tag['href'] for tag in soup.find(id="news_body").find_all('a')]

for href in hrefs:
    response = requests.get("https://nba.udn.com" + href)
    soup = BeautifulSoup(response.text, "html.parser")
    data = {}
    data["title"] = soup.select("h1.story_art_title")[0].text
    dtstr = soup.select("div.shareBar__info--author > span")[0].text
    datetime_object = datetime.strptime(dtstr, "%Y-%m-%d %H:%M")
    data["datetime"] = datetime_object.isoformat()
    data["href"] = href.replace("/", "-")
    content = []
    tags = soup.select("#story_body_content > span")[0].contents
    text = ""
    i = 0
    while i < len(tags):
        tag = tags[i]
        if tag.name == "figure":
            content.append("text:" + text)
            text = ""
            content.append("img:" + tag.select("a[href]")[0]["href"])
        elif tag.name == "p":
            content.append("text:" + text)
            text = ""
            tags = tag.contents
            i = -1
        elif tag.name == None:
            text = text + str(tag)
        else:
            text = text + tag.text
        i = i + 1
    data["content"] = content
    #print(data)
    response = requests.put("http://localhost:8000/news_upload/", data=json.dumps(data))
    print(response)

