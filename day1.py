

    # 파이썬 ?
    # 매우 인간적인 언어
    # 프로그래밍(언어 : 파이썬, 씨, 자바 ... => 프롣그램(application, app)
    # 프로그래밍 ?
    # 우리의 생각을 컴퓨터에 지시하는 행위


    # 텍스트에 주석 입히기
    # 블록 설정 => command + / => 블록 전체가 주석(참고문)으로 간주됨

print("hi")
    # 기본 프로그램 실행시 : control + r

    # 리스트 [], 튜플 (), 딕셔너리, 셋 :{}

if 4 in [1, 2, 3, 4] : print("4가 있어요")

languages = ['python', 'perl', 'c', 'java']
# 변수 = 데이터  =>  데이터를 변수에 저장해라라

for lang in languages:         # for = 반복해라 !
    if lang in ['python', 'perl']:         # if = 첫 번째 조건
        print("%6s need interpreter" % lang)
    elif lang in ['c', 'java']:            # elif = 첫 번째 조건이 성립하지 않을 때, 두 번째 조건
        print("%6s need compiler" % lang)
    else:                                  # else = 첫째, 둘째 조건 외의 모든 것들
        print("should not reach here")

# 유틸리티, GUI(Graphic User Interface), Web, DB, 데이터분석(파이썬으로 하는 것이 아니라, 파이썬에 추가적으로 설치한 패키지로 ex)pandas)

# import pandas as pd

print('hello, world');print('bye')

a = 1 # assign (할당, 왼쪽 <= 오른쪽)
a = 1+2 # 더해라

# 파이썬에서는 들여쓰기가 중요

# basckspace key : 엔터키 위에, tab
if a==4:
    print('4')
    print('four')
print("코드블록 밖")


#코드블록 : 들여쓰기를 동일한 코드 집합

print(5/3)

