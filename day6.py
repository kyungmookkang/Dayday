
"""
입출력 종류 : 표준, 파일, 네트워크
파일 입출력
- 파일 열기
1) - open() : 파일 열기
2) -> 파일 입력(read)/출력 (write)
3) -> 파일 닫기(close)
: 결론 : 메모리 관리를 소홀히 하지 마세요~

+Encoding Error
file - settings - editor - file encodings - project encoding - utf-8변경
"""

# 파일에 문자열 출력(쓰기)
f = open("hello.txt","w")   # 파일을 쓰기 용도로 열기
# open(파일명, 모드)
# 프로그램 상에서는 쓰기 모드로 열려있는 hello.txt 파일이 f라는 이름으로 사용됨

f.write('hello world')
f.close()

# 파일로부터 문자열 입력(읽기)
f = open("hello.txt", "r")
s = f.read()    # 읽은 내용을 s 에다가 잘 저장해라
print(s)
f.close()

"""
with ~ as 파일을 사용한 뒤에 자동으로 파일을 닫아줌 
with open(파일이름, 모드) as 파일변수:
    코드  
"""
with open("hello.txt", "r") as f:
    s = f.read()
    print(s)
# close 작업을 자동으로 수행

# 파일에 여러 줄 출력

"""
목표 값:
hello world 1
...
hello world 10
"""
# w 모드로 열게되면 기존에 작성되어 있던 내용은 사라짐 (덮어쓰기)
with open("hello.txt", "w") as f:
    for i in range(10):
        f.write("hello world {0} \n".format(i+1))
    # f.write("hello world 2 \n")
    # ... 이렇게 하면 바보

"""
리스트의 내용을 파일에 출력 

lines = ['안녕\n', '반가워\n', '잘지내\n']
with open("hello.txt", "w") as f:
   #  f.write(lines)  # Error 문자열만 받는다...
    f.writelines(lines)  # 줄이 안바뀌어서 보기 구리다 /n을 붙여보자
   
   with open("hello.txt", "r") as f:
    s = f.read()    # read 함수는 1 글자씩 읽어드림
    print(s)

with open("hello.txt", "r") as f:
    line = None
    while line != "":
        line = f.readline()    # readline 함수는 1 줄씩 읽어드림, 첫 문장만 읽음(for 또는 while문과 함께 사용해야한다)
        print(line.strip("\n"))     # \n을 삭제

with open("hello.txt", "r") as f:
    line = (f.readlines())
    # for i in range(len(line)):
    for i in line:
        print(i.strip("\n"))

* pickle 피클 : 파이썬 객체를 파일로 저장하고자 하는 경우에 사용되는 모듈
* 피클링 : 객체 -> 파일
* 언피클링 :파일 -> 객체

문자
문자열 객체

hello
nicetomeetyou
bye

강
경기도 용인시
30
컴퓨터

박
서울시 강남구
33
중국어

: 차이점 구조화 이름 주소 나이 전공..
"""
# 객체를 파일로 저장
import pickle

내용물 = "단팥"
색상 = "파랑"
너비 = "20센치"
높이 = "10센치"
가족명단 = {"잉어":30, "꽃게":10, "상어":40}

with open("myfish.p", "wb") as f:    # 객체 저장 시 w 가 아닌, wb(write binory)이진수,,로 저장
    pickle.dump(내용물, f)
    pickle.dump(색상, f)
    pickle.dump(너비, f)
    pickle.dump(높이, f)
    pickle.dump(가족명단, f)
# 프린트 하면 읽지 못한다 이상한 글자 나옴 ...
# 어떻게 읽어야할까 ? rb !!
import pickle

with open("myfish.p", "rb") as f:
    내용물 = pickle.load(f)   # pickle 의 load 함수로 객체를 읽어들이자.
    색상 = pickle.load(f)   # pickle 의 load 함수로 객체를 읽어들이자.
    너비 = pickle.load(f)   # pickle 의 load 함수로 객체를 읽어들이자.
    높이 = pickle.load(f)   # pickle 의 load 함수로 객체를 읽어들이자.
    가족명단 = pickle.load(f)   # pickle 의 load 함수로 객체를 읽어들이자.

print(내용물)
print(색상)
print(너비)
print(높이)
print(가족명단)

f = open("hello.txt", "a")  # a 는 append 의 약자
for i in range(3):
    f.write("%d 번째 줄 추가\n" %(i+1))
f.close()

''''
클래스 ? 붕어빵기계 : 면접에서 자주 묻는 질문 
객체 ? 붕어빵
메서드(동작)? 굽는다
attribute(속성) ? 내용물, 크기, 모양, ... 너비, 높이
'''

