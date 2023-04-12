# API 요청
import requests

url = "https://infuser.odcloud.kr/oas/docs?namespace=3074462/v1"
params = {"servicekey":""}

response = requests.get(url, params=params)
print(response.content)

# 네이버 개발자 센터 / 카카오 개발자 센터

# 자바랑 친해지기
# 4월 17일 옆 사람과 자바로 게임 만들어 서로 바꿔서 해보기