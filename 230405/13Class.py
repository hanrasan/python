
# 클래스

# 클래스는 객체 지향 프로그래밍에서 사용되는 데이터 타입으로, 속성과 메서드를 포함합니다.
# 클래스를 정의하고 인스턴스를 생성하여 사용할 수 있으며, 인스턴스의 속성과 메서드에 접근하여 값을 설정하고 호출할 수 있습니다.
# 클래스의 상속, 다형성, 캡슐화 등의 개념도 중요합니다.


# class Person:
#     def __init__(self,name,age,addr):
#         self.name = name
#         self.age = age
#         self.addr = addr
#     def getName(self):
#         return self.name
#     def getAge(self):
#         return self.age
#     def getAddr(self):
#         return self.addr
#     def toString(self):
#         return self.name + "|" + self.age + "|" + self.addr
#     def __str__(self):
#         return self.name + "|" + self.age + "|" + self.addr
#
# list = [Person('hong','55','Daegu'),Person('lee','66','Ulsan'),Person('kim','11','Incheon')]
# for item in list:
#     print(item.toString())
#
# print(list[0].name)
# hong = Person('hong','55','Daegu')
# print(hong.name)
# print(hong.age)
# print(hong.addr)
# print(hong.getName())
# print(hong.getAge())
# print(hong.getAddr())
# print(hong.toString())


# 클래스 상속


# class 변수 (자바 static 변수와 유사)

# class MyClass:
#     # class 변수(모든 객체가 공유하는 num)
#     num1 = 0
#
#     def __init__(self,num2):
#         # self.num2 인스턴스 변수(해당 객체에 저장되어 있는 num)
#         self.num2 = num2
#
#     @classmethod
#     def inc_class_var(cls):
#         cls.num1 += 1
#
#     def __str__(self):
#         return "인스턴스 num2 : " + str(self.num2) + " 클래스 num1 : " + str(self.num1)
#
# ob1 = MyClass(10)
# ob1.inc_class_var()
# ob2 = MyClass(20)
# ob2.inc_class_var()
#
# print(ob1)
# print(ob2)


# 상속

class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def sound(self):
        print(self.name,"가 소리를 냅니다.")

class Dog(Animal):
    def __init__(self, name, species):
        super().__init__(name,species)
    def sound(self):
        print(self.name,"가 멍멍 소리를 냅니다.")

class Cat(Animal):
    def __init__(self, name, species):
        super().__init__(name,species)
    def sound(self):
        print(self.name,"가 야옹 소리를 냅니다.")

ob1 = Dog('바둑이','진돗개')
ob2 = Cat('야옹이','고양이')
ob1.sound()
ob2.sound()