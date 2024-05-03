import requests
from bs4 import BeautifulSoup
import json
import time
import re

# スクレイピング対象のURL
url = "https://jigen.net/data/%E5%B8%B8%E7%94%A8%E6%BC%A2%E5%AD%97?rs=1000&so=0&ou=000&od=DESC&pg="

# 3ページ分のURLを取得
kanji_url = []
for i in range(3):
    response = requests.get(url+str(i+1))
    html = response.text
    soup = BeautifulSoup(html, "html.parser")
    kanji_url += soup.find("ul", {"class": "ka_list"}).find_all("a")


# 漢字構成を取得
data = {}
progress = 0
for j in kanji_url:
    href = j.get("href")
    url  = "https://jigen.net"+href
    soup = BeautifulSoup(requests.get(url).text, "html.parser")
    kanji = soup.strong.text
    ids = [x.text for x in soup.find(id = "kjid").find_all("dl")[1].find("dt",string="漢字構成").next_sibling.find_all("li")]
    for i in range(len(ids)):
        ids[i-1] = re.sub(r'#[0-9]*', '', ids[i-1])
    data[kanji] = ids
    time.sleep(1)
    progress += 1
    if progress % 100 == 0:
        print(progress)

# ファイルに保存
with open('data/joyo.json', mode='w') as f:
    f.write(json.dumps(data,indent=4))
