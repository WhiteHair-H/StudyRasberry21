from bs4 import BeautifulSoup as bs
from pprint import pprint
import requests as req

# 검색 url
url = 'https://search.naver.com/search.naver?query=%EB%82%A0%EC%94%A8'
html = req.get(url) #웹사이트 가져오기
#pprint(html.text)
soup = bs(html.text, 'html.parser')  # html 문자열에 대해서 , html 파싱

datas = soup.find('div', {'class' : 'detail_box'}) # 미세먼지 영역 찾기
#pprint(finedust)
details = datas.findAll('dd') # 요소 3개 찾기
#pprint(details)

# 미세먼지
finedust = details[0].find('span', {'class', 'num'}).get_text()
# 초미세먼지
ultrafinedust = details[1].find('span', {'class', 'num'}).get_text()
# 오존지수
ozone = details[2].find('span', {'class', 'num'}).get_text()

print('{0}\n{1}\n{2}'.format(finedust, ultrafinedust, ozone))





