dic={'아이디': '홍길동', '레벨':10, '체력': 100, '마나':20, '공격력': 200, '방어력':50}
print(dic.keys())
print(dic.values())
print(dic.items())

dic.clear()     # 모든 요소들을 제거
print(dic)      #{}

dic={'아이디': '홍길동', '레벨':10, '체력': 100, '마나':20, '공격력': 200, '방어력':50}
print(dic['아이디'])
print(dic.get('체력'))    # 키에 연결된 값을 추출
# 딕셔너리.get(키) == 딕셔너리[키]
print(dic.get('민첩'))    #None <> print(dic['민첩']Error!

if dic.get('민첩'):
    print('민첩 능력이 있습니다')
else:
    print('민첩 능력치가 존재하지 않습니다')

if dic.get('마나'):
    print("마법사 입니다")

dic = {'아이디': '홍길동', '레벨': 10, '체력': 100, '마나': 20, '공격력': 200, '방어력': 50}
print(dic.get('민첩',0))       # 민첩 키가 존재하지 않으면 디폴트 값으로 0을 출력

# ============================== #
# 집합(set)   : {}, 순서가 없음(오름,내림,알파벳,... 무시), 중복이 없음

s1=set([1,2,2,3])  # 리스트 자료를 기초로 집합(중복 제외)을 생성
print(s1) # 중복을 제거한 값 출력
# print(s1[2]) # Error : 리스트or튜플은 순서가 있음 -> 인덱싱을 통해 데이터에 접근 가능
# 반명에 Set은 순서가 없다 -> 인덱싱 불가능 -> 인덱싱으로 접근하려면 ? 리스트or튜플로 변환 후 인덱싱 수행
s11=list(s1)
print(s11[2])   # 인덱싱 가능


s2=set("hihello")
print(s2)
print(list(s2)) # 순서대로 나열하기위해 리스트

list()
tuple()
dict()


s1=set([1,2,3,4,5,6])
s2=set([4,5,6,7,8,9])
# 교집합
# s1&s2 / .intersection 함수
print(s1&s2)
print(s1.intersection(s2))

# 합집합
# '|'  / .union 함수
print(s1|s2)
print(s1.union(s2))

# 차집합
# '-' / .difference 함수
print(s1-s2)
print(s1.difference(s2))

s3=set()
s3.add(3)
print(s3)

# s3.add(3,4,5)   # .add 함수는 데이터 1개만 가능하다.
print(s3)

# update 함수 : 여러 개를 추가
s3.update([3,4,5,6])
print(s3)

s3.update([1,2,3,4,15,16])
print(s3)

# remove : 제거하기
s3.remove(3)
print(s3)

# ======================== #
# Bool불 자료형 : True(참) or False(거짓)
# True: "test", [1,2], 1, ...
# False: "", None, 0, {}, {}, ()




a=[1,2,3]
print(a.pop())
print(a.pop())

# while 조건:  # 조건이 참을 만족하는 동안에 문장 수행을 반복하세요. (조건이 거짓이 될 때까지)
    # 문장1
    # 문장2
    # ...

a=[1,2,3]

while   a: # a 리스트에 pop 대상 데이터가 남아 있는 경우
    print(a.pop()) #3 2 1
print("반복문을 종료합니다")

# if 조건:
#     문장1
#     문장2
# else
#     문장1
#     문장2

# if []:  #if 조건
#     print("True")
# else :
#     print("False")

# print((bool([])))
# print(bool)("dsdasd")
# print(bool(0))

a=[1,2,3]
# 변수 = 리스트? 리스트(객체)는 메모리에 생성되고, 변수 a는 리스트가 저장된 메모리상 주소를 가지게 된다
# a변수가 가리키는 메모리의 주소를 확인
print(id(a))    # 메모리의 140214116885824 번지에 [1,2,3]이 저장되어 있다는 의미

a=[1,2,3,]
b=a # a가 가지고 있는 값은 엄밀히 말하면 [1,2,3]이 저장되어 있는 "주소값"
print(id(b))
print(id(a)) # 두 값이 같음(= a가 가지고 있는 주소값이 b에 복사(저장))

# 두 변수가 가리키는 메모리상의 대상이 동일한지 확인
a=[1,2]
b=[1,2]
print(a is b)   #a와 b가 가리키는 메모리상의 대상이 동일한가요 ?
print(a==b)

