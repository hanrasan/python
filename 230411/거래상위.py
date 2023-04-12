import csv
import requests
from bs4 import BeautifulSoup

url = "https://finance.naver.com/sise/sise_quant.naver"
filename = "거래상위.csv"
f = open(filename, "w", encoding="utf-8-sig", newline="")
writer = csv.writer(f)

title = "N	종목명	현재가	전일비	등락률	거래량	거래대금	매수호가	매도호가	시가총액	PER	ROE"
print(type(title))
writer.writerow(title)


res = requests.get(url)
res.raise_for_status()
soup = BeautifulSoup(res.text, "lxml")

data_rows = soup.find("table", attrs={"class":"type_2"}).find_all("tr")
for row in data_rows:
    # <td> ~~ </td>
    columns = row.find_all("td")
    # 의미 없는 데이터는 skip
    if len(columns) <= 1:
        continue
    data = [column.get_text().strip() for column in columns]
    # print(data)
    writer.writerow(data)