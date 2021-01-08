def madd(a,b):
    return a+b

def msub(a,b):
    return a-b
'''
mod1.py를 실행시키면 __name__이라는 특별한 속성의 값으로
__main__이 저장됨
따라서 if __name__ == "__main__: 조건식이 참이 됨'''
if __name__ == "__main__":      # 이것만 작성하면 된다!!!!!!!!!
    print("__name__ 값 :", __name__)
    print(madd(3,2))    #5
    print(msub(10,3))   #7
else:
    print(("__name__ 값 :", __name__))