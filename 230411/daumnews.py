import requests
from bs4 import BeautifulSoup

# 다음 뉴스 크롤링
# url = "https://news.daum.net/"
url = "https://news.daum.net/digital#1"
res = requests.get(url)
res.raise_for_status()
soup = BeautifulSoup(res.text, "lxml")
# print(soup) -> 전체 코드

# 다음 뉴스 제목 + 링크 주소 스크래핑
news = soup.find_all("a", attrs={"class":"link_txt"})
# print(news) -> class = link_txt 인 a 태그만 추출

# 5개 뉴스의 제목 + 링크 주소 추출
# for idx, new in enumerate(news):
#     title = new.get_text()
#     link = new["href"]
#     print(title, link)
#     if idx >= 4:
#         break
    
# 다음 IT 뉴스의 상위 5개의 제목 + 링크 주소 추출
# print(news)
# for idx, new in enumerate(news):
#     title = new.get_text()
#     link = new["href"]
#     print(title, link)
#     if idx >= 4:
#         break
    
