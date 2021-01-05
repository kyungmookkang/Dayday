# print(1, 2, 3, sep="&")

print(list(range(5)))

# 튜플, 시퀀스, 딕셔너리

# 튜플은 리스트와 거의 동일
# 차이점 ?    : 튜플은 값을 변경(생성, 삭제, 수정)할 수 없음, () 사용

t1=(1,2,3) # 튜플
print(t1)
print(type(t1))
 # del t1[1]   # 참조할 때는 [](대괄호) 사용, index 1의 값 제거, 에러발생 !

# t1[0]=5 # 생성, 삭제, 수정이 되지 않기 떄문에 자료를 변경하면 안되는 상황에 사용가능 : 정책, 고유코드, 등 ..

print(t1[2])    # 인덱싱

print(t1[1:]) # 슬라이싱

t2=('a',3,4)
print(t1+t2)    # 튜플도 리스트와 마찬가지로 + 결합이 가능하다.

t3=(5,6)
print(t3*5)     # 곱셈 연산도 가능

print(len(t3))

person=('kim',20,60.5,True)     #
print(person)

t4=(7)
print(t4)
print(type(t4))     # type이 tuple이 아니라 int ?   : 연산자로 이해한다. 만약 튜플로 표현하고자 한다면 t4=(7,) 콤마를 찍어준다.

t5=5,8  # 되도록 튜플을 나타내는 기호(소괄호)로 묶어서 표현할 것. 묶지 않아도 가능은 하다.

print(t5)

print(range(5))
print(list(range(5)))

print(range(5))
print(tuple(range(5)))

print(tuple(range(5,20)))

print(tuple(range(5,101,2)))    # 마지막 인덱스는 증가의 폭을 의미

# 튜플 -> 리스트 변환
# 리스트 -> 튜플 변환

x=tuple(range(1,10))
print(x)
# 튜플 -> 리스트 : x에 저장된 5 -> 50 변경하고 싶은 경우
# x[4]=50     # error

# x[4] = 50
print(list(x))
print(type(list(x)))
tempx=list(x)
print(tempx)
tempx[4]=50
print(tempx)

y=[1,2,3]
tempy=tuple(y)
print(type(tempy))

s="hello"
print(list(s))
# 리스트에 문자열을 주면 문자 리스트가 만들어진다.
print(tuple(s))
# 튜플에 문자열을 주면 문자 튜플이 만들어진다.

a,b,c=1,2,3
print(a)
print(type(a))

k=1,2,3
k=a,b,c
print(a)
print(type(a))

# 시퀀스 자료형 : 연속적으로 저장
# 리스트, 튜플, 문자열, range, byte, bytearray 등은 모두 다 값들이 연속적으로 저장되어 있는 시퀀스 자료형
# (1,2,3)   [1,2,3] "hello" ....

# 시퀀스 자료형의 공통 기능

# 데이터 존재 유무 확인
# 작성방법 : 찾고자 하는 값 in 시퀀스객체

# 연습문제 0
a=[0,10,...,90]
alpha=range(0,91,10)
a=list(range(0,91,10))
print(list(alpha))

# a에 30이 있는지 확인 ?
print(30 in a) # true

# a에 30이 없는지 확인 ?
print(30 not in a) # false

print("hello 문자열에 h문자가 있나요?", 'h' in "hello")

# 시퀀스 객체 연결(하지만 range는 불가능)
a=(1,2)
b=(3,4)
print(a+b)

# print(range(0,4)+range(4,6))  # error

print(list(range(0,4))+list(range(4,6)))  # range->list로 변경한 다음 연결
print("hi"+"hello")

# 문자열 연결 : +
# 문자열과 숫자 연결 불가능
# print("hi"+100)   # error

# 문자열과 숫자 연결 => 숫자 -> 문자로 변경 먼저
str(100) + "hi"     # 숫자를 문자로 바꾸는 str 함수.
print(str(100) + "hi")

# 시퀀스 반복 *  단, range는 *연산자 사용 불가
# 시퀀스객체 * 정수 * 시퀀스객체
print([1,2,3]*5)

# range 객체를 튜플 또는 리스트로 변경한 다음 반복
print(list(range(0,5,1))*3)

print("ㅋ"*10)

# len(시퀀스객체) : 시퀀스 데이터(요소) 개수
a=[10,20,30,40]
print(len(a))

