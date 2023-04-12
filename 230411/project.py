# 나만의 비서 만들기 프로젝트

import requests
from bs4 import BeautifulSoup

# ----------------------------------------------------------------------------
# 다음 경제 뉴스 상위 5개 제목 + 링크
# 출력 형식
# 1. 뉴스 제목
#    링크 주소
# 2. 뉴스 제목
#    링크 주소

# 다음 날씨
# 출력 형식
# 현재 온도는 {} 도입니다.
# 오늘 온도는 어제보다 ~~
# 체감 온도는 몇 도이다.

# 해커스영어 사이트에서 매일 영어회화학습에서 한글 지문, 영어 지문 추출
# 출력 형식
# 한글지문 - 오늘의 표현(검은거만) 제외
# 영어지문 - 위와 동일
# ----------------------------------------------------------------------------

url_news_economic = "https://news.daum.net/economic#1"
url_weather = "https://search.daum.net/search?w=tot&DA=Z8T&q=%EB%8C%80%EA%B5%AC%20%EC%98%A4%EB%8A%98%20%EB%82%A0%EC%94%A8&rtmaxcoll=Z8T"


def create_soup(url):
    res = requests.get(url)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "lxml")
    return soup


soup = create_soup(url_news_economic)
news = soup.find_all("a", attrs={"class": "link_txt"})

for idx, new in enumerate(news):
    title = new.get_text()
    link = new["href"]
    print(f"{idx + 1}. {title}\n{link}\n")
    if idx >= 4:
        break

soup = create_soup(url_weather)
weather = soup.find("strong", attrs={"class": "txt_temp"})
ondo = weather.get_text()
print(f"현재 온도는 {ondo} 입니다.")

weather = soup.find("p", attrs={"class": "txt_desc"})
chegam = weather.get_text()
print(chegam)

# --------------------------------------------------------------

url = "https://www.hackers.co.kr/?c=s_lec/lec_study/lec_I_others_english&keywd=haceng_submain_lnb_lec_I_others_english&logger_kw=haceng_submain_lnb_lec_I_others_english"
soup = create_soup(url)
today_english = soup.find_all("div", attrs={"class": "conv_in"})

# for idx, te in enumerate(today_english):
#     print(te.get_text())

for te in today_english:
    print(te.get_text())

# ----------------------------------------------------------------