'''
res = 0
def add(n):
    # n에 전달된 값을 res에 저장
    global res
    res += n

add(3)
print(res)
add(4)
print(res)
'''
res1 = 0    # 전역변수
res2 = 0
def add1(n):    # 지역변수
    global res1
    # n 에 전달된 값을 res에 저장
    res1 += n
    return res1

print(add1(3000))
print(add1(5000))

print("-"*5)
# 2번 계산대

res1 = 0    # 전역변수
res2 = 0
def add2(n):    # 지역변수
    global res2
    # n 에 전달된 값을 res에 저장
    res2 += n
    return res2

print(add2(1500))
print(add2(3000))

''' 
100개의 계산대가 필요하다고 하면 너무 복잡하고 번거롭다 
이런 점을 해결할 방법 !!! 클라스~ 
클래스 : 각가의 계싼대를 객체로 간주하고 계산대의 특성 또는 동작 등을 일반화시켜 놓은 틀
정관사 / 부정관사
the car (객체)
a car (클래스)

사람(클래스) : 실체가 없음
사람홍길동(객체), 사람임꺽정(객체) : 실체가 있음
자동차(클래스) : 실체가 없음
내 아반뗴(객체)
  '''
print("-"*5)
class Calculator:   # 클래스명은 대문자로 시작한다.
    def __init__(self):
        self.res = 0
        print("init 함수가 호출됐네?")
    def add(self, n):
        self.res += n
        return self.res

cal1 = Calculator()     # 클래스로부터 객체를 생성. 계산대(클래스)로부터 계산대1(객체)를 생성
cal2 = Calculator()     # 클래스로부터 객체를 생성. 계산대(클래스)로부터 계산대2(객체)를 생성
print(cal1.add(3000))
print(cal1.add(5000))


print(cal2.add(1500))
print(cal2.add(2000))

import mod1
print(mod1.madd(1,2))

import mod1 as m # as: 모듈(패키지)명이 긴 경우, 축약해서 표현
print(m.madd(4,5))

# import pandas as pd
# import numpy as np
# import matplotlib.pyplot as plt
# 폴더 안에는 파일/폴더
# 빨간 줄은 설치가 안돼있어서 그렇다.

from mod1 import msub
# mod1 모듈에 정의되어 있는 msub 메서드만 가져와라
print(msub(6,3))

from mod1 import * # 모든 함수를 가져와라

print(madd(3,2))    #5
print(msub(10,3))   #7

print("-"*20)

# 1. 주어진 자연수가 홀수인지 짝수인지 판별해 주는 함수(is_odd)를 작성해 보자.

#n = int(input())
# if n%2 == 0:
#     print("%d is even!" %n)
# else:
#     print("%d is odd!" %n)

# 2. 다음은 "test.txt"라는 파일에 "Life is too short" 문자열을 저장한 후 다시 그 파일을 읽어서 출력하는 프로그램이다.
# 사용자의 입력을 파일(test.txt)에 저장하는 프로그램을 작성해 보자. (단 프로그램을 다시 실행하더라도 기존에 작성한 내용을 유지하고 새로 입력한 내용을 추가해야 한다.)

a = open("text.txt", "w")
a.write("Life is too short\n you need java")
a.close()

with open("text.txt", "r") as a:
    a = a.read()
    print(a)

# 3. 다음과 같은 내용을 지닌 파일 test.txt가 있다. 이 파일의 내용 중 "java"라는 문자열을 "python"으로 바꾸어서 저장해 보자.
# Life is too short
# you need java

with open("text.txt", "r") as a:
    a = a.read()
print(a.replace("java","python"))

# 4. "비트코인" 문자열을 화면에 출력하는 print_coin() 함수를 정의하라.
def print_coin():
    return "비트코인"


# 5. 4에서 정의한 함수를 호출하라.
bit = print_coin()
print(bit)

# 6. 4에서 정의한 print_coin 함수를 100번 호출하라.
def print_coin():
    return "비트코인"
bit = print_coin()
for i in range(100):
    print(bit)

print("-"*20)
# 7. "비트코인" 문자열을 100번 화면에 출력하는 print_coins() 함수를 정의하라.
def print_coins():
    return (bit+" ")*100
print(print_coins())

# 8. 하나의 문자를 입력받아 문자열 끝에 ":D" 스마일 문자열을 이어 붙여 출력하는 print_with_smile 함수를 정의하라.
# sm = str(input())
# def print_with_smile():
#     return (sm+":D")
# haha = print_with_smile()
# print(haha)
#     print("%d is even!" %n)
# else:
#     print("%d is odd!" %n)

