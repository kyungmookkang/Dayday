# import re
# if re.match("\d{4","12345"):
#     print("정상 전화번호")
# else:
#     print("비정상 전화번호")
#
#
# # re.sub("패턴","바꿀문자열","문자열",바꿀횟수)
# print(re.sub("apple|orange", "fruit","apple tree banana orange"))
#
# "1 2 apple 3 banana 4 7 9 30tree"
# # 수치데이터 => "num"으로 변경
#
# print(re.sub("[0-9]+", "num","1 2 apple 3 banana 4 7 9 30 tree"))
# print(re.sub("[0-9]+", "num","1 2 apple 3 banana 4 7 9 30 tree", 3))
# print(re.sub("\d+", "num","1 2 apple 3 banana 4 7 9 30 tree"))
# # [0-0]:\d, 공백/탭/엔터문자:\s, 문자/숫자:\w        # 공식
#
# print("="*50)
#
# pat = re.compile("apple|orange")
# pat.sub("fruit","apple tree banana orange")
# print(pat.sub("fruit","apple tree banana orange"))
# '''
#
#
#
# url = "https://www.multicampus.com/img/saas/main/logo/CUS0001/pc_main.png"
# urllib.request.urlopen(url).read()
# with open("test.png", "wb") as f:
#     f.write(mem)
#     print("저장되었습니다")
#
# 웹에서 사용하는 언어
# - Server, Client 간에 데이터를 주고 받을 때 사용하는 언어
# Client(페이지 요청, 웹브라우저에 www.naver.com) -> Web Server -> 메인페이지 제공(index.html) ->
# XML : Extensible Markup Language
# HTML : Hyper Text Markyp Language
#
# * 동적 페이지 : 클릭할 떄 마다 다르게 나타남 : jsp, asp, php 등
# * 정적 페이지 : 변하지 않는 내용에 해당함
# 구조화된 문서(xml) - 정적 페이지에 해당
# 비구조화된 문서(html) - 정적 페이지에 해당
#
#
#
# 클라이언트(날씨 클릭) -> 웹서버(날씨 페이지(동적,jsp) 생성) -> 생성된 페이지를 html 형식의 문서로 만들어 제공
# -> 웹브라우저 해석-> 결과를 화면에 출력
# 출력 : 오늘의 날씨는 맑습니다. 기온은 섭씨 영하 2도입니다.
#
#
# import ssl
# context = ssl._create_unverified_context()
# url = "https://www.multicampus.com/img/saas/main/logo/CUS0001/pc_main.png"
# mem = urllib.request.urlopen(url, context=context).read()
# # mem = urllib.request.urlopen(url).read()
#
# urllib.request.urlretrieve(url, "test.png")
# print("저장되었습니다")
#
# '''
# #
# # import ssl
# # context = ssl._create_unverified_context()
# # import urllib.request
# # url = 'https://www.multicampus.com/img/saas/main/logo/CUS0001/pc_main.png'
# # urllib.request.urlretrieve(url , 'test.png')
# # mem = urllib.request.urlopen(url , context=context).read()
# # with open('test2.png' , 'wb') as f:
# #     f.write(mem)
# # print('저장되었습니다')
#
# import ssl
#
# context = ssl._create_unverified_context()  # MAC 용 ! 이거 없으면 안된다
# #https://www.multicampus.com/img/saas/main/logo/CUS0001/pc_main.png
# import urllib.request
# url = 'https://www.multicampus.com/img/saas/main/logo/CUS0001/pc_main.png'
# # urllib.request.urlretrieve(url , 'test.png')
# # print('저장되었습니다')
#
# mem = urllib.request.urlopen(url , context=context).read()
# with open('test2.png' , 'wb') as f:
#     f.write(mem)
#     print('저장되었습니다')
#
# # http://www.weather.go.kr/weather/forecast/mid-term-rss3.jsp
#
#
# # >검색어 : 노래 제목, 멤버들 ,...
# # 비구조화된 문서 : 웹페이지 내용에 대해 기계가 해석하지 못하는 문서 -> 검색어를 기반으로 검색
# # ex) 방탄이 서울 강남구에서 공연을
# # print(했습니다)
# # 구조화된 문서 : 웹페이지 내용에 대해 기계가 해석 가능한 문서 -> 검색어의 의미를 기반으로 검색
# # -> 검색 폭 넓음,검색 결과에 대한 정확도 높음
# # <가수>
# #     <그룹명>BTS</그룹명>
# #     <도시이름>서울</도시명>
# #     <구이름>강남구</구이름>
# #     <멤버이름> ....</멤버이름>
# # </가수
#
# import urllib.parse as parse
# import urllib.request as request
# addr = "http://www.weather.go.kr/weather/forecast/mid-term-rss3.jsp"
# values = {'stdID':'109'}
#
# params = parse.urlencode(values)
# url = addr+"?"+params
# print(url)
#
# data = request.urlopen(url).read()
# data = data.decode('utf-8')
# print(data)
#
# # <a>
# # <b>
# #
# # </b>    # 꼭 b 부터 나와야한다.!!!!!!
# # </a>
#
# # 제주시의 1월 16일 자정 온도
#
# # 웹스크래핑 : BeautifulSoup패키지
#
# from bs4 import BeautifulSoup
#
# html ="""
# <html><body>
# <h1>스크레핑</h1>
# <p>웹 페이지 분석</p>
# <p>원하는 부분 추출</p>
# </body></html>
# """
# # 붕어빵봉토 = 붕어빵기계(크림,10센치)
# # soup=BeautifulSoup(html, "html.parser")
# # # 클래스
# # print(soup.html.body.h1.string)
# # p1 = soup.html.body.p
# # # print(soup.html.body.p.string)
# # # p2 = p1.next_sibling  # 줄바꿈 문
# # # print(p2.next_sibling.string)
# # # p2 = p1.next_sibling.next_sibling.string
# # print(p2)
# #
# # soup = BeautifulSoup(html2, "html.parser")
# # print(soup.find(id='title').string)
#
# html3="""
# <html><body>
# <ul>
# <li><a href = "http://www.naver.com">naver</a></li>
# <li><a href = "http://www.daum.net">daum</a></li>
# </ul>
# </body></html>
# """
# soup = BeautifulSoup(html3, "html.parser")
# print(soup) # 문자열 -> html파서로 분석할 수 있는 객체로 변환
# print(html3) #문자열을 저장하고 있는 변수
# # <태그명 속성명 = 속성값 속성명=속성값...>
#
# print(soup.find_all("a"))
# # print(html3.find_all("a"))
#
# links = soup.find_all("a")
# # print(html3.find_all("a"))
#
# for i in links:
#     href = i.attrs['href']
#     na = i.string
#     print(na, "-->", href)
#
#
# html4="""
# <p><a href = "aaa.html">aaa page</a></p>
# """
# soup = BeautifulSoup(html4, "html.parser")
# print(soup.p.a.string)
# print(soup.a.string)
# print(soup.a.attrs)
# mydict = soup.a.attrs
#
# print('href' in mydict)
# # if 'href' in mydict:
# #     ..
# # else:
# #     ..
# import urllib.request as req
#
# url = "http://www.weather.go.kr/weather/forecast/mid-term-rss3.jsp"
# res = req.urlopen(url)
# # print(res)
#
# # 정상응답 -> 200:ok
# # 문서를 찾지 못한 경우 -> 40x
# # 서버 자체 오류 -> 50x
# soup = BeautifulSoup(res,"html.parser")
# # print(soup)
# #
# # print("문서제목:",soup.title.string)
# # print(soup.find("title").string)
# # print(soup.find_all("title")[0].string)
#
# # 모든 wf태그의 내용을 출력
# # print(soup.find("wf").string)
# # print(len(soup.find_all("wf"))) #534개
#
# from bs4 import BeautifulSoup
#
# html = """
# <html><body>
# <div id="lang">
#     <h1>프로그래밍언어</h1>
#     <ul class="items">
#         <li>python</li>
#         <li>java</li>
#         <li>cpp</li>
#     </ul>
# </div>
# </body></html>
# # """
# # soup = BeautifulSoup(html4, "html.parser")
# # # print(soup.select("div#lang > h1")[0].string)
# #
# # # print(soup.select_one("div#lang > h1").string)
# # mylist = (soup.select("div#lang > ul.items > li"))
# # # print(soup.select_one("div#lang > ul.items > li"))
# # for i in mylist:
# #     print(i)
#
#
# ##################
# # Quiz
# # print(soup.a.attrs.values())
#
# # def once(a):
# #     if len(x) ==10:
# #         for i in range(10):
# #             if str(i) in x:continue
# #                 else:
# #                     print("false")
# #                     print("true")
# #                 else:
# # once("123414575670")
#                     print("false")