b=(1,2,3,4)
print(len(b))
print(len(range(1,10,2)))

print(len("안녕하세요")) # ㅣen 함수는 길이를 구함
# python 2.7 version  바이트 수가 나옴(15)
# python 3.xx version 글자의 수가 나옴(5)

s="안녕하세요"
print(len(s.encode('utf-8')))
# utf-8에서는 한글 한 글자가 3byte, 3*5 = 15 바ㅣ트

print(s.encode('utf-8'))

# 시퀀스 객체는 대괄호[] 기호로 참조
a=[5,6,7,8,9]
print(a[3])
print(a[-2])

r=range(1,10,2)
print(r[2])
print(a[-4])

s="Ohayo"
print(s[3])
print(a[-3])

# del 시퀀스객체 [인덱스] : 튜플, range, 문자열도 사용안됨
b=[10,20,30,40]
del b[1]
print(b)

# h="hello"
# del h[2]
# print(h)

# 시퀀스객체[시작인덱스:끝인덱스]
a=[10,20,30,40]
print(a[0:3])
print(a[0:0])
print(a[0:1])
print(a[1:-1])
print(a[1:-1:1])
print(a[3:1:-1])

print(a[0:len(a)])  # a[0:4]=a[0]~a[3]
print(a[:3:2])  #a[0]~a[2], 2칸씩 건너뛰기 -> a[0], a[2]  참조

r=range(20)
print(r[3:8])
print(r[:15:3])
print(list(r[:15:3]))

s="hello python"
s[:10]
print(s[:10])
print(s[:10:2])

# slice 객체를 이용하여 slicing
range(20)
# print(range(20))[slice(3,9,2)]
print(list(range(20)[slice(3,9,2)]))
       #     [5,6,7,...,19]: 8  10

print(list(range(10)))
print(a)
a[1:4]='a'
print(a)
a=list(range(10))
a[1:4]=['a','b','c']
print(a)

a=list(range(10))
a[2:7:2]=['x','y','z']
print(a)

a=list(range(10))
a[2:7:2]=['x','y','z']
print(a)

a=list(range(10))
a[2:7:2]=['x','y','z']
print(a)

print(a)
del  a[2:9:2]
print(a)

# IT 직무 유형 : SI(시스템통합), SM(시스템유지보수)

# 딕셔너리(사전)  : 단어-의미 구조와 유사하게 이름=홍길동 형식으로 표현
#                     딕셔너리?   키(KEY)=값(Value)의 쌍으로 표현
#                표현 예)딕셔너리 = {키:값, 키:값, ...}
# 딕셔너리는 시퀀스 객체가 아님. 데이터 참조 방법이 다름
# 키는 변하지 않는 값, 값에는 변하는 값을 표현
# 상수:문자상수(따옴표로 묶어서), 숫자상수(1,2,3,4,...)

d={'name':'kim', 'addr':'seoul', 'age':25, 'nn':['별명1', '별명2']}
#{key:value,...}, 키는 작은(큰)따옴표로 묶어서 표현, 값은 수치는 그대로, 문자는 작은(큰)따옴표로

d2={1:"hi"}
print(d2)

    # [1,10,15,20,30,70] 데이터들 사이에 연관 관계가 없음
    # 리스트(튜플) 구조로 연관 관계가 있는 데이터를 표현하기가(이해하기도) 어려움
    # ex) 게임 캐릭터 정보를 리스트로 표현
    # ['홍길동', 10, 100,20,200,50,...]

# ex) 게임 캐릭터 정보를 딕셔너리로 표현
# {'아이디': '홍길동', '레벨':10, '체력': 100, '마나':20, '공격력': 200, '방어력': 50,...}

#dic={'아이디': '홍길동', '레벨':10, '체력': 100, '마나':20, '공격력': 200, '방어력':50}
#print(dic)

c=dict(아이디='홍길동', 레벨=10, 체력=100, 마나=20, 공격력=200, 방어력=50) # dic 와 dict의 차이점
print(c)

print(zip(['a','b'],[1,2]))

print(dict(zip(['a','b'],[1,2])))   # zip 객체를 dict로 변환

c=dict(zip(['아이디','레벨','체력','마나','공격력','방어력'],['홍길동',10,100,20,200,50]))  # dic 와 dict의 차이점
# dict(zip([Key list],[Value list]))
print(c)

