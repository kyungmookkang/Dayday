print(1,2,3, sep="&")

print(3>2)  # 비교 연산자는 True or False 값으로 출력된다.
# print(2=2)  # equal이 한 번만 들어가면 equal이 아닌 assign으로 인식한다.
print(2==2)

print(3!=2) #!= : 느낌표 이퀄은 not equal : 같지 않다.

print('pyhton'=='Python')
print('python'!='Python')

print(1==1.0)   # 정수와 실수라는 점에서 차이, 값은 같습니다. 그래서 == 비교하면 True
# print(1 is 1.0) # is는 두 객체가 같은지 비교. 1은 정수객체, 1.0은 실수객체. 그래서 두 객체는 다르다.
# 홍길동나이==임꺽정나이(나이를 비교)
# 홍길동 is 임걱쩡 (사람을 비교)

# 논리 연산자 : and(모두 참->참), or(하나 이상 참->참), not(참->거짓, 거짓->참)

print(True and False)
print(False or False)
print(not False)

print(1==1 and 2!=1)
print(3>1 or 1<2)
print(not 1>2)

# 0:False, 1:True, 0이 아닌 모든 수가 True : 문법
print(bool(1))
print(bool(0))
print(bool(0.5))

print("="*50)

print(bool('test')) # 문자열도 True
print(bool(''))     # 빈 문자열은 False

print(bool(0 or 'test')) # False or True : True / 오직 False or False 만 False
print(bool(0 and 'test')) # False and True : False

# False or False -> False
# True and True -> True
# 0:거짓, 1:참

print("hi")
print("                     hi")
print("hi               ")

print("%10s" % "hi")    # 전체 열자리인데 뒤에 두칸은 hi
print("hello%10s" % "hi")
print("%-10shello" % "hi")

print("%.4f" % 3.141592)     # 소수 이하 5째 자리에서 반올림 ->4째 자리까지 표현 f: flaot
print("%10.4f" % 3.141592)     # 10자리를 확보한 다음 출력(우측 맞춤)


num=3
s='two'
day='three'

print(("I have %d apples" %num))
print(("I have %s apples" %s))

print("="*50)   # 위의 데이터 값을 십진수 %d, 문자열 %s 신경써야하지만 하위 .foramt()함수는 모두 가능하다. 즉, 더 편하다.

print(("I have {0} apples".format(num)))    # {}중괄호 안의 값이 format안의 값으로 대체된다.
print(("I have {0} apples".format(s)))    # {}중괄호 안의 값이 format안의 값으로 대체된다.

print("I had {0} eggs, so I was full for {1} days.".format(num,day))
#print("I had {0} eggs, so I was full for {1} days.".format(0,1,2,3......))

print("="*50) # 하위는 가능하지만, 잘 사용하진 않는다.

print("I had {num} eggs, so I was full for {day} days.".format(num=5, day=3))   # 다양하게 응용 가능하다.
print("I had {0} eggs, so I was full for {day} days.".format(5, day=3))   # 다양하게 응용 가능하다.

print("{0}".format("hi"))
print("{0:<10}".format("hi"))   #10자리 확보후 왼쪽 정렬
print("{0:>10}".format("hi"))   #10자리 확보후 오른쪽 정렬
print("{0:^10}".format("hi"))   #10자리 확보후 가운데 정렬
print("{0:^10}".format("hi"))   #10자리 확보후 가운데 정렬

print("{0:-<10}".format("hi"))   #10자리 확보후 가운데 정렬
print("{0:-^10}".format("hi"))   #10자리 확보후 가운데 정렬

print("{0:.4f}".format(3.141592))
print("{0:10.4f}".format(3.141592))

a="hello"

print(a.count('l')) # 문자가 몇 개 있는지 카운트 하는 함수.
print(a.count('e'))

#위치 확인
print(a.find('l'))  # 위치 : 2, 여러개 있는 경우에는 맨 처음 나온 위치가 출력
print(a.find('x'))  #   -1 : 문자가 없는 경우

print(a.index('l'))  #
# print(a.index('x'))  # 에러발생: 문자가 없는 경우 (이것이 .find 와 .index의 차이점)
print(a.find('x'))  #   -1 : 문자가 없는 경우

# 매우 많이 사용하는 Join 함수

print("abcd")
# 문자 사이사이에 ','를 넣고싶다.
print(",".join("abcd")) # 문자열 삽입
print(",".join(['a','b','c','d']))
# 리스트에 저장되어 있는 각각의 문자들이 컴마(,)와 결합하여 하나의 문자열이 됨.

print("".join(['a','b','c','d'])) # "abcd"

# South Korea, south Korea, SOUTH KOREA, ...

a="hi"
print((a.upper()))

print(a) # 여전히 "hi"
# 대문자로 변경하고자 한다면,
a=a.upper()
print(a)
# 소문자는 .lower
a=a.lower()
print(a)

# "대한민국" "대  한민국" "   대한민국"   ...
# 공백을 제거하는 함수

