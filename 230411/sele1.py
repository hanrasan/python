# 웹브라우저 자동화 도구를 활용한 데이터 수집
# selenium -> requests, bs4 등으로 크롤링이 안되는 경우에도 대부분 사용 가능

import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

# 웹드라이버 경로 설정
driver = webdriver.Chrome('./chromedriver')

# 자동화 시작
# 요청 사이트
driver.get("https://www.python.org")
# 웹브라우저의 제목 출력
print(driver.title)

# element (요소) 찾기
# 검색 바 찾기
search_bar = driver.find_element(By.NAME, 'q')
# 검색 바 초기화
search_bar.clear()
# 검색어 입력
search_bar.send_keys("selenium")
# 검색 시작! - 검색어 입력 후 엔터 (go버튼 누르기)
search_bar.send_keys(Keys.RETURN)
# 현재 요청한 주소를 출력
print(driver.current_url)
# 대기시간 설정 5초
time.sleep(5)
# 브라우저 종료
driver.close()
