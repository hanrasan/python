# print(True)
# print(False)
# print(10 == 100)
# print(10 != 100)
#
# x=25
# print(10<x<30)


# # 미쳐버린 파이썬 성능
# print("가방"=="가방")
# print("가방"=="오렌지")
# # ㄱ 보다 ㅇ 가 나중에 나와서, 아마도 아스키코드값을 받는게 아닐까?
# print("가방">="오렌지")
# print("가방"<"오렌지")


# 논리연산자 and(&&), or(||), not(!)
# print(not True)
# print(not False)
#
# print(True and True)
# print(True and False)
# print(False and False)
#
# n1 = int(input("n1 >"))
# n2 = int(input("n2 >"))
# print(n1>n2 and n1>20)


# if
# 파이썬에서는 들여쓰기를 조심해야한다.
# if 조건식 :
# if False :
#     print("참입니다. -1")
#     print("참입니다. -2")
# print("종료")


# 짝, 홀수 ( %, 끝한자리, in )
# num = input("num>")
# ln = int(num[-1])
# print(ln)
#
# if ln==2 or ln==4 or ln==6 or ln==8 or ln==0:
#     print("짝수")
#
# if str(ln) in "24680":
#     print("짝수")
#
# if ln%2==0:
#     print("짝수")


# 양, 음수
# num = int(input("num >"))
# if num>0:
#     print("양수")
# else:
#     print("음수")


# 입력한 데이터가 3의 배수인 경우 출력
# num = int(input("num >"))
# if num%3==0:
#     print("3의 배수이다.")
# else:
#     print("3의 배수가 아니다.")

# 절대값을 구하는 프로그램을 작성하시오
# num = int(input("num >"))
# if num>=0:
#     print(num)
# else:
#     print(-num)

# 세수를 입력받아 큰수를 출력하시오
# n1 = int(input("n1 >"))
# n2 = int(input("n2 >"))
# n3 = int(input("n3 >"))


# # 모듈 사용해보기
#
# import datetime
#
# now =  datetime.datetime.now();
# print (now)
#
# # 출력합니다.
# print(now.year, "년")
# print(now.month, "월")
# print(now.day, "일")
# print(now.hour, "시")
# print(now.minute, "분")
# print(now.second, "초")
#
# # 오후/오전
# if now.hour < 12:
#     print("오전")
# elif now.hour > 18:
#     print("오후")
# else:
#     print("저녁")
#
# # 계절구분
# if 3 <= now.month<=6:
#     print("{}월은 봄입니다.".format(now.month))
#
#
# # 주의
# if True:
#     pass
# else:
#     print("TEST")



# # ----------------------------------------------------
# // [문제풀기]
# # ----------------------------------------------------
# //입력한 데이터가 3의 배수인 경우 출력하시오
# //
# //절대값을 구하는 프로그램을 작성하시오
# //
# //수를 입력 받아 짝,홀수를 구분하여 출력하시오
# //
# //두수를 입력 받아 큰 수를 출력하시오
# //
# //세수를 입력받아 큰수를 출력하시오
# //
# //두수를 입력 받아 큰 수가 짝수이면 출력하시오
# //
# //두수를 입력 받아 합이 짝수이고 3의 배수인 수를 출력하시오


# # ----------------------------------------------------
# // [문제풀기]
# # ----------------------------------------------------
#
# //세 과목의 성적을 입력 받아 합계와 평균을 구하고 평균이 90점이상이면 "A"
# //80점이상이면 "B" , 70점이상이면 "C", 60점이상이면 "D" 60점 미만이면 "F"를 출력하시오
# //
# //
# //유원지에서 말을 태워주는데 처음 30분의 기본요금은 1인당 3000원이다
# //이후에는 10분당 500원씩의 추가 요금을 받는다. 말을 탄 시간을 입력 받아서
# //전체 금액을 계산하는 프로그램을 작성하여라
# //
# //배달 도시락을 주문하는데 10개까지는 개당 2500이고 10개를 초과하는 양에 대해서는 개당
# //2400원이다. 배달 도시락의 개수를 입력 받아서 금액을 계산하는 프로그램을 작성하라
# //
# //디스켓 1통에 5000원한다. 그런데 한번에 10통이상을 사면
# //전체 금액의 10%를 할인하여준다 그리고 100통 이상을 사면
# //전체 금액의 12%를 할인하여 준다. X통의 디스켓을 사려면 얼마가 있어야 하는가


n1 = int(input("성적 입력 >"))
n2 = int(input("성적 입력 >"))
n3 = int(input("성적 입력 >"))

sum = n1 + n2 + n3
avg = sum / 3

if avg >= 90:
    print("A")
elif avg >= 80:
    print("B")
elif avg >= 70:
    print("C")
elif avg >= 60:
    print("D")
else:
    print("F")