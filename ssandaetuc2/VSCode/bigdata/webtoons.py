import requests
from bs4 import BeautifulSoup

# url = "https://movie.daum.net/main"
# headers = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36"}
# res = requests.get(url, headers=headers)
# res.raise_for_status()

# soup = BeautifulSoup(res.text, "lxml")
# # print(soup)


# # 다음 무비에서 홈 텍스트 가져오기
# movie = soup.find_all("a", attrs={"class":"link_gnb"})
# # print(movie)

# for daum in movie:
#     print(daum.get_text())


# for year in range(2015, 2020):
#     url = "https://search.daum.net/search?w=tot&DA=YZR&t__nil_searchbox=btn&sug=&sugo=&sq=&o=&q={}%EB%85%84+%EC%98%81%ED%99%94%EC%88%9C%EC%9C%84".format(year)
#     headers = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36"}
#     res = requests.get(url, headers=headers)
#     res.raise_for_status()
#     soup = BeautifulSoup(res.text, "lxml")
    
#     images = soup.find_all("img", attrs={"class":"thumb_img"})
    
#     for idx, image in enumerate(images):
#         image_url = image["src"]
#         if image_url.startswith("//"):
#             image_url = "https:" + image_url
            
#         # print(image_url)
#         image_res = requests.get(image_url)
#         image_res.raise_for_status()

#         with open("bigdata/img/movie_{}_{}.jpg".format(year, idx + 1), "wb") as f:
#             f.write(image_res.content)

#         # 상위 5개의 이미지까지만 다운로드
#         if idx >= 4:
#             break
        
        
# 참고 - formatting

# # 숫자 대입
# s = "현재 파이썬 버전은 %d이다." % 3
# # print(s)
# # 문자열 대입
# s = "현재 파이썬 버전은 %s이다." % "최신"
# # print(s)

number = 3
state = "최신"

# s = "현재 파이썬 버전은 %d이고 %s이다." % (number, state)
# # print(s)

# # %s 포맷 코드이나 어떤 형태의 값으로 변환 대입이 가능

# # % 출력시
# rate = "현재 과정 진행율은 %d%%입니다." % 50
# # print(rate)

# lang = "%10s" % "Python"
# # 문자열의 길이가 10자리이고 앞공간은 공백으로 비워진다.
# # print(lang)

# lang = "%-10s" % "hehe" + "end"
# # 왼쪽 정렬
# # print(lang)

# pi = "%.4f" % 3.1415966535
# # print(pi)

# format() 함수 사용
# s = "현재 파이썬 버전은 {}이고 상태는 {}이다.".format(3,"최신")
# print(s)

# s = "현재 파이썬 버전은 {}이고 상태는 {}이다.".format(number, state)
# print(s)

# # 왼쪽 정렬이 기본값, 오른쪽 정렬 "{0:>10}", 가운데 정렬 "{0:^10}"
# s = "{0:>10}".format("Python")
# print(s)
# # 공백 채우기 "{0:=<10}" =으로 공백을 채우겠다
# s = "{0:=<10}".format("Python")
# print(s)

# s = "{0:=^10}".format("Python")
# print(s)

# 중괄호를 그대로 출력하는 방법
s = "{{Python}}".format()
print(s)

# f 문자열 포매팅 (파이썬 버전 3.6 이상부터 가능)
b = f"현재 파이썬 버전은 {number}이고 상태는 {state}이다."
print(b)

# 개인적으로 당부하고 싶은 과제
# 4월말까지 자바로 여러분의 웹개발 진행 -> 토이 프로젝트