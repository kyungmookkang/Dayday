# 3)adv
#      *
#     ***
#    *****
#   *******
#  *********
i=1
while i<10:
    s = ("*"*i)
    i += 2
    print(s.center(9))



# 4. for 문을 사용해

# 5. 소수를 구해보자 1~100
for num in range(2,101):
    for i in range(2, num+1):
        if num == i:
            print(num, end=" ")
        elif num % i == 0:
            break
# 쉽게 만들어보기
#
# 97 : 2 ~ 9 : 8번만 연산
# 2~96 : 95번 연산
# 제곱근
# 예) 12의 제곱근 :3
# 12의 약수 : 2, 3. ...

# lotto
import random
#
# for i in range(6):
#     [].append(randint(1,45))
# if len(set[]) == 6:

num_lotto = set()

for i in range(7):
    num_lotto.add(random.randint(1,46))
list_lotto = list(num_lotto)
list_lotto.sort()
print(list_lotto)

# 4-1. for 문을 사용해 2부터 100까지 숫자 중 소수를 (prime number)를 출력해보자.
# * 소수란? 1과 자기 자신으로만 나누어 떨어지는 수(2. 3 . 5. 7. 11. ..)

for k2 in range(2,101):
    for num in (2,k2):
        if k2 % num != 0:
            print(k2)

num_list = [1]
while len(num_list) < 6:
    num = random.randint(1,45)  # randint 마지막수 포함
    while num in num_list:  # num_list(로또번호가 저장된 리스트)에 방금 뽑은 수가 있다면
        num = random.randint(1,45)
    num_list.append(num)
print("로또 1등 당첨은 !!!! : ", num_list)

answer = set()
while len(answer) < 6:
    num = random.randrange(1,46)
    answer.add(num)
print("로또 1등 당첨 ! ", answer)

# 입력 -> 함수 -> 출력
#  def 함수명(매개변수 0 개 이상):
#     문장1
#     문장2
# 함수 정의 구문

# 함수 호출 구문

def add(a, b):
    sum = a + b
    return sum       # return : 출력이라고 보면 된다.

res = add(1, 2)   # parameter(인수)
print(res)

# 수행순서
# 함수는 스스로 수행하지 않는다. 호출해야만 수행
# 1) add(1,2) 호출
# 2) add 함수 수행 -> sum 리턴
# 3) sum이 res에 저장


def add(a, b):  # 사용자 함수(매개 변수)
    sum = a + b
    print("add 함수")
    return sum       # return : 출력이라고 보면 된다.

print("호출 전")
res = add(1, 2)   # parameter(인수)
print("호출 후")
print(res)

# 입력값이 없는 함수
def say():
    return "NANISITEN"  # return을 통해 say() 라는 함수가 "NANISITEN"으로 변환된다고 보면 이해 쉽다.
print(say())
s = say()
print(s)

# 출력값이 없는 함수(return문이 없는 함수)
def add(a, b):
    # return      # 출력값이 없다 : return 뒤 뭐 없어
    print("두 수의 합은 : ", a + b)
res = add(3, 4)
print(res)

# 매개변수의 초기값을 설정하여 함수 호출
def add(a,b):
    return a+b
res = add(b=5, a=3)
print(res)



def add(a,b=3):
    print(b)
    print(a)
    return a+b
res = add(2,5)  # 외부에서 전달되는 인수가 있으면 매개변수에 초기값이 등록이 돼있더라도 외부인수가 우선순위 !
print(res)

# 함수로 전달되는 인수의 개수가 정해져 있지 않은 경우
def add(a,b):
    res = a + b
    return res
r = add(1,2)
print(r)

def add(*arg):  # 매개변수(arguments) 명 앞에 *을 붙이면 튜플로 인식
    print(arg)
    res = 0
    for i in arg:
        res += i    # res = r + i
    return res
r = add(1,2,3,4)
print(r)

# 연습문제
# 곱셈
def mul(*args):
    print(args)
    res = 1
    for i in args:
        res *= i # res = res * i
    return res
