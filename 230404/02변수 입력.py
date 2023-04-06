
# 변수를 입력할 때 자료형을 넣을 필요가 없다.
# test = 10.5
# print(type(test))


# 문자열 입력
# str = input('문자열을 입력하세요>')
# print('result :',str)


# # 숫자값 받기
# # 아래와 같이 숫자를 입력하더라도 input은 기본적으로 str형으로 받는다.
# n1 = input('n1 입력 : ')
# n2 = input('n2 입력 : ')
# # 문자를 입력받으면 오류가 발생한다.
# n1 = int(n1)
# n2 = int(n2)
# print(n1+n2)


# 세 과목의 성적을 이벼력 받아 합계와 평균을 구하시오.

n1 = int(input())
n2 = int(input())
n3 = int(input())

sum = n1 + n2 + n3
print(sum)
avg = sum/3
print(avg)