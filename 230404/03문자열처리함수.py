
# format()
# format 형식 혹은 서식이라는 뜻으로, {}을 서식으로 인식하여 그 안에 값을 넣어준다.
# str = "TEST {}".format(10)
# str1 = "TEST {}".format('asdf')
# print(str)
# print(type(str))
# print(str1)


# {}안에 숫자를 넣거나 변수를 삽입하여 순서를 변경할 수 있다.
# print("{} {} {}".format(1, "문자열", True))
# print("{1} {0} {2}".format(1,2,3))
# charge = 5000
# print("{a} {charge}".format(charge = charge, a = 123))


# format() IndexError 예외
# format_a = "{} {}".format(1,2,3,4,5)
# print(format_a)
# format_b = "{} {} {}".format(1,2)


# --------------------------
# 미니 문제
# --------------------------
# 두 개의 값을 입력 받아서 다음 실행 결과가 나오도록 하시오.

# 사과 1개당 가격 : 1000
# 사과 개수 : 5

# 사과 1개당 가격은 {} 원이고, 총사과판매액수는 {}입니다.
# print("사과 1개당 가격은 {} 원이고, 총사과판매액수는 {}입니다.".format(1000,5*1000))


# str = "Hello World"
# print(str.upper())
# print(str.lower())
# print(str.capitalize())
# print(str.title())
# print(" hello ".strip())
# print(str.replace('H','h'))
# print(str.find('W'))
#
# print(str.startswith("H"))
# print("o" in str)
# print("x" in str)

