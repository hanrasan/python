import traceback

# 예외처리

# 예외 처리는 예기치 않은 상황이 발생할 때 프로그램이 종료되는 것을 막기 위한 방법입니다.
# 이를 위해 try-except 문을 사용하며, try 블록 안에서 예외가 발생하면 except 블록에서 예외를 처리합니다.
# 예외 처리를 사용하면 프로그램이 예외 상황에서도 정상적으로 동작할 수 있습니다.

# SyntaxError: unterminated string literal
# print("예외)

# ZeroDivisionError: division by zero
# print(10/0)

# NameError: name 'n' is not defined
# input('정수입력 >')
# print(1+n)

# TypeError: unsupported operand type(s) for +: 'int' and 'str'
# n = input('정수입력 >')
# print(1+n)

# print("절차지향이므로")
# print(10/0)
# print("아래는 나오지 않는다.")

# try:
#     print(10/0)
# except:
#     print("예외발생!")
#
# print("hello")


# 예외 객체
# try:
#     print(10/0)
# except Exception as e:
#     print(e)
#     traceback.print_exc()
#
# print("hello")


# try - except - else

try:
    print("try Area")
    # print("ERROR", 10/0)
except Exception as e:
    print("try-exception:",e)
else:
    print("else Area:","NO ERROR")
finally:
    print("finally Area:","Absolutely")

print("HI")


# try - except - finally