co1="  대한민국  "
co2="   대한민국"
# nstirp/rstrip 왼쪽:l 오른쪾:r 양쪽:strip
print(co2.lstrip())
print(co1.strip())
# "대  한민국" 사이는 없애지 못한다.

s="Life is too short"
#replace : 문자(열)을 치환

print(s.replace("is","isn't'"))
print(s.replace("Life","Your leg"))

print(s.split()) # 공백문자로 분리 -> 리스트로 출력
s="Life$is$too$short"
print(s.split('$')) # m: method(=function), c: class

t=str.maketrans('aeiou','12345')
print('apple'.translate(t)) #apple 문자열을 t 변환테이블을 참조하여 변환하세요.
# 문자 바꾸기
# str.maketrans('바꿀문자', '새문자') 작성하여 변환테이블 생성
# 엑셀의 찾기 -> 변경과 유사하다.

# 정규표현식 : 문자열 전처리
str=", python,."
print(str.lstrip(","))  # 왼쪽에 위치한 ","를 제거함
print(str.lstrip(" "))  # 왼쪽에 위치한 " "를 제거함
print(str.lstrip(" ,"))  # 왼쪽에 위치한 " ,"를 제거함 # 큰따옴표 안에 제거대상 문자를 나열
print(str.lstrip(", "))  # 왼쪽에 위치한 ", "를 제거함

print(str.rstrip(" ,."))  # 왼쪽에 위치한 ", "를 제거함

str="mook is cool~!@"
print(str.rstrip("cool"))
# [l/r]strip("삭제대상문자들")


# 메서드(함수) 체이닝(chaining) -> 코드가 간결해짐

print('python'.rjust(10))
s='python'.rjust(10)
print(s.upper())

print('python'.rjust(10).upper())

# 함수 : 우리 프로그램에 기본적으로 적재가 되는 함수 : 내장함수 (print),..
# 별도로 적재를 해야하는 함수 (import 한 다음에 사용) : 외장함수

import string
print(string.punctuation)
# punctuation(구두점) : !@#$%^&*(^%$#@}{+_)(<>?,.
print(str.strip(string.punctuation))
print(str.strip(string.punctuation+" "))

print('python'.ljust(10)   ) # 10자리 확보 후 좌측 정렬
print('python'.rjust(10)   ) # 10자리 확보 후 우측 정렬
print('python'.center(10)   ) # 10자리 확보 후 가운데 정렬


# Padding(패딩) : 특정 값으로 빈자리를 채우는 것.
print("hello".zfill(10))    # z:zero : 0으로 채워라

print("apple pineapple".find('p'))  # 가장 먼저 나오는 p의 자릿수를 출력
print("apple pineapple".find('pp'))

print("apple pineapple".rfind('p'))  # 오른쪽부터 가장 먼저 나오는 p의 자릿수를 출력
print("apple pineapple".rfind('pp'))

# # 리스트 ?
# x1=10
# x2=20
# x3=30
#
# x=[10,20,30]    # [] 안의 값들은 '요소'라고 부른다.
# print(x)
# # x 리스트의 0번 index 요소값 : 10
# print(x[0])
# y=['life','is','too','short']
# print(y[1])
#
# # 리스트에 다양한 자료형(정수, 실수, 불린, 문자, 요소, ...)을 저장할 수 있음
# z=[1,2,'life','is','too','short',True, 3.14]
# print(z[2])
# print(z[7])
#
# a=[1,2,['lfie','is']]   # a 변수에는 요소가 몇 개? 3(0~2번)
# print(a[2]) # ['lfie','is']
# # is 를 출력하려면 ?
# print(a[2][1])
#
# a=[1,2,['life','is',['too','short']]]
# # 'too' 출력
# print(a[2][2][0])
# print(a[-1][-1][0])
#
# b=[]        # 빈 리스트 생성
# b=list()    # 빈 리스트 생성
#
# b=[1,2,3]
# print(b[0]+b[2])
#
# Ashton=[30, 1, ['코딩', '산책', '영화']]
# Ashton=[30, 1, ['코딩', '산책', ['어벤져스','킬빌']]

# 리스트 Slicing

x=[10,20,30,40,50]
print(x[1:4])

s="abcdefg"
print(s[2:5])

a=[1,2,3,['x','y','z'],4,5]
# x, y 출력
print(a[3][0:2])

range(5)    # 0~5 : 0~4 (5-1:4) 까지 숫자를 생성
print(list(range(5))) # 0,1,2,3,4

print(list(range(3,10))) # [3, 4, 5, 6, 7, 8, 9]

print(list(range(3,10,2))) # [3, 5, 7, 9]

print(list(range(10 ,0,-1))) # [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

# 리스트 연산(+,*)
a=[1,2]
b=[3,4]
print(a+b)  # [1, 2, 3, 4]

print(a*3)  # [1, 2, 1, 2, 1, 2]
print(len(a))   # 2

