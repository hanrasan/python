# # 기본적으로 '',"" 은 str로 인식한다.
# print('hello world')
# print("hello world")
# # 쉼표는 자동으로 띄어쓰기를 해준다.
# print("hello","world","jung")
#
# # int, float 등의 자료형을 자동으로 구분해준다.
# # 데이터를 먼저 저장하고 자료형을 처리해준다.
# print(type(123))
# print(type(123.123))
# print(type('hello world'))
# print(type("hello world"))
#
# # 연산자
# # + - * / % **(제곱연산자) //
# print(2**3)
# print(3**3)
# # // 은 나눗셈을 실행하고 소수점은 내림처리한다.
# # 자바와의 차이점은 자료형에따라 결과값도 달라지지만,
# # 파이썬에서는 자동으로 자료형을 바꾸어준다.
# print('3//2 =',3//2)
# print('3/2 =',3/2)


# 3 문자열 처리
# 문자열 다음에 배열처럼 []를 하여 인덱스의 순번에 있는 문자를 추출가능하다.
# 왼쪽에서 오른쪽의 인덱스와 오른쪽에서 왼쪽으로의 인덱스가 따로 존재한다.
# 왼쪽에서 오른쪽 : 0 1 2 3
# 오른쪽에서 왼쪽 : -1 -2 -3 -4
# print("안녕하세요")
# print("안녕하세요"[0])
# print("안녕하세요"[1])
# print("안녕하세요"[2])
# print("안녕하세요"[3])
# print("안녕하세요"[4])
# print("")
# print("안녕하세요"[-1])
# print("안녕하세요"[-2])
# print("안녕하세요"[-3])
# print("안녕하세요"[-4])
# print("안녕하세요"[-5])


# 문자열 처리 - 슬라이싱
# print("안녕하세요"[0:3])
# print("안녕하세요"[0:0])
# print("안녕하세요"[0:1])
# print("안녕하세요"[0:2])
# print("안녕하세요"[1:1])
# print("안녕하세요"[1:2])
# print("안녕하세요"[2:4])
#
# print("안녕하세요"[2:-1])


# 문자열 길이
# 띄어쓰기도 하나의 문자로 인식한다.
# print(type(' '))
# print(len('안녕하세요'))
# print(len('안녕 하세요'))

