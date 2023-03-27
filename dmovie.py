import requests
from bs4 import BeautifulSoup

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://movie.daum.net/ranking/reservation',headers=headers)

soup = BeautifulSoup(data.text, 'html.parser')
#print(soup)
# 내가 원하는 위치에 있는 데이터 가져오기

# #mainContent > div > div.box_ranking > ol > li
# #mainContent > div > div.box_ranking > ol > li:nth-child(1) > div > div.thumb_cont > strong

lis = soup.select("#mainContent > div > div.box_ranking > ol > li")

rank = 0
for li in lis:
    a_tag = li.select_one("div > div.thumb_cont > strong")
    # 만약에 a_tag 가 None이 아니면 text를 출력
    if a_tag is not None:
        rank = rank + 1
        print(rank, a_tag.text)