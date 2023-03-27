import requests
from bs4 import BeautifulSoup

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://movie.daum.net/ranking/reservation',headers=headers)

soup = BeautifulSoup(data.text, 'html.parser')
#print(soup)
# 내가 원하는 위치에 있는 데이터 가져오기

# #mainContent > div > div.box_ranking > ol > li
# #mainContent > div > div.box_ranking > ol > li:nth-child(1) > div > div.thumb_cont > strong
# #mainContent > div > div.box_ranking > ol > li:nth-child(1) > div > div.thumb_cont > span.txt_append > span:nth-child(1)
# #mainContent > div > div.box_ranking > ol > li:nth-child(2) > div > div.thumb_cont > span.txt_append > span:nth-child(1)

movies = soup.select("#mainContent > div > div.box_ranking > ol > li")

rank = 0
for movie in movies:
    movie_name = movie.select_one("div > div.thumb_cont > strong")
    movie_point = movie.select_one("span.txt_append")
    # 평점만 : movie_point = movie.select_one("span.info.txt")
    # 만약에 movie_name이 None이 아니면 text를 출력
    if movie_name is not None:
        rank = rank + 1
        print(rank, movie_name.text, movie_point.text)