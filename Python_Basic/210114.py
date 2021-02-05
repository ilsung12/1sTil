# 210114
# 파이썬 클래스 상세 이해
# Self, 클래스, 인스턴스 변수

# 클래스, 인스턴스 차이 중요
# 클래스를 인스턴스화 시켜서 사용
# 네임스페이스 : 객체를 인스턴스화 할 때 저장된 공간 *독립적 공간
# 클래스 변수 : 직접 사용가능, 객체보다 먼저 생성된다.
# 인스턴스 변수 : 객체마다 별도로 존재, 인스턴스 생성후 사용


# 선언
# class 클래스명:
#     함수
#     함수

# 인스턴스
# 인스턴스


print('예제1 클래스의 구성--------------------------------------------------------------------------------')
# 예제 1


class UserInfo:  # 클래스 첫글자는 대문자가 원칙!,단어와 단어가 만날때도 대문자
    # 구성 : 속성 + 메소드

    # 속성 : 키 나이 전화번호 등
    # 메소드 : 동사를 구현
    def __init__(self, name):  # ****클래스를 최초 초기화하는 함수 필수!
        self.name = name

    def user_info_p(self):
        print("Name : ", self.name)


user1 = UserInfo("Kim")
user1.user_info_p()
user2 = UserInfo("Park")
user2.user_info_p()

print(id(user1))
print(id(user2))
print(user1.__dict__)
print(user2.__dict__)

# 결과===>
#Name :  Kim
#Name :  Park
# 2557369579000
# 2557369579112
#{'name': 'Kim'}
#{'name': 'Park'}

print('예제2 self의 이해--------------------------------------------------------------------------------')
# 예제 2
# self의 이해


class SelfTest:
    def funtion1():
        print('function1 called!')

    def funtion2(Self):
        print(id(Self))
        print('function2 called!')


self_test = SelfTest()
# self_test.funtion1()
SelfTest.funtion1()
self_test.funtion2()

print(id(self_test))
SelfTest.funtion2(self_test)

print()
print()

# 결과===>
# function1 called!
# 2557369579224
# function2 called!
# 2557369579224
# 2557369579224
# function2 called!

print('예제3--------------------------------------------------------------------------------')
# 예제 3
# 클래스 변수, 인스턴스 변수
# 인스변수는 무조건 self 가 들어가야함
# 클래스 변수는 self 가 없음


class WareHouse:
    # 클래스 변수
    stock_num = 0
    # 셀프가  없어서 여러 인스턴스에서 공유

    def __init__(self, name):
        self.name = name
        WareHouse.stock_num += 1

    def __del__(self):
        WareHouse.stock_num -= 1


user1 = WareHouse('kim')
user2 = WareHouse('Park')
user3 = WareHouse('Lee')
print()
print()


print('클래스 변수--------------------------------------------------------------------------------')
# 클래스 변수
print(user1.__dict__)
print(user2.__dict__)
print(user3.__dict__)
print(WareHouse.__dict__)  # 클래스 네임스페이스, 클래스 변수를 공유함.

print()
print()

# 결과===>
#{'name': 'kim'}
#{'name': 'Park'}
#{'name': 'Lee'}
# {'__module__': '__main__', 'stock_num': 3, '__init__': <function WareHouse.__init__ at 0x000002536F1A6D08>, '__del__': <function WareHouse.__del__ at 0x000002536F1A6D90>, '__dict__': <attribute '__dict__' of 'WareHouse' objects>, '__weakref__': <attribute '__weakref__' of 'WareHouse' objects>, '__doc__': None}


print('인스턴스 변수--------------------------------------------------------------------------------')
# 인스턴스 변수
print(user1.name)
print(user2.name)
print(user3.name)
print(user1.stock_num)

print()
print()
# 결과===>
# kim
# Park
# Lee
# 3