# b 변수를 만들 떄, a 변수의 값은 가져오면서도 a와는 다른 주소를 가리키도록 하고싶다.
# 1번 방법 [:] 이용
a=[1,2,3]
b=a[:]  #b=a는 동일한 대상(데이터)를 가리킴
print(id(a))
print(id(b))
print(a)
print(b)
a[1]=10
print(a)
print(b)

# 2번 방법 copy모듈에 있는 copy함수를 이용

# 패키지(폴더) : 모듈(파일) 또는 패키지의 묶음
# 모듈 : 관련 함수들의 묶음

# from 모듈명 import 함수명
# 모듈로부터 함수를 가져와라
from copy   import copy
a=[1,2]
b=copy(a) #b=a[:] 와 같음
print(id(a))
print(id(b))
print(a is b)   # 주소가 다르니깐

# IF 조건문

# if 조건문:
#     코드

x=1
if x==1:
    print("x는 1이다")
    print("x는 홀수이다")
print("출력됩니다") # if 와는 별개의 문장

    #pass    # 코드를 수행하지 않고 넘어감
    # print("x는 1이다")

x=5
if x>=1:
    print("1이상")
    if x>-5:
        print("5이상")
    if x==10:
        print("10")
print("출력")

money=True
if money:
    print("버스")
    print("택시")
else:
    print("도보")

# or, and, not : 여러 조건을 표현

money = 1000
card = True
if money>=5000 or card : # or:또는, and:그리고(이고, 이면서)
    print("Taxi")
else:
    print("Bus")

# ================

money = 1000
card = True
if money>=5000 and card : # or:또는, and:그리고(이고, 이면서)
    print("Taxi")
else:
    print("Bus")

# ================

money = 6000
card = True
# if card != False:   # != '같지 않다'

if not money <= 5000:
    print("Taxi")
else:
    print("Bus")

# ================
# x in 리스트(튜플, 문자열)
print(1 in [1,2,3])
print(4 not in (1,2,3))
print('a' in ('a','b'))

#===================

# if 조건:
#     문장
# else:
#     문장

# if 조건:
#     문장
# elif 조건:
#     문장
# elif 조건:
#     문장
# else:
#     문장

money=1000
card=True
if money > 3000:
    print("Taxi")
elif card: # 3000원 이하의 돈을 가지고 있지만, 카드를 가지고 있다면
    print("Bus")
else: # 3000원 이상도 없고, card도 없는 경우
    print("Walking")

Temp=18
if Temp >=25:
    print("Turn it on")
elif Temp >=22:
    print("Keep it")
else:
    print("Turn it off")

# 자율자동차 동작의 일부를 if구문으로 작성한다면, if가 몇 개 필요할까? 무한대....
# if 앞에 뭔가 있다면 :
#     결과=확률계산
#     if 결과값이 0.5 이상:
#         print('Stop')
#     else:
#         print("Drive")

s=60
if s>=60:msg="pass"
else:msg="fail"
print(msg)
# same same same
s=60
if s>=60:
    msg="pass"
else:
    msg="fail"
print(msg)

#================
# 퇴근을 5초 당겨주는 궁극의 코드

s=60
msg="pass"  if s>=60 else "fail"
# 조건문이 참인 경우 if 조건문 else 조건문이 거짓인 경우
# 만약에 s가 60 이상이면 "pass" 를 msg에 대입하고ㅡ 아니면 "fail"을 msg에 대입
print(msg)

#==================
# 반복문 : for, while
i=0
while i<10: # 'i 변수 값이 10보다 작다.' 라는 조건을 만족하는 동안에, 반복하세요.
    i=i+1
    print(i, "번째 반복 수행")

while True: # 무한 루프(loop)
    i=i+1
    print(i, "번째 반복 수행")

    # 조건을 만족했을 때, 반복 종료
    if i>10:
        break # 반복문을 빠져나가라

prompt="""
1. 추가
2. 삭제
3. 종료
번호 입력 : """
print(prompt)


# num=0
# while num!=3:
#     print(prompt)
#     num=int(input())    # 종료(3) 할 때까지 prompt 반복

a=0
while a<10:
    a=a+1
    if a%2==0: continue # continue는 while의 시작위치로 이동
    print(a)

# 연습문제
# While 문을 이용하여 1~100 사이의 자연수 중 4의 배수의 합을 출력.

f=4
while f<100:
    f=f+4
    f=f+f
    print(f)