res = mul(1,2,3)
print(res)
# res = mul(1,2,3) 인수가 가변적
# => 6 출력

# 연습문제2
def addmul(op, *args):
    print(op)
    print(args)
    res = 1
    for i in args:
        res += i # res = res * i
    return res
res = addmul("add",1,2,3,4)
print(res)
# res = addmul("add", 1,2,3,4) 인수가 가변적
# print(res) 1+2+3+4 결과 출력

# res = addmul("add", 1,2,3,4) 인수가 가변적
# print(res) 1*2*3*4 *5결과 출력
def addmul(op, *args):
    if op == "add":
        res = 0
        for i in args:
            res += i

    elif op == "mul":
        res = 1
        for i in args:
            res *= i
        return res

res = addmul("mul", 1,2,3,4)
print(res)


def am(a,b):
    return  a+b, a*b    # 함수의 결과는 항상 1개. 튜플형식으로 (덧셈,곱셈) 리턴
res = am(3,4)
r1 = res[0]
r2 = res[1]
print(r1)

r1,r2 = am(3,4)
print(r1)
print(r2)

def prn(a):
    if a == "Hello":
        return      # Hello 면 돌아간다. 하지만 Hello 가 아닌 다른 문장일 땐 리턴 발동 하지않음.
    print("Good to see you")

prn("How are you?")

# def say(name, age, male=True):  # 매개변수를 작성하세요
#     if name == '사나':
#         age = 25
#     res = say("내 이름은 :", name, age)
# say('사나',25)

def say(name, age, female=True):  # 매개변수를 작성하세요 / 기본값(male = True)는 꼭 매개변수 마지막에 둬야한다.
    print("내 이름은", name)
    print("나이는", age)
    if female:
        print("성별은 여")
    else:
        print("성별은 남")
say('사나',25)


# 목표 값 : say('사나', 25)
# 내 이름은 사나
# 나이는 25
# 성별은 여

# 목표 값 : say('사나', 25, True)
# 내 이름은 사나
# 나이는 25
# 성별은 여

# 목표 값 : say('태연', 26, False)
# 내 이름은 태연
# 나이는 26
# 성별은 남

# 목표 값 : say('태연', 26)
# 내 이름은 태연
# 나이는 26
# 성별은 여

a = 1
def mytest(a):
    a = a+1
mytest(10)   # 매개변수 a는 함수 안에서만 사용되는 변수임, 함수 밖에 있는 a가 아님
print(a) # 1
print(mytest(a))


# scope
a = 1
def mytest3(a):
    a = a+1     # 함수 안에서 밖에 있는 변수를 증가시키고 싶다면?2가지 방법 존재 1) return 2) global

mytest3(a)
print(a)    #2가 출력됐으면..

# 1. return 사용
a = 1
def mytest3_1(a):
    a = a + 1  # 함수 안에서 밖에 있는 변수를 증가시키고 싶다면?2가지 방법 존재 1) return 2) global
    return a
a = mytest3_1(a)
print(a)  # 2가 출력됐으면..

# 2. global 사용 : 함수 안에서 함수 밖의 변수를 직접 사용 가능
a = 1
def mytest3_2():
    global  a
    a = a + 1
mytest3_2()
print(a)

# lambda : def와 동일한 기능 수행하는 예약어
# 함수 정의시 일반적으로 def를 사용 / 함수가 복잡하거나 def를 사용하지 못하는 곳에서는 림다사용

# 1. def
def myadd(a,b):
    return a + b
res = myadd(2,3)
print(res)

# 2. lambda
myadd2 = lambda a,b : a+b
# 함수명 = lambda 변수1,변수2, ... : 매개변수를 이용한 계산식
res = myadd2(2,5)
print(res)

# # Quiz

# def mymax(*args):
# m = max(mymax(5,1,3,2))
# print(m)

# print(mymax(5,1,3,2,))  # 5
# print(mymax(2,7,9)) # 9
def mymax(*args):
    print(max(args))
mymax(5,1,3,2)

