# dictionary 기본
# dic_a = {
#     "name":"홍길동",
#     "age":"55",
#     "job":"돚거",
#     "hobby":['감옥','탈출'],
#     "certification":['정문처리기사','락픽활용능력1급','STILLD']
# }
# print(dic_a)
# print(dic_a['name'])
# print(dic_a['age'])
# print(dic_a['job'])
# print(dic_a['hobby'])
# print(dic_a['certification'])
# print(dic_a['hobby'][0])
# print(dic_a['hobby'][1])
# print(dic_a['certification'][0])
# print(dic_a['certification'][1])
# print(dic_a['certification'][2])
#
# dic_a['addr'] = "돚거 광역시 어쩌구"
# print(dic_a)
# del dic_a['job']
# print(dic_a)
# print(dic_a.keys())
# print(dic_a.get('name'))
#
# for key in dic_a:
#     print(key,":",dic_a[key])
#
# for value in dic_a.values():
#     print(value)


# # 깊은 복사 & 얕은 복사
# list_a = [10,20,30]
# # 얕은 복사 (주소 복사)
# list_b = list_a
# # 깊은 복사 (공간 따로 생성 + 값 복사)
# list_c = list_a.copy()
#
# list_a[1] = 100
# print(list_a)
# print(list_b)
# print(list_c)


# 학생이름:점수 로 구성되어 있는 딕셔너리를 보고 평균점수를 구해보세요.
# students = {'Tom':90,'Jane':85,'Mike':95,'John':80,'Anna':92}
# print(sum(students.values())/len(students))


# --- chatGPT Code ---
# students = {'Tom':90,'Jane':85,'Mike':95,'John':80,'Anna':92}
# average = sum(students.values()) / len(students.values())
# print(f"The average score is {average:.2f}")

# === 강사님 코드 ===
# total = sum(students.values())
# print(total//len(students.values()))


