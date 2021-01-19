# 210118
# 파이썬 모듈과 패키지

# 패키지 예제
# 상대 경로
# .. : 부모디렉토리
# .  : 현재디렉토리




 # fibonacci
# class fibonacci:
#  def __init__(self, title="fibonacci"):
#   self.title = title
  
#  def fib(n):
#   a, b = 0, 1
#   while a < n :
#    print(a, end = '')
#    a, b = b, a + b
#   print()
  
#  def fib2(n):
#   result = []
#   a, b = 0, 1
#   while a < n :
#    result.append(a)
#    a, b = b, a+b
#   return result
  
 
 
 # calculation
# def add (l, r):
#  return l + r


# def mul (l, r):
#  return l * r


# def div (l, r):
#  return l / r
  
      



 # 사용 1 (Fibo -> 클래스 형태 -> from y.x import x)

import builtins

from pkg.fibonacci import Fibonacci

Fibonacci.fib(300)

print("ex1: ", Fibonacci.fib2(400))
print("ex1: ", Fibonacci().title)


# 결과 

# 01123581321345589144233
# ex1:  [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377]
# ex1:  fibonacci


print("-------------------------------------------------------------------")

# 사용 2 (클래스 형태, 권장x)
from pkg.fibonacci import *

Fibonacci.fib(500)

print("ex2: ", Fibonacci.fib2(600))
print("ex2: ", Fibonacci().title)


# 결과

# 01123581321345589144233377
# ex2:  [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377]
# ex2:  fibonacci


print("-------------------------------------------------------------------")


# 사용 3 (클래스 형태, alias)
from pkg.fibonacci import Fibonacci as fb

fb.fib(1000)

print("ex3: ", fb.fib2(1600))
print("ex3: ", fb().title)


# 결과

# 01123581321345589144233377610987
# ex3:  [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597]
# ex3:  fibonacci



print("-------------------------------------------------------------------")


# 사용 4 (함수 형태)
import pkg.calculation as c

print("ex4 : ", c.add(10, 100))
print("ex4 : ", c.mul(10, 100))


# 결과

# ex4 :  110
# ex4 :  1000


print("-------------------------------------------------------------------")


# 사용 5 (함수)
from pkg.calculation import div as d
print("ex5 : ", int(d(100, 10)))


# 결과 

# ex5 :  10

print("-------------------------------------------------------------------")


# 사용 6 
import pkg.prints as p
import builtins

p.prt1()
p.prt2()
print(dir(builtins))