# for 문 사용
def mymax(*args):
    m = 0
    for i in range(len(args)):
        if m < args[i]:
            m = args[i]
    return m
print("최대값 :", mymax(5,1,3,2))
print("최대값 :", mymax(2,7,9))


#
def pt(x):
    return x+10
print(pt(1))
#
pt = lambda x : x+10
print(pt(1))

# 람다 함수 자체를 바로 호출
(lambda x : x+10)(1)
print((lambda x : x+10)(1))

print((lambda x,y : x+y)(1,2))

y = 2
print((lambda x : x+y)(1))

print((lambda x,y = 3: x+y)(1))

def pt(x):
    return x+10
map(pt, [1,2,3])
# 함수의 인수 부분에 간단한 함수를 적용하고자 하는 경우
print(list(map(pt, [1,2,3])))
# map(함수, 데이터)
print(list(map(lambda x : x+10, [1,2,3])))


# Quiz
# fl =['test.c', 'test2.h', 'sample.py', 'sample2.c']
# # 확장자가 c or h 인 파일 이름을 모두 화면에 출력
#
# for i in fl:
#     test
#


# 1. 리스트에서 20 보다 작은 3의 배수를 출력하라

lst = [13, 21, 12, 14, 30, 18]
12
18
for i in lst:
    if i % 3 == 0 and i < 20:
        print(i)

# 2. 리스트에서 세 글자 이상의 문자를 화면에 출력하라
lst = ["I", "study", "python", "language", "!"]
print(lst[1:4])
# or
for sam in lst:
    if len(sam) >= 3:
        print(sam)
# study
# python
# language

# 3. 파일 이름이 저장된 리스트에서 확장자를 제거하고 파일 이름만 화면에 출력하라.
lst3 = ['hello.py', 'ex01.py', 'intro.hwp']

for i in lst3:
    res = i.split(".")
    print(res[0])

# hello
# ex01
# intro

# 4. my_list를 아래와 같이 출력하라.
my_list = ["가", "나", "다", "라"]
for i in range(0,3):
    print(my_list[i], my_list[i+1])

# 가 나
# 나 다
# 다 라
print("=======")
# 5. 반복문과 range 함수를 사용해서 my_list를 아래와 같이 출력하라.
list_5 = ["가", "나", "다", "라"]
for i in range(3,0,-1):
    print(list_5[i],list_5[i-1])
# 라 다
# 다 나
# 나 가

# 6.리스트에 5일간의 저가, 고가 정보가 저장돼 있다. 고가와 저가의 차를 변동폭이라고 정의할 때, low, high 두 개의 리스트를 사용해서 5일간의 변동폭을 volatility 리스트에 저장하라.
low_prices  = [100, 200, 400, 800, 1000]
high_prices = [150, 300, 430, 880, 1000]

volatility = []
for i in range(5):
    volatility.append(high_prices[i]-(low_prices[i]))
print(volatility)

# 7.리스트에 저장된 데이터를 아래와 같이 출력하라.
apart = [ [101, 102], [201, 202], [301, 302] ]
for i in apart:
    print(i[0], "호")
    print(i[1], "호")

    print("----")




# 101 호
# 102 호
# -----
# 201 호
# 202 호
# -----
# 301 호
# 302 호
# -----
#
# 8. 구글 입사 test
# 1부터 10,000까지 8이라는 숫자가 총 몇번 나오는가?
#
# 8이 포함되어 있는 숫자의 갯수를 카운팅 하는 것이 아니라 8이라는 숫자를 모두 카운팅 해야 한다.
# (※ 예를들어 8808은 3, 8888은 4로 카운팅 해야 함)

e = 0
for i in range(1,10001):
    e += str(i).count('8')
print(e)

print(str(list(range(1,10001))).count('8'))
# count : 문자열 관련하여 특정 문자의 개수를 세는 함수
# 8128.count(8) # 숫자는 불가
# 때문에 묹자화 시킨다. str 함수
i = 8128
print(str(i).count('8'))
print(str(8128).count('8'))

