# answer
i=0
sum=0
while i<=100:
    if i%4==0:
        sum=sum+i
    i=i+1
print(sum)

#=============
# for 문

# for 변수 in 리스트/튜플/문자열:
#     문장1
#     문장2

mylist=[1,2,3]
for i in mylist:
    print(i)

mylist=["원","투","쓰리"]
for i in mylist:
    print(i)

mylist=["bigdata"]
for i in mylist:
    print(i)

for i in [(1,2),(3,4),(5,6)]:
    print(i)

for i in [(1,2,3)]:
    print(i)

for i,j in [(1,2),(3,4),(5,6)]:
    print(i)
    print(j)
    print("="*30)

for i in range(5):
    print(i)

for i in range(3,10):
    print(i)

for i in range(3,10,2):
    print(i)

a=[5,6,7,8]
for i in range(len(a)):
    print(i)

i=2
for dan in range(1, 10):    # dan = 2 to 9
    for i in range(1,10):   # i= 1 to 9
        print(dan*i, end=" ")   #
    print("")   # 줄 바꿈





# =======================================================================================



# 1. a 리스트에서 중복 숫자를 제거하자.
a = [1,1,1,2,2,3,3,3,4,4,5]
print(set(a))

# 2. while 문을 사용해 1~1000 까지의 자연수 중 3의 배수이면서 7의 배수인 수의 합을 구해 보자.

i=0
sum=0

while i <= 1000:
    i += 1
    if i%3 == 0 and i%7 == 0:
        sum += i
print(sum)

# 3. while문을 사용하여 다음과 같이 별(*)을 표시하는 프로그램을 작성해 보자.

# 1)
# *
# **
# ***
# ****
# *****

i = 0
while i < 5:
    i += 1
    print("*"*i)

# 2)
#      *
#     **
#    ***
#   ****
#  *****
i=0
while i<5:
    i += 1
    s = ("*"*i)
    print(s.rjust(5))

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


# 4. for 문을 사용해 1부터 100까지의 숫자를 출력해보자.

for nums in range(1,101):
   print(nums, end=" ")

# 4-1. for 문을 사용해 2부터 100까지 숫자 중 소수를 (prime number)를 출력해보자.
# * 소수란? 1과 자기 자신으로만 나누어 떨어지는 수(2. 3 . 5. 7. 11. ..)


# 5. A 학급에 총 10명의 학생이 있다. 이 학생들의 중간고사 점수는 다음과 같다.
score = [70, 60, 55, 75, 95, 90, 80, 80, 85, 100]
# for문을 사용하여 A 학급의 평균 점수를 구해 보자.
sum = 0
for s in score:
    sum+=s
avg = sum/len(score)
print("Average : ", avg)

# 6. 로또 당첨 번호 제작(adv)
# *주의:중복된 수 나오면 안됨
# 이번 주 로또 당첨 번호 :  3 7 13 22 25 29

# print(random.random())  # 0~1
# print(random.randrange(1,7))    # 1~6
# print(random.randrange(1,7))
#
# print(random.randint(1,46)) #1~45
# print(random.randrange(1,46))
# # 차이점
# print(random.randrange(1,46,2)) # 1~45까지 2씩 증가시킨 수 중에서 난수 발생
import random
lotto = []
while len(lotto) < 6:
    nums = random.randrange(1,46)
    if nums in lotto : pass
    else: lotto = lotto + [nums]
    print(lotto)

# 7. 자판기(pro, 커피 한 잔에 300원이라 가정, 초기 커피는 10개)
# 돈을 넣어 주세요: 500
# 거스름돈 200를 주고 커피를 줍니다.
# 돈을 넣어 주세요: 300
# 커피를 줍니다.
# 돈을 넣어 주세요: 100
# 돈을 다시 돌려주고 커피를 주지 않습니다.
# 남은 커피의 양은 8개입니다.
# 돈을 넣어 주세요: 0
# 종료합니다
# pro = input("돈을 넣어주세요 : ")
price = 300
c = 10

while c>0:
    money = int(input("돈을 넣어주세요 : "))
    if money == 500:
        print("거스름돈 200를 주고 커피를 줍니다.")
        c -= 1
    elif money == 300:
        print("커피를 줍니다.")
        c -= 1
    elif money == 100:
        print("돈을 다시 돌려주고 커피를 주지 않습니다.", "남은 커피의 양은 %d 개 입니다." % c)
    else:
        print("종료합니다.")
        break














