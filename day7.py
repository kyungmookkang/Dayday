# 파이썬 라이브러리 : 수 많은 파이썬 함수


# 1) abs 함수
print(abs(-3))  # 절대값을 구하는 함수

# 2) all 함수 : 모두 참 -> True
print(all([1,2,3]))  # 1, 2, 3 모두 다 참
print(all([1,2,3,0]))   # 1,2,3,0 거짓이 있으므로 전체가 거짓이 됨

# 3) any 함수 : 어느 하나라도 참 -> 참, 모두 거짓 -> 거짓
print(any([1,2,3,0]))   #1,2,3,0 참이 있으므로 전체가 참.
print(any([0, ""])) # 모두 거짓
print(any([]))  # 비어있는 리스트는 거짓 -> 거짓

# 4) chr 함수 : 아스키 코드 -> 문자를 출력 함수
# 아스키 코드 ? : ASCII American Standard Code for Information Interchange : 7진법/ 0~126 총 127개
print(chr(65))  # A when? 아스키 코드 사용할 떄,

# 5) ord 함수 : 문자 -> 아스키코드를 출력
print(ord('A')) # 65

# 6) !! 중요 !!
# enumerate : 열거형 데이터를 표현하는 함수, for 문과 함께 사용
# 리스트, 튜플, 문자열 과 같이 시퀀스를 같은 데이터 -> 입력 -> 인덱스를 포함하는 enumerate 객체 생성

for i in ['aaa', 'bbb', 'ccc']:
    print(i)    # aaa / bbb / ccc 이 떄, 시퀀스의 번호를 부가해볼까 ? enumerate

for idx,i in enumerate(['aaa', 'bbb', 'ccc']):
    print(idx, i)    #0,aaa / 1,bbb / 2,ccc
# 7) 인덱스 : 자료의 위치(순서)번호, 0번 부터 사용
a=[10,20,30]   # :10 0번, 20 1번, 30 2번

# 8) eval 함수 : 문자열로 구성된 수식 -> 입력 -> 문자열을 실행한 결과를 리턴 출력.  # tensorflow, deeplearning 시, 많이 사용한다.
print("10+20")  # "10+20"
print(type("10+20"))

print(eval("10+20"))  #  30
print(type(eval("10+20")))

print(eval("divmod(5,3)")) # 몫과 나머지도 계산한다.

# 8) filter 함수 : 원하는 데이터를 걸러내는 함수
# filter(함수이름, 1번째 인수에 있는 함수에 입력될 반복 가능한 자료형)
# filter 함수의 리턴값이 True인 값들만 묶어서 돌려준다.

# 8-1)

def pos(a):
    res = []
    for i in a:
        if i>0:
            res.append(i)
        return res

print(pos([1,3,-5,-7,9]))   #[1,3,9] 만 추출하고싶다.-> 위의 함수 체크

# 8-2) filter 함수
def pos2(a):
    return a>0
print(list(filter(pos2, [1,3,-5,-7,9])))

# 8-3) filter + lambda 함수
print(list(filter(lambda a:a>0,[1,3,-5,-7,9])))

# 9) hex 함수 : 16진수로 변환
print(hex(234))
# 16진수 ea = e*16+a*1=14*16+10*1=234

# int함수 : '3' -> 3 / 10진수
print(int('3'))
print(float('3.4'))
print(int('ea',16))

# 10) 일반적인 리스트 저장 표현
num = []
for n in range(11):
    num.append(n)
print(num)
#  리스트 내포(comprehension)
print([ n for n in range(11) ]) # : 콜론 기호 없음
print(list(n for n in range(11)))

print([ n*2 for n in range(11) ])

# Quiz
# 1~10 까지의 짝수만 저장
evenNum = []
for i in range(1,11):   # No.1
    if i % 2 == 0:  # No.2
        evenNum.append(i)
print(evenNum)

# List comprehension
oddNum = []
print([i for i in range(1,11)  if i % 2 == 0 ])
#                    No.1            No.2

# 리스트
# [(메뉴,후식),...]
[('쌈밥', '사과'),
 ('쌈밥', '아이스크림'),
 ('쌈밥', '커피'),
 ('치킨', '사과'),
 ('치킨', '아이스크림'),
 ('치킨', '커피'),
 ('쌈밥', '아이스크림'),
 ('쌈밥', '커피'),
 ('쌈밥', '아이스크림'),
 ('쌈밥', '커피'), ]

# 11) 이중 for 문 .. 삼중 사중~~~
li = []
for x in ['쌈밥', '치킨', '피자']:
    for y in ['사과', '커피', '아이스크림']:
        print((x,y))
        li.append((x,y))
print(li)

# 12) 리스트 내포
['쌈밥', '치킨', '피자']
['사과', '커피', '아이스크림']

print([ (x,y) for x in   ['쌈밥', '치킨', '피자']  for y in ['사과', '커피', '아이스크림'] ])

contest = []
['경묵', '주동', '광태', '영환', '병찬','상원']
['농구','축구','배구','야구','달리기']

print([ (x,y) for x in ['경묵','주동', '광태', '영환', '병찬','상원'] for y in  ['농구','축구','배구','야구','달리기'] ])

# 0~9 까지 수 중에서 5보다 작으면서 2로 나누어 떨어지는 수를 리스트에 저장하시오. : 0 2 4
print([ x for x in range(10)  if x < 5 and x % 2 == 0   ])
print([ x for x in range(10)  if x < 5 if x % 2 == 0   ])

