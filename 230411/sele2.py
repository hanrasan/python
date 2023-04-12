import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


browser = webdriver.Chrome("./chromedriver")

# 브라우저 창 크기 제어
browser.maximize_window()

# 네이버로 이동
browser.get("https://www.naver.com")
print(browser.title)

# 로그인 버튼 클릭
elem = browser.find_element(By.CLASS_NAME, "link_login")
elem.click()

# id / pw 입력
browser.find_element(By.ID, "id").send_keys("ssssssssss")
browser.find_element(By.ID, "pw").send_keys("aaaaaaaaaa")
browser.find_element(By.ID, "log.login").click()

# id 를 만약에 새로 입력한다면
browser.find_element(By.ID, "id").clear()
browser.find_element(By.ID, "id").send_keys("haha")
browser.find_element(By.ID, "pw").clear()
browser.find_element(By.ID, "pw").send_keys("hehe")
time.sleep(5)

# html 정보 출력
print(browser.page_source)

# 브라우저 종료
# 현재 탭만 종료
# browser.close()
# 전체 브라우저 종료
browser.quit()