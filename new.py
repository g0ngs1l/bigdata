import requests
from bs4 import BeautifulSoup
import csv
from openpyxl import Workbook

# 엑셀파일 쓰기
write_wb = Workbook()

# Sheet1에다 입력
write_ws = write_wb.active

# 컬럼 데이터 입력
write_ws['A1'] = '순위'
write_ws['B1'] = '제목'
write_ws['C1'] = '평점'
write_ws['D1'] = '예매율'
write_ws['E1'] = '개봉날짜'

# url = 'https://movie.daum.net/ranking/reservation'

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://movie.daum.net/ranking/reservation',headers=headers)

soup = BeautifulSoup(data.text, 'html.parser')
rank = 0

movies = soup.select(".thumb_cont")
for tr in movies:
    rank = rank + 1
    a_tag = tr.select_one("a")
    m1 = f'{rank}위' # 순위
    m2 = a_tag.text # 제목
    txt_grade = tr.select_one("span.txt_grade")
    m3 = txt_grade.text # 평점
    txt_num = tr.select_one("span.txt_num")
    m4 = txt_num.text # 예매율
    txt_date = tr.select_one(".txt_info > span.txt_num")
    m5 = txt_date.text # 개봉날짜

    # 행 단위로 추가
    write_ws.append([m1, m2, m3, m4, m5])

# 엑셀 파일 저장
write_wb.save('영화순위.xlsx')