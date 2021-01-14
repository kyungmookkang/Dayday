'''
# 회문 : 유전자 염기서열 분석 ..
# n-gram : 언어패턴
'''

# 1. map(함수, 자료)

def twoTimes(n):
# #1
# a = []
#     for i in n:
#         i = i*2
#         a.append(i)
#     return a
    # 구현
#2
    return [2*i for i in n]
res = twoTimes([1,2,3])
print(res)

# map 활용
def twoTimes(n):
    return n*2
res = list(map(twoTimes, [1,2,3]))
print(res)

# 3. pow 함수

print(pow(3,2))  # pow(a,b) a의 b승 : 9

# 4. 자리올림
print(round(3.141592, 4))   # 소수이하 4째 자리까지 출력(5번째 자리에서 반올림함)

# 5. zip 함수
print(zip([1,2], [3,4], [5,6], [7,8])) # : 1 3 5 7 / 2 4 6 8  list 로 묶어줘야 볼 수 있음
print(list(zip([1,2], [3,4], [5,6], [7,8])))

# 6. filter : 트정 조건으로 걸러진 요소들을 묶어서 리턴, map과의 차이점이라면, 함수의 결과가 참/거짓 인지에 따라 요소를 포함할지를 결정

t = list(range(1,11))
print(t)
# 짝수 리스트를 출력
# 1. for
def isEven(n):
    return True if n % 2 == 0 else False
res = []
for v in t:
    if isEven(v):
        res.append(v)
print(res)

#2. filter
print(list(filter(isEven, t)))

#3. lambda
print(filter(lambda x: x%2 ==0, t))


# OS 모듈 : 디렉토리, 파일의 경로 등 확인/제어
import os
print(os.environ)

print(os.getcwd())  # current working directory
# os.mkdir('sample.py')
# os.rmdir('sample.py')
# os.rename("sample", "Test")
# os.rename("day9.py", "web2.py")




