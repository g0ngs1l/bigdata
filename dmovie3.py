import requests
from bs4 import BeautifulSoup

# 내가 만든 모듈(함수)를 포함시키기
#import func
from func import my_print

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://movie.daum.net/ranking/reservation',headers=headers)

soup = BeautifulSoup(data.text, 'html.parser')
rank = 0

movies = soup.select(".thumb_cont")
for tr in movies:
    rank = rank + 1
    a_tag = tr.select_one("a")
    my_print(f'{rank}위 {a_tag.text}')
    txt_grade = tr.select_one("span.txt_grade")
    my_print(f'평점: {txt_grade.text}')
    txt_num = tr.select_one("span.txt_num")
    my_print(f'예매율: {txt_num.text}')
    txt_date = tr.select_one(".txt_info > span.txt_num")
    my_print(f'개봉날짜: {txt_date.text}')