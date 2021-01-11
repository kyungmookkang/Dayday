# 정규표현식 : 복잡한 문자열 처리(Life is too short ~)
# 스크래핑 : 데이터 긁어오기 / 웹에서 필요한 정보 추출

jumin="""
park 850101-1234567
kim 950202-2345678
"""
import re # regular expression (정규 표현식 모듈)
p = re.compile("(\d{6})[-]\d{7}")    # 정규식 작성
print(p.sub("\g<1>-*******", jumin))

 # 정상적인 주민번호에 대한 일반적인 규칙을 정의(숫자6자리 - 숫자7)


# print(jumin)
# # park 850101-*******
# # kim 950202-*******
#
# # error 방지
# s = 'pithon'
# print(s)
# print(s[0] + "y" + s[2:])
#
# for line in jumin.split("\n"):
#     for word in line.split(" "):
#         if len(word) ==14 and word[:6].isdigit() and word[7:].isdigit():
#             word = word[:6] + "-" + "*******"
#             print(word)
# # print(jumin.split("\n"))
#
# d = "1234"
# print(d.isdigit())

jumin="""
park 850101-1234567
kim 950202-2345678
"""
import re # regular expression (정규 표현식 모듈)
p = re.compile("(\d{6})[-]\d{7}")    # 정규식 작성
print(p.sub("\g<1>-*******", jumin))
# 정상적인 주민번호에 대한 일반적인 규칙을 정의(숫자6자리 - 숫자7)

# re.match("패턴", "문자열")   # 문자열이 패턴에 부합되나요 ?
print(re.match("hello","hello, world"))# 문자열에 hello 문자열이 있는지 판단
# 출력(매치됨) : "hello, world"  <re.Match object; span=(0, 5), match='hello'>

print(re.match("hi","hello, world"))
# 출력(매치안됨) : None

if re.match("hello","hello, world"):    #None 은 거짓
    print("주어진 hello, world 문자열 hello(문자열)패턴에 매치 됐습니다.")
else:
    print("매치되지 않았습니다")

print(("hello, world".find("hello")))

# 특정 문자열이 맨앞/뒤 오는지 판단?
# 문자열 맨 앞에 ^를 붙이면 맨 앞에 오는지 판단
#  "   끝에 $를    "   끝   "

print(re.search("^hello", "hello, world"))  # hello로 시작하는지 확인
print(re.search("world$", "hello, world"))  # world로 끝나는지 확인

# hello 또는 world 문자열이 포함되어 있는지 확인
print(re.match("hello|world", "hello"))
print(re.match("hi|world", "hello"))

# 정규표현식 메타문자 (메타 : 정보의 정보, 데이터(예- 전화번호부)의 데이터(색인, ...)
# 매타문자 종류 : ( ) { } [ ] \ | ? + * $ ^ ...
"""
[ ] 메타문자 :
대괄호 안에는 어떤 문자도 올 수 있음

ex) [abcdef] 의미? a,b,....,f 중에서 어떤 한 개의 문자와 매치
'a' 문자는 정규표현식에 매치됨
"""
print(re.match("[abcdef]", "a"))    # 매치
print(re.match("[abcdef]", "z"))    # 매치 안됨
print(re.match("[abcdef]", "abc"))  # 매치 됐지만 a 매치 후 멈춤
print(re.match("[abcdef]", "c"))   # 매치됨

print(re.search("my", "hello, my world"))   # 매치됨
print(re.match("my", "hello, my world"))   # 첫 글자부터 안되면 짤 - None

# [from - to]
# [a-d] 정규식 의미 : [abcd], [a-f]==[abcdef]
# [0-5] == [012345]

print(re.match("[0-9]", "1234")) # 1234는 0~9까지 숫자에 해당
print(re.match("[0-9]*", "1234")) # 1234는 0~9까지 숫자에 해당-, *은 문자(숫자)가 0개 이상 있는지 확인
print(re.match("[0-9]*", "a1234")) # a1234에서 a는 [0-9] 범위가 아님. 원래는 None이 나와야함, 그러나 *이 있으므로 0개도 매칭이 된 것으로 출력

print(re.match("[0-9]+", "1234")) # 1개 이상 있는지 확인
# [a-z], [A-Z], [a-zA-Z], [^0-9] : 0~9(숫자)를 제외한 문자 (^ = not)
# search 는 전체영역 / match는 왼쪽 부터 점검 해서 처음에 안맞으면 짤

print(re.search("^hi", "hello, hi"))     #무자열이 hi로 시작해야 함 (시작하지 않으므로 None)
print(re.search("hi", "hello, hi"))  # <re.Match object; span=(7, 9), match='hi'>
print(re.match("hi", "hello, hi"))  # None

print(re.match("hello|hi|good", "goodhi"))
print(re.match("[0-9]", "12a3bcd"))
print(re.match("[0-9]*", "a12a3bcd"))    # 숫자가 0개 이상 있는지 판단
print(re.match("[0-9]+", "a12a3bcd"))    # 숫자가 1개 이상 있는지 판단

print(re.match("ab","abc"))
print(re.match("ba","abc"))

print(re.match("a*b", "bb"))     # a문자가 0개 이상 있고 b가 나오면 매치
print(re.match("a+b", "ab"))    # a문자가 1개 이상 나와야하고 반드시 b가 그 뒤로 나와야함.
print(re.match("a+b", "aaaaaaab"))
print(re.match("a+cb+", "aaaaaaaaaaacbbbbbbbbb"))
print(re.match("a+b*","aaaaaaabbbbbcccc"))
# 패턴이 문자열에 있느지만 보면 됨(문자열이 패턴을 반드시 가지고 있어야함)




