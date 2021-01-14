dic = {
    '.-':'A','-...':'B','-.-.':'C','-..':'D','.':'E','..-.':'F',
    '--.':'G','....':'H','..':'I','.---':'J','-.-':'K','.-..':'L',
    '--':'M','-.':'N','---':'O','.--.':'P','--.-':'Q','.-.':'R',
    '...':'S','-':'T','..-':'U','...-':'V','.--':'W','-..-':'X',

    '-.--':'Y','--..':'Z'}



def morse(src):
    res = []
    for word in src.split("  "):  # word 에는 단어가 저장, 입력된 문장에 저장된 단어 3개
        for c in word.split(" "):   # c에는 문자가 저장
            res.append(dic[c])
        res.append(" ")   # 단어와 단어가 공백문자로 구분
    return  "".join(res)

print(morse('.... .  ... .-.. . . .--. ...  . .- .-. .-.. -.--'))

def ngram(s, num):
    res = []
    slen = len(s)-num +1
    for i in range(slen):
        ss = s[i:i+num]
        res.append(ss)
    return res

def diff_ngram(sa, sb, num):
# #a=ngram(sa, num)
# b=ngram(sb, num)
# print(a)
# print(b)
#     ['오늘', '늘 ', ' 멀', '멀티', '티캠', '캠퍼', '퍼스', '스에', '에서', '서 ', ' 너', '너무', '무 ', ' 쉬', '쉬운', '운 ', ' 프', '프로', '로그',
#      '그래', '래밍', '밍을', '을 ', ' 공', '공부', '부했', '했다']
#     ['멀티', '티캠', '캠퍼', '퍼스', '스에', '에서', '서 ', ' 공', '공부', '부했', '했던', '던 ', ' 오', '오늘', '늘의', '의 ', ' 프', '프로', '로그',
#      '그래', '래밍', '밍은', '은 ', ' 너', '너무', '무 ', ' 쉬', '쉬웠', '웠다']
# cnt =0  #일치한 단어의 개수를 저장하기 위한 변수
# r = [] # 일치한 단어를 저장하기 위한 변수
# for i in a:
#     for j in b:
#         if i==j:   # 두 단어 (i,j)가 일치한다면
#             cnt+=1
#             r.append(i)
# return cnt/len(a), r
#
#