print([x+y for x in range(10) for y in range(10)])

# 셋{} comprehension
print({x+y for x in range(10) for y in range(10)})  # 이거는 셋이다 중복값 제거

# 딕셔너리{} comprehension {키:값 키:값 ...}
print({x+y: "값" for x in range(10) for y in range(10)})  # 이거는 셋이다 중복값 제거

score = {'철수':50, '영희':70, '순신':100}
print({ name:num for name, num in score.items() if name != '영희' })


score = {'철수':50, '영희':70, '순신':100}
# 점수가 60점 이상이면 pass, 미만이면 fail
# 출력 = {'철수':fail, '영희':pass, '순신':pass}

print({ name:num for name, num in score.items() } )

scores= {'철수':50,'영희':70,'순신':100}

print({name: 'pass' if value > 60 else 'fail' for name, value in scores.items() })

# Quiz 1
words =['Computer', 'Coke', 'Bread']
# 리스트 컴프리헨션으로
print([ word.lower() for word in words] )

# Quiz 2
a = [1, -5, 4, 2, -2, 10]
# a에 저장된 값이 0보다 크면 a값, 작으면 0을 저장하고 출력
print([ i if i > 0 else 0 for i in a  ])

# Quiz 3
a = [1,2,3,4,5]
# a값이 1이면 "pass", 2이면 "fail", 나머지는 "no"
# print([ i if i ==1 "pass" elif i==2 "fail" else "no" for i in a                         ])
print([ "pass" if i == 1 else "fail" if i == 2  else "no" for i in a   ])



for i in a:
    if i ==1:
        print("pass")
    elif i==2:
        print("fail")
    else:
        print("no")

print("-"*30)

# 13) 딕셔너리 응용
x = {'a':10, 'b':20, 'c':30}
print(x)

x['aa']= 40
print(x)
# 13-1) setdefault
x.setdefault('d')   # 키 d가 추가, 값이 None 저장
print(x)
# 13-2) update
x['a'] = 100
  # 마지막 저장값이 수정된다.
x.update(b=200)
print(x)

x['z'] = 99
print(x)

x.update(k=50, s=55, p=100)
print(x)

x.update({'a':10, 'd':30})
print(x)

# 13-3) zip
print(list(zip([1,2],['one','two'])))
x.update(zip(['aa','c'],[999,777]))
print(x)

x={'a':10, 'b':20, 'c':30, 'd':40}
print(x)
x.pop('d')      # pop 쓸 때 key를 지정해야함
print(x)

v = x.pop('a')
print(v)    # 10

x={'a':10, 'b':20, 'c':30, 'd':40}
del x['b']
print(x)

x.clear()
print(x)

# 14) 리스트(튜플) -> 딕셔너리 생성
li = ['a','b','c']
d = dict.fromkeys(li)
print(d)

d2 = dict.fromkeys(li,10)
print(d2)

from collections import defaultdict # collections 모듈에서 defaultdict 함수를 가져옴
# print(d2['z']) 키가 없으므로 에러
d2 = defaultdict(int)
print(d2['z'])

d3 = {'a':10, 'b':20}
# key만 출력
# value만 출력
# key,value쌍을 출력
for k in d3:
    print(k)

for k in d3.keys():
    print(k)

for v in d3.values():
    print(v)

for k,v in d3.items():
    print(k,v)

keys = ['a','b','c','d']
print(dict.fromkeys(keys))

for key, value in dict.fromkeys(keys).items():  # dict.fromkeys(keys)는 딕셔너리
    print(key, value)

d4 = {key:value for key, value in dict.fromkeys(keys).items()} # dict.fromkeys(keys)는 딕셔너리
print(d4)

x = {'a': 10, 'b': 20, 'c': 30, 'd': 40}
newx = { k:v for k,v in x.items() if k != 'b'   }
print(newx)

# newx는 x에 저장된 데이터에서 값이 '20'인 자료를 뺀 나머지를 저장
newx = { k:v for k,v in x.items() if v != 20}
print(newx)

# 딕셔너리 = {키1: {키a:값a}, 키2: {키c:값c, 키d:값d}}
영화평점  = {'BTS': {'머큐리':4.5, '매트릭스':4.0}, '소녀시대': {'머큐리':3.5, '매트릭스':3.0} }

print(영화평점['BTS']['매트릭스'])

영화평점['BTS']['매트릭스'] = 5
print(영화평점['BTS']['매트릭스'])

x = {'a':0,'b':1}
y = x # 실제로는 딕셔너리가 1개 만들어짐
print(x is y)   # 변수 이름만 다를 뿐 x,y 는 같은 객체

x['a'] = 100
print(y)

y = x.copy()    # 완전히 다른 2개의 딕셔너리가 만들어짐
print(x is y)
print(x==y)
x['a']=111
print(x)
print(y)

x = {'a':{'python':'3.8'}, 'b': {'python':'2.7'}}
y = x.copy()

y['a']['python'] = '2.777777'
print(y)
print(x)

#중첩 딕셔너리에서는 copy메서드 대신 copy모듈의 deepcopy함수를 사용
x = {'a':{'python':'3.8'}, 'b': {'python':'2.7'}}
import copy
y = copy.deepcopy(x)    # 깊은 복사
y['a']['python'] = '2.777777'
print(y)
print("="*50)

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