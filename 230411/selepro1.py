# q-net.or.kr -> 검색어 정보처리기사 클릭 -> 자동화(selenium)
# 결과 화면내에서 2023년 정기 기사 2회의 데이터만 출력

import requests
import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

browser = webdriver.Chrome("./chromedriver")
browser.maximize_window()

browser.get("https://www.q-net.or.kr/man001.do?&gSite=Q&gId=")
# print(browser.title)

searchbar = browser.find_element(By.ID, "searchQuery")
searchbar.clear()
searchbar.send_keys("정보처리기사")
searchbar.send_keys(Keys.RETURN)

url = browser.current_url
# print(url)

res = requests.get(url)
res.raise_for_status()
soup = BeautifulSoup(res.text, "lxml")

# title = "       구분	                    필기원서접수(인터넷)(휴일제외)	                            필기시험	필기합격(예정자)발표	실기원서접수(휴일제외)	        실기시험	최종합격자 발표일"
# print(title)

# data_rows = soup.find("table").find("tbody").find_all("tr")
# idx = 0
# for row in data_rows:
#     columns = row.find_all("td")
#     data = [column.get_text().strip().replace('\r','').replace('\n','').replace('\t','') for column in columns]
#     if idx == 1:
#         print(data)
#     idx = idx + 1


# ---------------- chatGPT --------------------------------------------------------------------------------------------
data_rows = soup.find("table").find_all("tr")
idx = 0
for row in data_rows:
    columns = row.find_all("td")
    heads = row.find_all("th")
    finalH = [head.get_text().strip() for head in heads]
    if idx == 2:
        finalC = [column.get_text().strip().replace('\r','').replace('\n','').replace('\t','') for column in columns]
        for h in zip(finalH, finalC):
            print(h)
        print()
    idx = idx + 1

# time.sleep(5)