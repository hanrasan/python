# 프로젝트
# movie.daum.net
# tving 영화순위의 4개 이미지 가져오기
# 영화뉴스의 3개 뉴스의 제목과 링크 주소 가져오기
# 구글 검색에서 원하는 검색어 입력 후 나오는 결과화면의
# 스크롤을 제일 아래로 내리도록 하고 검색화면을 스크린샷 하기
# data.go.kr 로그인 과정 자동으로 진행하고 스크린샷 찍고 .exe 파일로 저장하기

# 출력 형태 -> fullproject.py
# 오늘의 뉴스
# 1. 뉴스 제목
# 링크
# 2. ~~~

import time
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

url = "https://movie.daum.net/ranking/ott"
res = requests.get(url)
res.raise_for_status()
soup = BeautifulSoup(res.text, "lxml")

heads = soup.find_all("div", attrs={"class":"head_section"})
for head in heads:
    if "티빙" == head.get_text().strip():
        img_ol = head.find_next_sibling()
        imgs = img_ol.find_all("img", attrs={"class":"img_thumb"})
        for idx, img in enumerate(imgs):
            image_url = str(img["src"])
            if image_url.startswith("//"):
                image_url = "https:" + image_url
    
            image_res = requests.get(image_url)
            image_res.raise_for_status()
    
            # with open("bigdata/230412/movie_img/movie_{}.jpg".format(idx + 1), "wb") as f:
            with open("movie_{}.jpg".format(idx + 1), "wb") as f:
                f.write(image_res.content)
        
            if idx >= 3:
                break


# 영화뉴스의 3개 뉴스의 제목과 링크 주소 가져오기

browser = webdriver.Chrome()
browser.maximize_window()
browser.get("https://movie.daum.net/contents/news")

time.sleep(2)

news = browser.find_elements(By.CLASS_NAME, "link_txt")

news_text = ""
idx = 0
for new in news:
    idx = idx + 1
    if idx > 3:
        break
    title = new.text
    link = new.get_attribute("href")
    print(title, link)
    news_text = news_text + title + " : " + link + "\n"

with open("movienews.txt", "w", encoding="utf-8") as f:
    f.write(news_text)



# 구글 검색에서 원하는 검색어 입력 후 나오는 결과화면의
# 스크롤을 제일 아래로 내리도록 하고 검색화면을 스크린샷 하기

browser = webdriver.Chrome()
browser.maximize_window()

interval = 2

url = "https://www.google.com/"
browser.get(url)

search_bar = browser.find_element(By.NAME, "q")
search_bar.clear()
search_bar.send_keys("반월당 맛집")
search_bar.send_keys(Keys.RETURN)

prev_height = browser.execute_script("return document.body.scrollHeight")

while True:
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight)")
    time.sleep(interval)

    curr_height = browser.execute_script("return document.body.scrollHeight")
    if curr_height == prev_height:
        break
    
    prev_height = curr_height

browser.get_screenshot_as_file("searchResult.png")
    
print("스크롤 완료")



# data.go.kr 로그인 과정 자동으로 진행하고 스크린샷 찍고 .exe 파일로 저장하기

browser = webdriver.Chrome()
browser.maximize_window()

browser.get("https://www.data.go.kr/")

login = browser.find_element(By.CLASS_NAME,"before")
btn_login = login.find_element(By.TAG_NAME, "a")
btn_login.click()

browser.find_element(By.ID, "mberId").send_keys("sssssssssss")
browser.find_element(By.ID, "pswrd").send_keys("aaaaaaaaaaaaa")
browser.find_element(By.CLASS_NAME, "btn-login").click()

browser.get_screenshot_as_file("loginResult.png")

browser.quit()