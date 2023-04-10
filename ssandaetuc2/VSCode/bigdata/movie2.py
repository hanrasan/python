import requests
from bs4 import BeautifulSoup

url = "https://search.daum.net/search?w=tot&DA=YZR&t__nil_searchbox=btn&sug=&sugo=&sq=&o=&q=%EC%97%AD%EB%8C%80%EA%B4%80%EA%B0%9D%EC%88%9C%EC%9C%84"
headers = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36"}
res = requests.get(url, headers=headers)
res.raise_for_status
soup = BeautifulSoup(res.text, "lxml")

# title_main = soup.find("a", attrs={"class":"tit_main"})

# print(title_main.text)


titles = soup.find_all("a", attrs={"class":"tit_main"})

for title in titles:
    print(title.text)