print(dict(zip(['a','b'],[1,2])))#zip객체를 dict로 변

c1=dic={'아이디': '홍길동', '레벨':10, '체력': 100, '마나':20, '공격력': 200, '방어력':50}
c2=dict(아이디='홍길동', 레벨=10, 체력=100, 마나=20, 공격력=200, 방어력=50) # dic 와 dict의 차이점
c3=dict(zip(['아이디','레벨','체력','마나','공격력','방어력'],['홍길동',10,100,20,200,50]))  #

# 리스트 내부에 (키, 값) 형식의 튜플로 표현
c4=dict([('아이디','홍길동'), ('레벨',10), ('체력',100), ('마나',20), ('공격력',200),('방어력',50)])
#dict([])
print(c1)
print(c2)
print(c3)
print(c4)
c5=dict({'아이디':'홍길동', '레벨':10, '체력':100, '마나':20, '공격력':200,'방어력':50})
print(c5)

# 딕셔너리 데이터 추가/삭제
a={'nn':'bear'}
print(a)
# 딕셔너리 a 에 데이터 추가

a['addr']='seoul'
# 딕셔너리 변수명[Key name]=Value
print(a)

a[100]=300
print(a)

a['hobby']=['a','b','c']
print(a)
# 100: 300 제거하기
del a[100]
print("삭제 후 :",a)
# del 딕셔너리변수명[Key] -> key와 value을 모두 제거

# 홍길동:프로그래밍, 임꺽정:분석, 이순신:딥러닝
# 이름=[홍길동,임꺽정,이순신]
# 취미=[프로그래밍,분석,딥러닝]
# print(이름[0])
# print(취미[0])

# {홍길동:프로그래밍, 임꺽정:분석, 이순신:딥러닝}
# 딕셔너리 활용 -> json 파일 포맷(웹)

# Key만 추출
print(dic.keys())   #키만 추출
print(dic.values())   #키만 추출
print(dic.items())   #모두 추출

mykey=dic.keys()
print(mykey)
#print(mykey[0])
listmykey=list(mykey)
print(listmykey)

dic={'아이디': '홍길동', '레벨':10, '체력': 100, '마나':20, '공격력': 200, '방어력':50}
dic['저항력']=111
print(dic)
print(dic['마나'])        # 추가 하고 읽고 중요해요

#   print(dic['민첩성']) # 없는 Key를 참조하려고 하면 Error!
# 딕셔너리에 키가 있는지 확인 ?
print(dic.keys())   # 어떤 Key 가 있는지 참조

print('민첩성' in dic) # 있으면 True / 없으면 False
print('마나' in dic)

print(len(dic)) # 딕셔너리 안에 있는 요소의 개수를 파악할 떄 len 함수를 이용


# 1. 리스트 생성
#2016년 11월 영화 예매 순위 기준 top3는 다음과 같습니다. 영화 제목을 movie_rank 이름의 리스트에 저장해보세요. (순위 정보는 저장하지 않습니다.)
# 순위	영화
# 1	닥터 스트레인지
# 2	스플릿
# 3	럭키
movie_rank=['닥터 스트레인지', "스플릿", "럭키"]
print(movie_rank)
# 의도 : movie_rank = ['닥터 스트레인지', "스플릿", "럭키"]
# 2. movie_rank 리스트에 "배트맨"을 추가하라.

print(movie_rank + ["배트맨"])
# 의도 movie_rank.append("배트맨")

# 3. movie_rank 리스트에는 아래와 같이 네 개의 영화 제목이 바인딩되어 있다. "슈퍼맨"을 "닥터 스트레인지"와 "스플릿" 사이에 추가하라.
movie_rank = ['닥터 스트레인지', '스플릿', '럭키', '배트맨']
a=movie_rank[0],'슈퍼맨',movie_rank[2],movie_rank[3]
print(a)
# insert(인덱스, 추가하고자 하는 데이터)
movie_rank.insert(1,"슈퍼맨")
print(a)


# 4. movie_rank 리스트에서 '럭키'를 삭제하라.
movie_rank = ['닥터 스트레인지', '슈퍼맨', '스플릿', '럭키', '배트맨']
del movie_rank[3]
print(movie_rank)


