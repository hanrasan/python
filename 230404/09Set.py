# Set 생성
# set1 = {10,20,30,40,50}
# set2 = {20,70,30,44,90}
# print(set1)
#
# for data in set1:
#     print(data)


# # 교집합
# result1 = set1.intersection(set2)
# print(result1)
#
# # 합집합
# result2 = set1.union(set2)
# print(result2)
#
# # 차집합
# result3 = set1.difference(set2)
# print(result3)


# 컬렉션 -> Set 변환함수 set()
# list_a = [10,10,20,20,30,40,50]
# print(list_a)
# # 중복제거
# print(set(list_a))
# # set -> list
# print(list(set(list_a)))
# print(sorted(list(set(list_a))))
# print(sorted(list(set(list_a)),reverse=True))


# 로또번호를 생성합니다.
# 난수형성된 파이썬 모듈을 찾아보시고 진행합니다.
# set을 통해서 난수값을 받아 오름차순 정렬해서 6자리 로또번호를 출력해보세요.

# import random
#
# lotto = set()
#
# while len(lotto) < 6:
#     lotto.add(random.randint(1,45))
# print(sorted(lotto))

import random
import time

# random_int = random.randint(1,45)
lotto = set()
print(len(lotto))
while len(lotto) < 6:
    # print(random.randint(1,45))
    # time.sleep(0.5)
    lotto.add(random.randint(1,45))
lotto_list = sorted(list(lotto))
print(lotto_list)