# 9. 현재 가격을 입력 받아 상한가 (30%)를 출력하는 print_upper_price 함수를 정의하라.
# i = [300, 500, 1000, 1500]
# def print_upper_price():
#     return sort.i[-3:]
# print(print_upper_price())

# 10. 하나의 리스트를 입력받아 짝수만 화면에 출력하는 print_even 함수를 정의하라.
lines = [1,3,5,4,6,12,67,68,9,100]
pe = lines
if i %2 ==0:
         print()

#
# def print_even():
#
#     return i
# print(print_even())


# 11. 하나의 딕셔너리를 입력받아 딕셔너리의 key 값을 화면에 출력하는 print_keys 함수를 정의하라.
def print_keys(dic):
    print(list(dic.keys()))
dic = {'BTS': {'머큐리':4.5, '매트릭스':4.0}, '소녀시대': {'머큐리':3.5, '매트릭스':3.0} }
print_keys(dic)

# 12. 문자열과 한줄에 출력될 글자 수를 입력을 받아 한 줄에 입력된 글자 수만큼 출력하는 print_mxn(string) 함수를 작성하라.
def print_mxn(string):
    print(str)

# 13. 연봉을 입력받아 월급을 계산하는 calc_monthly_salary(annual_salary) 함수를 정의하라. 회사는 연봉을 12개월로 나누어 분할 지급하며, 이 때 1원 미만은 버림한다.
# calc_monthly_salary(12000000)
# 1000000
def calc_monthly_salary(annual_salary):
    print(int(annual_salary / 12))
calc_monthly_salary(120000000)


# 14. 문자열 하나를 입력받아 인터넷 주소를 반환하는 make_url 함수를 정의하라.
# make_url("naver")
# www.naver.com
def make_url(addr):
    print("www."+addr+".com")
make_url("naver")

# 15. 문자열을 입력받아 각 문자들로 구성된 리스트로 반환하는 make_list 함수를 정의하라.
# make_list("abcd")
# ['a', 'b', 'c', 'd']
def make_list(str):
    print(list(str))
make_list("abcd")

'''16. 게임 기업 입사문제
어떤 자연수 n이 있을 때, d(n)을 n의 각 자릿수 숫자들과 n 자신을 더한 숫자라고 정의하자.
예를 들어
d(91) = 9 + 1 + 91 = 101
이 때, n을 d(n)의 제네레이터(generator)라고 한다. 위의 예에서 91은 101의 제네레이터이다.
어떤 숫자들은 하나 이상의 제네레이터를 가지고 있는데, 101의 제네레이터는 91 뿐 아니라 100도 있다. 그런데 반대로, 제네레이터가 없는 숫자들도 있으며, 이런 숫자를 인도의 수학자 Kaprekar가 셀프 넘버(self-number)라 이름 붙였다. 예를 들어 1,3,5,7,9,20,31 은 셀프 넘버 들이다.
1 이상이고 5000 보다 작은 모든 셀프 넘버들의 합을 구하라.
'''
not_self_num = set()
for i in range(1,5000):
    num = i+sum(map(int,str(i)))
    not_self_num.add(num)
self_num = set(range(1,5000))-not_self_num
print(sum(self_num))


'''
1. 다음 입사문제
1차원의 점들이 주어졌을 떄, 그 중 가장 거리가 짧은 것의 쌍을 출력하는 함수를 작성하시오.
(단 점들의 배열은 모두 정렬되어있다고 가정한다.)
예를 들어 S - {1,3,4,8,13,17,20}이 주어졌다면, 결과값은 (3,4)가 될 것이다.
'''
S = {1, 3, 4, 8, 13, 17, 20}
def spair(S):
    dict = {}
    for (x,y) in zip(S[:-1], S[1:]):
        if not dict.get(y-x):
            dict[y-x] = [(x,y)]
        else :
            dict[y-x] = dict[y-x] + [(x,y)]

    return dict[min(dict.keys())]
S = [1, 3, 4, 8, 13, 17, 20]
print(spair(S))


'''
2.
회문(palindrome)? 순서를 거꾸로 해서 읽어도 제대로 읽을때와 같은 단어 or 문장
rotator, sos, abba (nurses run)
문제: 임의의 단어(문장)을 입력받아 회문 여부를 출력 => True or False 출력
'''
# def palindrome(string, start, stop):
#     if (stop - start <= 0):
#         return True
#     else:
#         return ((string[start] == string[stop]) and
#                 palindrome(string, start + 1, stop - 1))
#
# while (True):
#     a = input()
#     if (a == '0'): break
#     if (palindrome(a, 0, len(a) - 1)): print("yes")
#     else: print("no")
























