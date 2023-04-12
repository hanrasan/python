# 화면 스크롤 제어

import time
from selenium import webdriver

browser = webdriver.Chrome()
browser.maximize_window()

# 페이지 이동 주소
url = "https://play.google.com/store/movies?hl=ko"
browser.get(url)

# 해상도 높이로 스크롤 내리기
# browser.execute_script("window.scrollTo(0, 1080)")

# 화면의 가장 아래로 스크롤 내리기
# browser.execute_script("window.scrollTo(0, document.body.scrollHeight)")

# 2초에 한 번씩 스크롤을 내림
interval = 2

# 2초 스크롤 전 현재 문서 높이를 가져와서 저장
prev_height = browser.execute_script("return document.body.scrollHeight")

# 반복문 수행
while True:
    # 스크롤을 가장 아래로 내림
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight)")
    # 페이지 로딩 대기
    time.sleep(interval)
    
    # 스크롤 진행 후 현재 문서 높이를 가져와서 저장
    curr_height = browser.execute_script("return document.body.scrollHeight")
    if curr_height == prev_height:
        break
    
    prev_height = curr_height
    
print("스크롤 완료")