news="""
연합뉴스TV

[날씨] 추위 대신 미세먼지 말썽…밤까지 중부 중심 눈

기사입력 2021.01.12. 오후 1:40 기사원문 스크랩 본문듣기 설정

화나요 후속기사원해요 좋아요 평가하기9 댓글9

글자 크기 변경하기

인쇄하기 

보내기

동영상 뉴스
[앵커]
오늘은 추위가 풀리는 대신 서쪽 지역의 공기 질이 나쁘겠습니다.
중부지방을 중심으로 눈도 내리겠습니다.
기상캐스터 연결해서 날씨 정보 더 자세히 알아보겠습니다.
김민지 캐스터.
[캐스터]
네, 추위가 한층 풀렸습니다.
어제보다 옷차림을 조금 더 가볍게 하고 나왔는데도 크게 춥지 않습니다.
내륙에 내려졌던 한파특보는 모두 해제가 됐고요.
오늘 한낮에 전국에 영상권으로 올라서겠습니다.
한낮에 서울은 1도, 대전 3도, 대구 5도 등 어제보다 5도 정도 기온이 높겠습니다.
따뜻한 서풍이 불어오면서 추위의 힘이 약해지는 건데요.
이 서풍을 타고 또 미세먼지가 들어오겠습니다.
대기 정체로 먼지가 쌓이면서 오늘은 서쪽 지역을 중심으로 미세먼지 농도 나쁨 수준 보이겠고요.
밤에 중국발 오염물질까지 들어와서 내일은 전국적으로 공기 질 상황이 나쁘겠습니다.
오늘 전국에 구름이 많습니다.
차츰 중부를 중심으로 눈이 내리겠습니다.
수도권과 충남, 전북에 1~3cm, 강원 영서와 충북, 경북과 제주 산지에 최고 5cm의 눈이 내려 쌓이겠습니다.
대부분 오늘 밤이면 그칠 텐데요.
강원 영서 지역은 내일 새벽까지 눈이 이어지겠습니다.
지금은 눈발 정도만 날리고 있습니다.
눈이 쌓이면서 퇴근길 무렵에는 길이 많이 미끄럽겠습니다.
조심히 이동하시기 바랍니다.
날씨 전해 드렸습니다.

"""
import re

