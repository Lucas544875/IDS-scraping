import requests
from bs4 import BeautifulSoup

# スクレイピング対象の URL にリクエストを送り HTML を取得する
res = requests.get("https://jigen.net/data/%E5%B8%B8%E7%94%A8%E6%BC%A2%E5%AD%97?rs=300&so=0&ou=000&od=DESC&pg=1")

# レスポンスの HTML から BeautifulSoup オブジェクトを作る
soup = BeautifulSoup(res.text, 'html.parser')

# title タグの文字列を取得する
# title_text = soup.find('title').get_text()
# print(title_text)
# > Quotes to Scrape
kanjis = soup.find_all('td', {'class': 'td2'})

# class が quote の div 要素を全て取得する
# quote_elms = soup.find_all('div', {'class': 'quote'})
# print(len(quote_elms))
# > 10
