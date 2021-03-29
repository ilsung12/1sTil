# 210113
# 파이썬 함수식 및 람다(lambda)

# 함수 정의
# def 함수명(parameter):
#   code

# 함수 선언 위치 중요

# 예제 1
print('--------리턴값이 없는 함수-------------------------------------------------------')

def hello(world):
    print("hello", world)


hello("Python !")
hello(7777)

# 결과값 :
# hello Python !
# hello 7777

print('--------리턴값이 있는 함수-------------------------------------------------------')

# 예제 2


def hello_return(world):
    va = "hello " + str(world)
    return va


t1 = hello_return("python !!!!!!!!")
print(t1)

# 결과값 : 
# hello python !!!!!!!!

print('--------다중 리턴---------------------------------------------------------------')


# 예제 3 (다중 리턴)
def func_mul(x):
    y1 = x * 100
    y2 = x * 200
    y3 = x * 300
    return y1, y2, y3  # 리턴해주는 값이 여러개


v1, v2, v3 = func_mul(1)
print(v1, v2, v3)


# 결과값 : 
# 100 200 300


print('--------데이터 타입 반환---------------------------------------------------------')

# 예제 4 (데이터타입 반환)

def func_mul2(x):
    y1 = x * 100
    y2 = x * 200
    y3 = x * 300
    return [y1, y2, y3]


lt = func_mul2(100)
print(lt, type(lt))

# 결과값 : 
# [10000, 20000, 30000] <class 'list'>


print('--------*args, *kwargs----------------------------------------------------------')

# 예제 5
# *args, **kwargs


def args_func(*args):
    # for t in *args:
    #     print(t)
    # * : 여러 개의 인수를 받을 때, 키워드 인수를 받을 때 사용하는 표시
    # *a 라고 써도 되고, *asdfg 라고 적어도되고, *myname 라고 적어도 된다.

    for i, v in enumerate(args):
        print(i, v)


args_func('kim')
print("")
args_func('kim', 'park')
print("")
args_func('kim', 'park', 'lee')
print("")

# **kwargs
# **kwargs는 (키워드 = 특정값) 형태로 함수를 호출할 수 있다.
# 그것은 그대로 딕셔너리 형태로 {'키워드': '특정 값'} 이렇게 함수내부로 전달됨.


def kwargs_func(**kwargs):
    for k, v in kwargs.items():
        print(k, v)


kwargs_func(name1='kim')
print()
kwargs_func(name1='kim', name2='park', name3='lee')
print()


# 전체 혼합

def example_mul(arg1, arg2, *args, **kwargs):
    print(arg1, arg2, args, kwargs)


example_mul(10, 20)
example_mul(10, 20, 'park', 'kim', age1=24, age2=35)


# 결과값 : 
# 0 kim

# 0 kim
# 1 park

# 0 kim
# 1 park
# 2 lee

# name1 kim

# name1 kim
# name2 park
# name3 lee

# 10 20 () {}
# 10 20 ('park', 'kim') {'age1': 24, 'age2': 35}


print('--------중첩 함수(클로저)--------------------------------------------------------')

# 중첩 함수(클로저)


def nested_func(num):
    def func_in_func(num):
        print('>>>', num)
    print("in func")  # 얘가 먼저 나옴 *스포주의; 원리는 num의 위치
    func_in_func(num+1000)


nested_func(10000)  # num의 값은 여기서 출력 되기 때문

# 결과값 :
# in func
# >>> 11000


print('--------------------------------------------------------------------------')

# 예제 6


def func_mul3(x: int) -> list:
    y1 = x * 100
    y2 = x * 200
    y3 = x * 300
    return [y1, y2, y3]


print(func_mul3(2))
# print(func_mul3(5))

print("")

# 결과값 :
# [200, 400, 600]

print('--------람다식------------------------------------------------------------------')

# 람다식 예제
# 람다식 : 메모리 절약, 가독성 향상, 코드 간결
# 함수는 객체 생성 -> 리소스(메모리) 할당
# 람다는 즉시 실행(heap 초기화) -> 메모리 초기화


# 일반적 함수 -> 변수 할당
def mul_10(num: int) -> int:
    return num * 10


var_func = mul_10
print(var_func)
print(type(var_func))
print(var_func(10))
print("")


def lambda_mul_10(num): return num * 100 # 람다식 : 한줄요약 이랄까
print('>>>', lambda_mul_10(10))
print("")


def func_final(x, y, func):
    print(x * y * func(10))

func_final(10, 10, lambda_mul_10)
print(func_final(10, 10, lambda x: x * 1000)) # 함수내에서도 명령어로 가능 


# 결과값 : 
# <function mul_10 at 0x00000288954F8048>
# <class 'function'>
# 100

# >>> 1000

# 100000
# 1000000
# None


