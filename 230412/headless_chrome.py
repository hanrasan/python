# headless -> 창을 띄우지 않음

from selenium import webdriver
from selenium.webdriver.common.by import By

option = webdriver.ChromeOptions()
option.headless = True
option.add_argument("window-size=1920x1080")
option.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36")

browser = webdriver.Chrome(options=option)
# browser = webdriver.Chrome()
browser.maximize_window()

url = "https://www.whatismybrowser.com/detect/what-is-my-user-agent/"
browser.get(url)

de_value = browser.find_element(By.ID, "detected_value")
print(de_value)
browser.get_screenshot_as_file("useragent.png")
browser.quit()

# .py 파일을 실행 파일(.exe)로 생성 -> pyinstaller
# -F : 하나의 파일로 생성 -w : 콘솔 창 안보이게 함
# pyinstaller -F -w headless_chrome.py