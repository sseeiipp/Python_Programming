a = 2
b = 3
print(a, end=" ")
print(b)
print(a, b, sep=",")

a = 2
b = 3
# a = (2,b) = 3

x = y = z = 0
a, b = 2, 3  # 튜플 언패킹
print(a, b)

# 값 swap
temp = a
a = b
b = temp
print(a, b)

a, b = b, a

# 변수명
# CamelCase, snake_case
snake_case = "뽀로로"
camelCase = "뽀로로"
MAX_VALUE = 100
# 파이썬 자료형
# 1. 기본 자료형 : 숫자형(정수,실수) ,불리언,문자열
# 2. 컬렉션 자료형 : 리스트, 튜플, 딕셔너리, 집합

# 숫자형
a = 10
print(type(a))
# 2진수, 8진수, 16진수
print(bin(a), oct(a), hex(a))
print(ord("A"), chr(65))

# int 자료형은 값 의 표현 범위가 제한 X
x = 10**100
print(x, type(x))

# 오버플로우 테스트
a = 2147483647 + 1
print(a, type(a))

b = 3.14
print(b, type(b))

# 실수형의 표현 범위
# 부동소숫점 저장 방식
# 64비트 = 부호(1비트) + 지수부(11비트)
# 실수의 오차 발생

import sys

print(sys.float_info.min)
print(sys.float_info.max)

print(-sys.float_info.min)
print(-sys.float_info.max)

a = 1.7e308
b = 1.8e308
print(a, b)

# 실수의 오차
print(0.1 + 0.2 == 0.3)
print(f"{0.1:.20f}")
print(f"{0.2:.20f}")
print(f"{0.3:.20f}")

# 형변환
print(float(100))
print(int(3.14))
print(float("3.14"))
print(int("123"))
