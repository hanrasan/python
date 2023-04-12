# https://auction.realestate.daum.net/v15/
# 다음부동산 - 경매 - 아파트의 첫 페이지의 내용을 추출하고
# 이미지 - 설명 - 토지 - 최저가를 추출하시오

# 출력 형태
# 1번 경매 물건 : 아파트
# 위치 : 서울 금천구 ~~
# 평수 : 토지 ~~

import time
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

url = "https://auction.realestate.daum.net/v15/"

browser = webdriver.Chrome()
browser.maximize_window()

browser.get(url)

apartment = browser.find_element(By.ID, "y_onoff1")
apartment.find_element(By.TAG_NAME, "a").click()
time.sleep(3)

res = requests.get(url)
res.raise_for_status()
soup = BeautifulSoup(res.text, "lxml")

elem = browser.find_element(By.XPATH, '//*[@id="SearchListUl"]')
titles = elem.find_elements(By.CLASS_NAME, "Title")
addrs = elem.find_elements(By.CLASS_NAME, "Address")
imgs = elem.find_elements(By.CLASS_NAME, "GoodsPhoto")

for img in imgs:
    pass




time.sleep(3)