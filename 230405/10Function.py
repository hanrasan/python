# 함수의 기본 구조
# def print_3_times():
#     print("안녕하세요")
#     print("안녕하세요")
#     print("안녕하세요")
#
# print_3_times()


# 매개변수

# def print_n_times(value,n):
#     for i in range(n):
#         print(value)
#
# print_n_times("HELLO~",5)


# 가변 매개변수

# def print_n_times(*value):
#     # 튜플 형태로 가변인자를 받음
#     print(value)
#     for i in value:
#         print(i)
#
# print_n_times("HELLO","my","name","is","Hong")


# 매개변수 디폴트 값

# def print_n_times(value,n=10):
#     for i in range(n):
#         print(value)
#
# print_n_times("HELLO~")


# 키워드 매개변수

# def print_n_times(*value,n):
#     for i in range(n):
#         for data in value:
#             print(data,end="")
#         print()
#
# print_n_times("HELLO~","my","name","is","Hong",n=5)


# 매개변수 지정

# def test(a, b, c):
#     print(a , b , c)
#
# test(10,20,30)
# test(b=5, c=3, a= 7)


# 리턴값 확인

# def test():
#     return (100,200)
#
# test()
# print(test())
# print(type(test()))


# 팩토리얼 코드 1! 2! 3! 4!

# def factorial(n):
#     output = 1
#     for i in range(1, n+1):
#         output *= i
#     return output
#
# print("3!", factorial(3))
#
# def factorial2(n):
#     if n==0:
#         return 1
#     else:
#         return n*factorial2(n-1)
#
# print("3!",factorial2(3))


# 함수를 인자로 받는 함수

# def call_10_times(func):
#     for i in range(10):
#         func()
#
# def print_hello():
#     print("HELLO WORLD!")
#
# call_10_times(print_hello)


# map() 함수 사용하기

# # 함수를 선언
# def power(item):
#     return item*item
#
# def under_3(item):
#     return item < 3
#
# # 변수를 선언
# list_input_a = [1,2,3,4,5]
#
# # # map() 함수 사용하기
# output_a = map(power, list_input_a)
# print(output_a)
# print(list(output_a))
#
# output_b = filter(under_3, list_input_a)
# print(output_b)
# print(list(output_b))


# 문제1.

# def multiply_by_2(item):
#     return item*2
#
# def even_numbers(item):
#     return item % 2 == 0
#
# list_input = [1,2,3,4,5]
#
# output_a = list(map(multiply_by_2, list_input))
# print(output_a)
#
# output_b = list(filter(even_numbers, list_input))
# print(output_b)


# 람다식

# 함수를 선언
# def power(item):
#     return item*item
# power = lambda item: item * item
#
# print(power(4))

# def under_3(item):
#     return item < 3
# under_3 = lambda item: item < 3
#
# print(under_3(2))


# under_3 = lambda item: item < 3
#
# print(list(filter(under_3,[1,2,3,4,5])))
# # 인라인 람다
# print(list(filter(lambda item: item < 3,[1,2,3,4,5])))


# numbers = [1,2,3,4,5]
# result = [(lambda x:x*2)(x) for x in numbers]
# print(result)
#
# def test(x):
#     return x*2
# result2 = [test(x) for x in numbers]
# print(result2)


