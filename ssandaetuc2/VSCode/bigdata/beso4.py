import requests
from bs4 import BeautifulSoup

# 크롤링의 일반적인 예
url = "https://comic.naver.com/webtoon"
headers = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36"}
res = requests.get(url, headers=headers)
res.raise_for_status()

# 스크래핑의 일반적인 예
soup = BeautifulSoup(res.text, "lxml")
# print(soup)

# 문자열 추출
# print(soup.title.get_text())

# soup 객체에서 처음 발견되는 div element를 출력
# print(soup.div)

# div element의 속성 정보를 출력
# print(soup.div.attrs)

# div element의 속성 중에서 id 속성 정보를 출력
# print(soup.div["id"])

# "id":"root"인 div 태그를 출력해라
# print(soup.find("div", attrs={"id":"root"}))

# "id":"root"인 태그
# print(soup.find(attrs={"id":"root"}))


test1 = (soup.find(attrs={"id":"root"}))
# 다음 태그 출력
# test1.next_sibling
# test2 = test1.next_sibling.next_sibling
# print(test2)
# 이전 태그 출력
# test1.previous_sibling

# next, previous 두 번 사용하기 불편할 때
# test3 = soup.find("div")
print(test1.find_next_sibling("div"))