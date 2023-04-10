# pypi (Python Package Index) - 패키지 관리 시스템
# 웹서버에 나에게 정보를 달라고 요청하는 패키지

# pip 설치 -> python3 get-pip.py 혹은 python get-pip.py

# web crawling / web scraping
# 크롤링은 요청하면 다 가져옴
# 스크랩핑은 내가 원하는 정보만 추출해서 가져옴

# http 상태코드
# 100번대 -> 정보코드 (요청을 받았고 프로세스를 계속 시작한다.)
# 200번대 -> 성공코드
# 300번대 -> 리다이렉션 코드 (요청 완료를 위해 추가 작업이 필요한 경우)
# 400번대 -> 클라이언트측 오류
# 500번대 -> 서버측 오류

import requests
# res = requests.get("http://google.com")
# 응답코드가 200 이면 정상
# print("응답코드 :", res.status_code)

# 크롤링이 잘 안될 경우 웹브라우저에서 요청하는 것처럼
url = "http://google.com"
headers = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36"}
res = requests.get(url, headers=headers)
# 웹페이지 정상, 비정상일 경우 종료
res.raise_for_status()

print(len(res.text))
print(res.text)

with open("mygoogle.html", "w", encoding="utf8") as f:
    f.write(res.text)
    
# 정규표현식
import re
# . : 하나의 문자를 의미
# ^ : 문자열의 시작
# $ : 문자열의 끝

# re.

# ca.e -> care, cafe, caffee(x), case
# ^de -> desk, destination, fade(x)
# se$ -> case, base, face(x)