print(5//3) # 몫만 나온다 (소수점 이하는 버리는 연산 //)
print(6//3) #2
print(6//3.0) #2.0

print(7 % 4) # 몫을 제외한 나머지 연산자
print(2 ** 3) # 거듭제곱

print(2 ** 1000) #2의 1000승

print(int(3.3))  # int 는 값을 정수로 만들어주는 함수
print(int(5/2))
print('10') # 일영 이라고 읽음
print(int('10')+2) #문자열 일영 => 숫자 10 변환 => 더하기 2 => 12

print(type(10)) # type 10이라는 자료형은 무엇입니까?
print(type('123'))

print(divmod(9, 4)) #9를 4로 나눈 몫과 나머지 => (2, 1) (몫, 나머지)
      # 함수(인수1, 인수2)

res=divmod(9, 4) # res= (2, 1) 튜플 1개, 요소 2개(몫, 나머지)
print(res)
print("결과:", res)
print("1번째 요소 : ", res[0]) #res 튜플에 저장된 1번째 요소값을 출력
print("2번째 요소 : ", res[1]) #res 튜플에 저장된 2번째 요소값을 출력

# 튜플(리스트)에서 데이터의 위치는 0번 부터 시작한다.

res1, res2 = divmod(9, 4)   # 변수를 왼쪽에 2개를 주면 자동으로 대입을 한다. 몫과 나머지를 구분하기 편하다.

print("1번째 요소 : ", res1)
print("2번째 요소 : ", res2)

# 10진수 : 0~9
# 2진수 : 0~1
# 8진수 : 0~7
# 16진수 : 0~9abcdef

#a+1 -> b+2 -> d+2 -> f+1 = 10 ...

print(11) #11, 10진수
print(0b11) #3, 2진수
print(0o10) #8, 8진수

print(5)
print(float(5))

print(float('3.14')*2)
print(type(3.14))

print("Kang's laptop")

print('he said, "how are you?"')

# " / ' 함께 사용하면 안된다. 구분해서 사용할 것!

print("안녕 \n\n 반가워요 \n 잘있어요")  # \n 은 줄 바꿈 (newline)

print("안녕")
print("반가워요")
print("잘있어요")

print("안녕 \t 반가워요 \n 잘있어요")  # \t 은 tab

# naver$daum$samsung
print("naver", "kakao", "samsung") # 공백으로 연결되어 출력
print("naver", "kakao", "samsung", sep="$") # sep = separated 공백 대신 입력값 출력

print('안녕'); print('하세요')

print('안녕', end=""); print('하세요') # end 연결 시, 사용! 끝나는 부분을 강제로 출력

print('안녕', end=" "); print('하세요')

a=1
b=2
c=3
# = 위의 식과
a, b, c= 1, 2, 3

print(a, b, c)

a=b=c=d=1
print(a,b,c,d)

x,y=1,2

print(x,y)
print(y,x)

a=1 # 메모리에 a라는 공간을 만들고, 1을 저장해라
print(a)

# 메모리에 있는 변수를 제거
del a
# print(a) 에러가 뜬다.

# 변수만 만들고 값을 저장하고 싶지 않은 경우
b=None # 사과바구니 자체가 없음
# print(b)
# b=''  # 사과바구니에 사과가 없음
#
# x=10
#
# x+=10  # x=x+10  축약형 연산자
#
# x=x-5 # x-=5

#입력을 받은 뒤 엔터 키를 누르면 다음 문장으로 이동

# input()
# x=input("출력하고 싶은 값을 입력해주세요.")
# print("당신이 입력한 값은 : ", x)

# x=input("첫 번쨰 수 입력 :")
# y=input("두 번쨰 수 입력 :")
# print("덧셈 결과는", x+y)

# input 함수로 입력받은 모든 데이터는 '문자'로 간주

# x=int(input("첫 번쨰 수 입력 :"))
# y=int(input("두 번쨰 수 입력 :"))
# print("덧셈 결과는", x+y)
# 덧셈 결과로 만드려면 ?  int 함수는 변수를 정수로 만들어준다.

# x=float(input("첫 번쨰 수 입력 :"))
# y=float(input("두 번쨰 수 입력 :"))
# print("덧셈 결과는", x+y) # float 함수는 변수를 실수로 만들어준다.

# a,b=input("두 수를 입력하세요 :").split() #3 2 -> error -> .split() 공백으로 나눈다
# print(a)
# print(b)

# .split()  : 앞에 있는 함수를 공백으로 분리해주는 함수

# 문제 1. 숫자 두 개 입력 : 1 2 (엔터) -> 3 출력하도록 프로그래밍



# # x,y=input("숫자 두 개 입력 : ").split()
# print(int(x)+int(y))

# mapping : 사상 x -> f -> y

# 함수 출력 = map(함수, 함수 입력)

# x1, x2=map(int, input("숫자 두 개 입력 :").split(","))
# "1,2" -> ['1,', '2'] -> [1,2] -> x1=1, x2=2
# print(x1+x2)

# x='hello'
x="""인생은 짧다, 그랫거 파이썬이 필요하다."""

print(x)

a="python"
print(a*3)

x="life is too short"
print(len(x))
print(x[0])  # 위치(인덱스)는 0부터 시작

# 인덱싱 : 변수에 저장된 문자열에 대해 위치를 지정하여 참조하는 행위
print(x[-1])   # -기호는 뒤에서부터 참조

print(x[-3])

print(x[5:7]) # 범위 지정하여 슬라이싱 [시작위치 : 끝위치+1]
# 5<= x <7

# short?
print(x[12:18])
print(x[12:]) # 끝위치를 지정하지 않으면, 문자열의 마지막까지 참조
print(x[:5])    # 맨 앞에서부터 5-1:4번 인덱스까지 출력

print(x[:]) # 전체
print(x)

print(x[8:-3])

# "20201229" =>년/월/일


# print(x)
# print(x[1])
#
# x[1]="y"  # error : 문자 . 문자열의 요소값은 변경이 안된다
x="pithon"
x=x[0:1]+"y"+x[2:]
print(x)

x=5
print("I had %d eggs" % x) # 문자열 포매팅, %d (decimal십진수)

x="four"
print("I had %s eggs" % x) # 문자열 포매팅, %s (string문자열)

x="ten"
d=3
per=30
print("I had %s eggs, so I was full for %d days. %d%%" % (x, d, per)) # 괄호로 묶어줘야한다.!!!!
# %f : 실수


# 연습문제
# 1. 첫 번째와 셋 째 문자를 출력하세요.
letters = 'python'
letters
print(letters[0]+letters[2])

# 2.뒤에 4자리만 출력하세요.
cn="24가 2210"
print(cn[-4:])

# 3. 문자열에서 '파' 만 출력하세요.
s = "파이썬파이썬파이썬"
# print(s[0]+s[3]+s[6])

# 다른 해답
print(s[:])  #offset : 몇 칸을 건너뛸 것인지, 양수(좌->우), 음수(우->좌)
print(s[::3])
print(s[::-1])

s = 'python'
print(s[::-1])  # 뒤에서부터 읽기 offset!

tel = "010-3292-1234"
# 데이터수집 -> 전처리 -> 분석 ->..
# 숫자만 추출하기
# replace 함수!: 문자(열) 치환     replace(from, to)
print(tel.replace("-",""))



# 4.문자열 '720'를 정수형으로 변환해보세요.
num_str = "720"
print(int(num_str))


# 5. 문자열 "15.79"를 실수(float) 타입으로 변환해보세요.
data = "15.79"
print(float(data))


# 6. 에어컨이 월 48,584원에 무이자 36개월의 조건으로 홈쇼핑에서 판매되고 있습니다. 총 금액은 계산한 후 이를 화면에 출력해보세요.
month = 48584
print(month*36, "원")
