# 3.1)[캐스터]가 캐스팅한 내용만 추출하시오
print(re.search('\\[캐스터\\][a-zA-Zㄱ-ㅎ가-힣0-9,.~\n ]+',news).group())
# 3.2)달린 댓글의 개수를 출력하시오
print(re.search('댓글\d+', news).group())
# 3.3) 대전의 온도를 출력하시오
print(re.search('대전 \d+도',news).group())
# 3.4) 가장 많이 등장한 단어가 무엇인가요? (공백기준)
li = news.split()
word_count = {}
for i in li:
    count = li.count(i)
    word_count[i] = count
print([(x,v) for x,v in word_count.items() if max(word_count.values()) == v])
'''
1.0~9의 문자로 된 숫자를 입력받았을 때, 이 입력값이 0~9의 모든 숫자를 각각 한 번씩만 사용한 것인지 확인하는 함수를 작성하시오.


입력 예시: 0123456789 01234 01234567890 6789012345 012322456789
출력 예시: True False False True False







1. IT기업 코딩 테스트문제
주어진 문자열(공백 없이 쉼표로 구분되어 있음)을 가지고 아래 문제에 대한 프로그램을 작성하세요.

이유덕,이재영,권종표,이재영,박민호,강상희,이재영,김지완,최승혁,이성연,박영서,박민호,전경헌,송정환,김재성,이유덕,전경헌

김씨와 이씨는 각각 몇 명 인가요?
"이재영"이란 이름이 몇 번 반복되나요?
중복을 제거한 이름을 출력하세요.
중복을 제거한 이름을 오름차순으로 정렬하여 출력하세요.

2. 토지 원고 데이터
1) 저자명 추출
2) 제목 추출
3) 출판사명 추출
4) 인용부호(큰 따옴표)로 묶여있는 내용을 모두 추출하여 리스트에 저장
5) 토지 원고 전체에서 한글에 해당되는 내용만 추출하여 저장, 가장 많이 사용된 단어
100개를 출력
6) 각 장의 제목 저장 및 출력

'''