# print(a[0]+"hi")    # 1hi? -> 에러발생!!! (정수와 문자열은 더할 수 없다)
print(type(a[0]))
print(type("hi"))
# type이 같아야한다.

# import string
# a=[1,2]
#
# print(str(a[0])+"hi")    체크!!!!!!!!!!!!소스!!


a=list(range(1,10))
print(a)
del a[:5]   # 0~4번 index까지 삭제
print(a)

a=[1,2,3]
print(a)
# 4를 뒤에 추가하고 싶다면 ?
print(a+[4])

a.append(5)   # 뒤에다 추가한다.
print(a)

a.append([5,6,7,10])    # 요소로 묶여서 추가된다.
print(a)

a.extend([5,6,7,10])    # 묶이지 않고 확장.
print(a)

a+=[100,101]    # 다양한 방법
print(a)

# 정렬 : 정해진 순서(내림/오름차순(0->0, ㄱ->ㅎ, a->z)로 데이터를 나열

a=[3,7,5,1]
a.sort()        # sort : 정렬함수 : a에 저장된 자료를 정렬(오름)하고 결과를 a에 저장
print(a)

# 아래와 같이 출력하면 안됨
a=[3,7,5,1]
print(a.sort())     # none 곧바로 출력해서 확인할 수 없다.

a=['b','k','d']
a.sort()
print(a)

a=[3,7,5,1]
a.sort()       # 내림차순 해보자
a.reverse()         # reverse !
print(a)

# 리스트의 특정 위치에 데이터 추가 : insert
a=[7,8,9]
# 7과 8 사이에 4 추가 : insert
a.insert(1,4)   # 들어갔을 때 7과8 사이인 2번쨰 자리임으로 0,1,2,3~ : (1,4(들어갈 값))
print(a)

# 리스트의 요소를 제거 : del, remove, pop

# del: 특정 위치에 지정된 값을 제거
a=[10,20,30]
del a[1]
print(a)


# remove : 특정 값을 제거
a=[10,20,30,10,20,30]
a.remove(30)    # 첫째 30만 제거
print(a)

# pop
a=[10,20,30]
a.pop() # 가장 마지막 위치에 있는 데이터를 제거
print(a)


# 연습문제
# 1.다음과 같은 문자열이 있을 때 이를 대문자 BTC_KRW로 변경하세요.
ticker = "btc_krw"
print(ticker.upper())


# 2.다음과 같은 문자열이 있을 때 이를 소문자 btc_krw로 변경하세요.
ticker = "BTC_KRW"
print(ticker.lower())

# 3.다음과 같은 문자열이 있을 때 공백을 기준으로 문자열을 나눠보세요.
a = "hello world"
print(a.split(" "))


# 4.다음과 같이 문자열이 있을 때 btc와 krw로 나눠보세요.
ticker = "btc_krw"
print(ticker.split("_"))


# 5.다음과 같이 날짜를 표현하는 문자열이 있을 때 연도, 월, 일로 나눠보세요.
date = "2020-12-30"
print(date.split("-"))


# 6.문자열의 오른쪽에 공백이 있을 때 이를 제거해보세요.
data = "039490     "
print(data.rstrip())

# 7.
# 변수에 다음과 같이 문자열과 정수가 바인딩되어 있을 때 % formatting을 사용해서 다음과 같이 출력해보세요.
name1 = "김민수"
age1 = 10
name2 = "이철희"
age2 = 13
# 이름: 김민수 나이: 10
# 이름: 이철희 나이: 13
print("이름: %s 나이: %d" %(name1, age1))
print("이름: %s 나이: %d" %(name2, age2))


# 8. 문자열의 format( ) 메서드를 사용해서 7번 문제를 다시 풀어보세요.
print("이름: {0} 나이: {1}".format(name1, age1))
print("이름: {0} 나이: {1}".format(name2, age2))


# 9. 컴마를 제거한 후 이를 정수 타입으로 변환해보세요.
price = "5,969,782,550"
price.replace(",","")

print(int(price.replace(",","")))

# 10. 다음과 같은 문자열에서 '2020/12'만 출력하세요.
분기 = "2020/12(E) (IFRS연결)"
print(분기[0:7])

# 11. 아래 문자열에서 소문자 'a'를 대문자 'A'로 변경하세요.
string = 'abcdfe2a354a32a'

print(string.replace("a","A"))


# 12.
# 주민등록번호 뒷자리의 맨 첫 번째 숫자는 성별을 나타낸다. 주민등록번호에서 성별을 나타내는 숫자를 출력해 보자.
pin = "881120-1068234"
print(pin[-7])

# 13.다음과 같은 문자열 a:b:c:d가 있다. a#b#c#d로 바꿔서 출력해 보자.
a = "a:b:c:d"
print(a.replace(":","#"))

# 14. ['Life', 'is', 'too', 'short'] 리스트를 Life is too short 문자열로 만들어 출력해 보자.
# (join 활용)
# 매우 많이 사용하는 Join 함수
print(" ".join(['Life', 'is', 'too', 'short']))