# 5. movie_rank 리스트에서 '스플릿' 과 '배트맨'을 를 삭제하라.
movie_rank = ['닥터 스트레인지', '슈퍼맨', '스플릿', '배트맨']
b=movie_rank[:2]
print(b)
del movie_rank[2]
del movie_rank[2]
# 두번 사용하면 스플릿 배트맨 삭제
num=[5,1,4,3,2]
print(max(num))     # 최대값
print(min(num))     # 최소값
print(sum(num))     # 리스트의 모든 값들의 합
print(len(num))     # 데이터의 개수 확인

avg=sum(num)/len(num)   # 평균 구하기 !!중요



# 6. price 변수에는 날짜와 종가 정보가 저장돼 있다. 날짜 정보를 제외하고 가격 정보만을 출력하라. (힌트 : 슬라이싱)
price = ['20180728', 100, 130, 140, 150, 160, 170]
# 출력 예시:
# [100, 130, 140, 150, 160, 170]
print(price[1:])



# 7.슬라이싱을 사용해서 홀수만 출력하라.
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(nums[0:11:2])

#의도 :
print(nums[::2])

# 8.슬라이싱을 사용해서 리스트의 숫자를 역 방향으로 출력하라.
nums = [1, 2, 3, 4, 5]
# 실행 예:
# [5, 4, 3, 2, 1]
print(nums[::-1])


# nums.sort()
# nums.reverse()
# print(nums)



# 9.interest 리스트에는 아래의 데이터가 저장되어 있다.
interest = ['삼성전자', 'LG전자', 'Naver']
#interest 리스트를 사용하여 아래와 같이 화면에 출력하라.
# 출력 예시:
# 삼성전자 Naver
print(interest[0],interest[2])

print(interest[::2])

# 10. interest 리스트에는 아래의 데이터가 바인딩되어 있다.
interest = ['삼성전자', 'LG전자', 'Naver', 'SK하이닉스', '미래에셋대우']
# interest 리스트를 사용하여 아래와 같이 화면에 출력하라.
# 출력 예시:
# 삼성전자 LG전자 Naver SK하이닉스 미래에셋대우
print(interest[0:])
print("/".join(interest))
# join <> split
a=("/".join(interest))
print(a.split("/"))

# 11. interest 리스트에는 아래의 데이터가 바인딩되어 있다.
interest = ['삼성전자', 'LG전자', 'Naver', 'SK하이닉스', '미래에셋대우']
# join() 메서드를 사용해서 interest 리스트를 아래와 같이 화면에 출력하라.
# 출력 예시:
# 삼성전자
# LG전자
# Naver
# SK하이닉스
# 미래에셋대우
print("\n".join(interest))
#
# 12. 리스트에 있는 값을 오름차순으로 정렬하세요.
data = [2, 4, 3, 1, 5, 10, 9]
data.sort()
print(data) #data 변수에는 정렬된 결과가 저장됨

data = [2, 4, 3, 1, 5, 10, 9]
print(sorted(data))
print(data)     # data 변수에는 정렬 전의 data가 그대로 저장됨

# 짝수 or 홀수 파악하기 함수 : 2로 나눈다.
x=3
x%2
print(x%2)

# 13.
# 홍길동 씨의 주민등록번호는 881120-1068234이다. 홍길동 씨의 주민등록번호를 연월일(YYYYMMDD) 부분과 그 뒤의 숫자 부분으로 나누어 출력해 보자.
# ※ 문자열 슬라이싱 기법을 사용해 보자.
id="881120-1068234"
print('연월일:',id[:6],",", id[7:])



# 14
# (1,2,3) 튜플에 값 4를 추가하여 (1,2,3,4)를 만들어 출력해 보자.
# ※ 더하기(+)를 사용해 보자.
t=(1,2,3)
t+=(4,)
print(t)


# 15
# 다음과 같은 딕셔너리 a가 있다.
a = dict()
a
{}
# 다음 중 오류가 발생하는 경우를 고르고, 그 이유를 설명해 보자.
a['name'] = 'python'
print(a)
a[('a',)] = 'python'
print(a)
a[250] = 'python'
print(a)
# 딕셔너리의 키는 변하지 않는 값을 사용

# a[[1]] = 'python' # 오류 : Key에는 가 올수 없다.


# 16
# 딕셔너리 a에서 'B'에 해당되는 값을 추출해 보자.
a = {'A':90, 'B':80, 'C':70}
# ※ 딕셔너리의 pop 함수를 사용해 보자.
print(a.pop('B'))



