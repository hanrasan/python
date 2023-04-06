
# 파일 입출력

# 파일 입출력은 컴퓨터 파일에 데이터를 쓰거나 읽는 것을 말합니다.
# 파이썬에서는 open() 함수를 사용하여 파일 객체를 생성하고, 이 객체를 통해 파일을 읽거나 쓸 수 있습니다.
# 파일을 읽는 경우 read() 메서드를 사용하고, 파일을 쓰는 경우 write() 메서드를 사용합니다.
# 파일을 다 사용한 후에는 close() 메서드를 사용하여 파일을 닫아주어야 합니다.
# 또한, with 문을 사용하면 파일을 자동으로 닫아주므로 코드가 간결해집니다.


# 파일 쓰기

# 문법 open('파일 경로', '파일 모드')
# 파일모드
# r : 읽기
# w : 쓰기
# a : 추가
# x : 배타적 생성 모드 (파일이 이미 있을때 오류를 발생 시키는 모드)

# file = open("file1.txt", 'w')
# file.write("MY NAME IS")
# file.close()

# file = open("file1.txt", 'a')
# file.write("\nTEST TEST TEST\n")
# file.close()

# file = open("file1.txt", 'r')
# str = file.readlines()
# print(str)
# file.close()


# file = None
# try:
#     file = open("file2.txt", "x")
#     file.write("TEST")
# except FileExistsError as e:
#     print(e)
# finally:
#     if file is not None:
#         file.close()


# with 예약어 - file.close() 자동 처리

# try:
#     with open("file1.txt",'x') as file:
#         file.write("MY NAME IS ")
# except FileExistsError as e:
#     print(e)


# 콘솔창에서 처리하는 메모장을 만들어 봅시다.

# def menu() 메뉴함수
# 1. 파일쓰기 - open, input ... 파일 이름 받기, 파일 생성, 내용 쓰기
# 2. 파일수정 - 덮어쓰기
# 3. 파일삭제 - 내용제거 ''
# 4. 파일종료 - 프로그램 종료

t = ''
def menu():
    print("1. 파일쓰기")
    print("2. 파일수정")
    print("3. 파일삭제")
    print("4. 파일종료")
    try:
        num = int(input("[메뉴번호] > "))
    except ValueError as e:
        print("옳바른 번호를 입력해주세요.")
        print("EX) 1")
    finally:
        menu()

while t != 'n':
    t = input("Text File 생성\n[y/n = Exit] > ")
    print()
    if t == 'y':
        menu()