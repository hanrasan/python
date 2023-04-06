# # 1. List 기본
# list_a = [1,2,3,4,'c','asdf',True,False]
# print(list_a)
#
# # 2. 요소에 접근
# print(list_a[0])
# print(list_a[1])
# print(list_a[2])
# print(list_a[3])
# print(list_a[4])
# print(list_a[5])
# print(list_a[6])
# print(list_a[7])
# print()
# print(list_a[-1])
# print(list_a[-2])
# print(list_a[-3])
# print()
#
# # 3. 요소값 변경
# list_a[0] = 'hong gil dong'
# print(list_a[0])
#
# # 4. 리스트 요소 이중접근
# print(list_a[5][1])

# list_b = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# print(list_b)
# print(list_b[0])
# print(list_b[1])
# print(list_b[2])
# print(list_b[0][0])
# print(list_b[1][0])
# print(list_b[2][0])

# 5. 반복문과 List

# for i in range(10):
#     print(i)
#
# for i in [1,2,5,4,3]:
#     print(i)

# 반복문과 list를 이용하여
# 출력하고자하는 구구단수를 3개를 입력받아(ex 3,5,7)
# 해당 단수의 구구단을 출력해보세요. (list와 for문을 이용합니다.)

# n1 = int(input("원하는 단수를 입력하세요. (1/3) > "))
# n2 = int(input("원하는 단수를 입력하세요. (2/3) > "))
# n3 = int(input("원하는 단수를 입력하세요. (3/3) > "))
# print()
#
# numArr = [n1, n2, n3]
#
# for i in numArr:
#     print(f'{i}단')
#     for j in range(1,10):
#         print(f'{i} X {j} = {i*j}')
#     print()

# ---chatGPT Code---
# for i in range(3):
#     n = int(input(f"원하는 단수를 입력하세요. ({i+1}/3) > "))
#     print(f"{n}단")
#     for j in range(1, 10):
#         print(f"{n} x {j} = {n*j}")
#     print()

# =======강사님 코드========
# list_dan = [int(input('단수 입력 >')),int(input('단수 입력 >')),int(input('단수 입력 >'))]
# for dan in list_dan:
#     for i in range(1,10):
#         print(f'{dan} X {i} = {dan*i}')
#     print()


# 6. 기존 list에 값 추가

# list_c = [10,20,30]
# print(list_c)
# # 파이썬에서는 안되는 코드
# # list_c[3] = 40
# # print(list_c)
# list_c.append(40)
# print(list_c)
# list_c.append('answer')
# print(list_c)
# list_c.insert(0,123)
# print(list_c)
# list_c.extend([100,200,300])
# print(list_c)


# 7. list 요소 제거

# list_d = [10,20,30,40,50,60,70,60,60,60,70]
# print(list_d)
# # 인덱스 요소 제거
# del list_d[2]
# print(list_d)
# # del list_d[2]
# # print(list_d)
# # 마지막 요소 제거
# num = list_d.pop()
# print(list_d, num)
#
# # 슬라이싱 범뮈 요소 제거
# del list_d[1:4]
# print(list_d)
#
# list_d.remove(60)
# print(list_d)
#
# # list 안의 중복된 요소 제거
# print(set(list_d))


# 8. 리스트 내부 값 탐색

# list_e = [10,20,30,40,50]
# print(15 in list_e)
# print(20 in list_e)
# print(15 not in list_e)
# print(20 not in list_e)
#
#
# # 0. 리스트 길이
# print(len(list_e))


# -1을 입력하기 전까지 점수를 입력받아 list에 저장합니다.
# 저장된 리스트 안에서 최대값, 최소값, 평균, 총합을 구하고 출력하세요.

# i = 0
# num = []
# sumNum = 0
# while i != -1:
#     i = int(input("점수 입력 (종료 : -1) >"))
#     if i == -1:
#         break
#     else:
#         num.append(i)
#
# num.sort()
# print(num)
# min = num[0]
# max = num[len(num)-1]
#
# for i in num:
#     sumNum += i
#
# avg = sumNum / len(num)
#
# print("최대값: {}, 최소값: {}, 평균: {}, 총합: {}".format(max,min,avg,sumNum))


# ----- chatGPT Code -----
# num = []
# sumNum = 0
# length = 0
#
# while True:
#     i = int(input("점수 입력 (종료 : -1) >"))
#     if i == -1:
#         break
#     num.append(i)
#     length += 1
#
# num.sort()
# minNum = min(num)
# maxNum = max(num)
#
# for i in num:
#     sumNum += i
#
# avg = sumNum / length
#
# print("최대값: {}, 최소값: {}, 평균: {}, 총합: {}".format(maxNum, minNum, avg, sumNum))


# === 강사님 코드 ===
# list = []
# while True:
#     data = int(input("입력[종료:-1] >"))
#     if data == -1:
#         break
#     list.append(data)
#
# print(list)
# # max = list[0]
# # min = list[0]
# #
# # for i in list:
# #     print(i)
# #     if max < i:
# #         max = i
# #     if min > i:
# #         min = i
# # print("max:",max)
# # print("min:",min)
# print("max:",max(list))
# print("min:",min(list))
# print("sum:",sum(list))
# print("avg:",sum(list)/len(list))