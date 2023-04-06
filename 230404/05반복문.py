# 반복문
# range(반복횟수)
# for i in range(5):
#     print(i)
# print()
# for i in range(5,10):
#     print(i)
# print()
# for i in range(0,10,2):
#     print(i)


# range() 역방향
# for i in range(5,-1,-1):
#     print(i)
# print()
# for i in reversed(range(5)):
#     print(i)


# 입력받은 구구단 출력
# 1부터 입력받은 수중에 3의 배수만 출력

# num = int(input("구구단 단수 > "))
# for i in range(1,10):
#     print("3 x",i,"=",i*num)

# num = int(input("범위지정 > "))
# for i in range(1,num+1):
#     if i%3==0:
#         print(i)


# 구구단 전체 출력
# 구구단 전체 역순 출력
# 별찍기
# *
# **
# ***
# ****
# *****
#
# *****
# ****
# ***
# **
# *

#    *
#   ***
#  *****
# *******

# for i in range(2,10):
#     print(i,"단")
#     for j in range(1,10):
#         print(i,"x",j,"=",i*j)
#     print()

# for i in reversed(range(2,10)):
#     print(i,"단")
#     for j in range(1,10):
#         print(i,"x",j,"=",i*j)
#     print()

# for i in range(9,1,-1):
#     print("{} 단".format(i))
#     for j in range(9,0,-1):
#         print(i,"x",j,"=",i*j)
#     print()

# for i in range(1,6):
#     print("*"*i)

# for i in range(5,0,-1):
#     print("*"*i)

# h=int(input("h > "))
# for row in range(0,h):
#     for star in range(0,row+1):
#         print("*",end="")
#     print()

#    *
#   ***
#  *****
# *******

# i(행)    j(곻백)   k(별)
# 0        0-2      0-0
# 1        0-1      0-2
# 2        0-0      0-4
# 3        x        0-6

# h = int(input("h > "))
# for i in range(0,h):
#     # 공백(높이의 영향을 받는다)
#     for j in range(0,(h-1)-i):
#         print(" ",end="")
#     # 별
#     for k in range(0,i*2+1):
#         print("*",end="")
#     print()


# 무한루프~

# import time
#
# # 5초 후의 값이 num에 저장
# num = time.time() + 5
# cnt = 0
# while True:
#     print("*",end="")
#     if time.time() > num:
#         break
#     cnt += 1
# print("총 반복된 *의 개수는 {}개 입니다.".format(cnt))


# continue
# 1부터 10가지의 수 중에 3의 배수만 제외하고 출력

for i in range(1,11):
    if i%3==0:
        continue
    print(i)