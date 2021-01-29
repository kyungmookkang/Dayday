# # id 를 이용한 다양한 데이터 참조 방
import urllib
#
from bs4 import BeautifulSoup
# # fp = open("lang.html", mode="r")
# # soup = BeautifulSoup(fp, "html.parser")
# # print(soup)
# # print("="*50)
# # print(soup.select_one("ul > li"))
# # print("-"*50)
# # print(soup.select("ul > li"))   #리스트
# #
# # # python 추출하기 feat. select_one
# # print(soup.select_one("ul > li#py"))    # id가 py인 데이터 추출 #을 이용
# # print(soup.select_one("#py"))    # 선택자(selector)
# # print("-"*50)
# # print(soup.select_one("ul#language > li#py")) # 복잡한 과정이나 이해를 높이기 위한 표현
# # print(soup.select_one("#language > #py"))
# # print(soup.select_one("#language #py"))
# # print(soup.select_one("li[id='py']"))
# # print("-"*50)
# # print(soup.select_one("li:nth-of-type(3)"))
# # print(soup.select("li")[2].string)
# # print("-"*50)
# # print("-"*50)
# print("-"*50)
#
# # 네이버 달러 환율 정보 가져오기
# # import ssl
# # context = ssl._create_unverified_context()
# # import urllib.request
# # req = urllib.request.urlopen(ssl, context=context).read()
# # import urllib.request as req
# # url = "https://finance.naver.com/marketindex/?tabSel=exchange#tab_section"
# # res = req.urlopen(url)
# '''
# # import ssl
# # context = ssl._create_unverified_context()  # MAC 용 ! 이거 없으면 안된다
# import ssl
# ssl._create_default_https_context = ssl._create_unverified_context
#
# import urllib.request as req
# url = "https://ko.wikisource.org/wiki/%EC%A0%80%EC%9E%90:%EC%9C%A4%EB%8F%99%EC%A3%BC"
# res = req.urlopen(url)
# soup = BeautifulSoup(res, "html.parser")
# print(soup.select_one("#mw-content-text > div.mw-parser-output > ul:nth-child(6) > li > b > a").string)
#
# mylist = soup.select("#mw-content-text > div.mw-parser-output > ul:nth-child(6) > li > ul > li")
# for li in mylist:
#     print(li.string)
# # print(len(mylist))
# '''
# # fp=open("fruits-vegetables.html")
# # soup = BeautifulSoup(fp, "html.parser")
# # print(soup.select("div"))
# # print(soup.select("li"))
# #
# # print(soup.select("li.black")[1].string)
# #
# # print(soup.select("#ve-list > li:nth-of-type(4)")[0].string)
# # print(soup.select("#ve-list > li"))
# #
# # dic = {"data-lo":"us", "class":"black"}  # {속성명:속성값,...}
# # print(soup.find("li")) #find함수 == select_one함수, findAll==select함수
# #
# # print(soup.findAll("li",dic))
# # print(soup.find("li",dic))
# #
# # print(soup.find(id="ve-list").find("li", dic).string)
#
# # Selenium : 웹 브라우저를 제어하는 프로그램
# import ssl
# ssl._create_default_https_context = ssl._create_unverified_context
#
# # pip install selenium
#
# # # # 크롬드라이버를 다운로드 받아 설치
# # # # chromedrive는 크롬 웹브라우저를 제어하는 프로그
# # # driver = webdriver.Chrome("coolmuk/scrap/chromedriver.exe")
# # driver = webdriver.Chrome("/Users/coolmuk/chromedriver")
# # from selenium import webdriver  # 중요1
# # driver=webdriver.Chrome("/Users/coolmuk/chromedriver")  # 중요하다
# # url="https://naver.com"
# # driver.get(url)
# # html = driver.page_source
# # print(html)
#
# # 멜론 실시간 인기 차트 곡 수집
# # url = "https://www.melon.com/chart/index.htm"
# # driver.get(url)
# # html = driver.page_source
# # # print(html)
# # soup = BeautifulSoup(html, "html.parser")
# # # print(soup)
# # songs = soup.select("tr")[1:]
# # # print(len(songs))
# # song = songs[2]
# # print(song)
# # title = song.select("a")
# # # print(title)
# #
# # print("="*50)
# # for song in songs:
# #    print("song:", song.select("div.ellipsis.rank01 > span > a")[0].stirng)
#
# # 인스타그램 클롤링(제주도맛집)
#
#
# # 네이버 - 강아지 - 이미지 주소
# # https://search.naver.com/search.naver?where=image&sm=tab_jum&query=%EA%B0%95%EC%95%84%EC%A7%80
# # 네이버 - 고양이 - 이미지 주소
# # https://search.naver.com/search.naver?where=image&sm=tab_jum&query=%EA%B3%A0%EC%96%91%EC%9D%B4
# # baseUrl = "https://search.naver.com/search.naver?where=image&sm=tab_jum&query="
# # word = input("검색어를 입력하세요 : ")
# from urllib.request import urlopen
# from urllib.parse import quote_plus
# # num = int(input("개수 입력 : "))
# # url = baseUrl+quote_plus(word)
# # # print(url)
# # html = urlopen(url)
# # # print(html)
# # soup = BeautifulSoup(html, "html.parser")
# # # print(soup)
# # img = soup.find_all(class_="_img")
# # # main_pack < section < div._cotentRooot.image_wrap > div.photo_grup._listGrid > div.photo_tile._grid > div:nth-child(3) > div > div.thumb > a > img
# # print(img)
# # print(len(img))
#
# # 다나와 :노트북 검색 결
import ssl
ssl._create_default_https_context = ssl._create_unverified_context
#
#
import urllib.request as req
# url = "http://search.danawa.com/dsearch.php?k1=%EB%85%B8%ED%8A%B8%EB%B6%81&module=goods&act=dispMain"
# res = req.urlopen(url)
# soup = BeautifulSoup(res, "html.parser")
# print(soup.select_one("#adReaderProductItem10100022 > div > div.prod_info > p > a"))
#
#
#
from selenium import webdriver  # 중요1
driver=webdriver.Chrome("/Users/coolmuk/chromedriver")  # 중요하다
# url="http://search.danawa.com/dsearch.php?query=무선청소기&tab=main"
# # url
# driver.get(url) # 해당 url을 브라우저에 띄움
# print(driver.current_url)
# driver.implicitly_wait(3)    #웹 페이지의 모든 요소(이미지, 텍스트 등)를 모두 읽을 때까지 3초 대기
#
# from bs4 import BeautifulSoup
# html = driver.page_source
# soup = BeautifulSoup(html, "html.parser")
# print(soup)
#
# prod_items = soup.select("li.prod_item")
# print(prod_items)
# print("="*50)
# print(len(prod_items))


# url = "http://search.danawa.com/dsearch.php?query=무선청소기&tab=main"
# from selenium import webdriver
# driver = webdriver.Chrome('c:/scrap/chromedriver.exe')
# url = "http://search.danawa.com/dsearch.php?query=무선청소기&tab=main"
# driver.get(url)
from bs4 import BeautifulSoup
#
html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')
# print(soup)
#
# prod_items = soup.select('li.prod_item')
# print(len(prod_items))

# <a href="http://www.google.com" target="_blank"><img src="google.png" width="300" height="200"></a>

# 2번 요세푸스 문제

def sol(n,k): #n=10, k=3
    a=list(range(1,n+1)) #a=(1,2,3,4,5,6,7,8,9,10)
    j=k-1 #j=3-1=2
    b=0
    while(len(a)>1):
        b=(len(a)+b)%k  # (5+2)%3 => 나머지=1, b=1
        del a[j::k]   #a[0::3]
        j=k-b-1 #j=3-1-1=0   => j=1
    return a #마지막살아남은1명병사
print(sol(10,3)) #총 10명 병사, 3명 간격으로 자살

#3 번 문제
# from collections import Counter
# with open("input.txt", "r") as f:
#     words = [w.strip(".,") for w in f.read().split()]
#
# Counter(words).most_common(10)
# print(words)
#
# <html>
# <head>
#     <meta charset = "UTF-8">
#     <style>
#         .box{
#         background-color:#09c;
#         }
#         .hover-box:hover{
#         background-color:orange;
#         }
#         .focus-input:foucs{
#         background-color:yellow;
#         }
#     </style>
#
# </head>
# <body>
# <div class = "box hover -box">마우스를 올려주세요</div>
# <input type = "texxt" value="click me" class - "focus-input">
#
# </body>
# <div style="width:50%;height:20%;background-color:orange"
#     200*100화면
# </div>
#
# </body>
# </html>

'''
마진 : 바깥쪽(싱히죄우) 여백
margin: 100px 상하좌우여백
margin: 50px 10px 상하 50px 좌우 10px
margin: 10px 20px 30px 40px 상10 하20 조30 우 40 여백

패딩: 안쪽 여백
'''
<html>
<head>
    <meta charset = "UTF-8">
    <style>
        #box1{margin:20pxx}
        #box2{margin:20px;padding:0}
        .box{background-color:orange}
    </style>
</head>
<body>
<div class = "box">
    <div id = "box1"> 마진 20px </div>
</div>

</body>
<div style="width:50%;height:20%;background-color:orange"
    200*100화면
</div>

</body>
</html>



<html>
<head>
    <meta charset="UTF-8">
    <style>
	.box-container{
		background-color: #d2f4ff;
		border: 2px solid #09c;
		margin: 5px 15px;
	}
	.box-container div{
		width: 120px;
		height: 80px;
		background-color: #fde6ff;
		border: 2px solid #90C;
		font-size: 15px;
	}
	#box1{ margin: 10px;  padding: 0; }
	#box2{ margin: 5px 25px; padding: 0; }
	#box3{ margin: 0;  padding: 10px 30px 5px; }
	#box4{ margin: 10px; padding: 10px 20px; }
	#box5{ margin: 10px 30px 0 50px; padding: 30px 0 }    </style>
</head>
<body>
	<div class="box-container">
		<div id="box1">m: 10<br>p: 0</div>
	</div>
	<div class="box-container">
		<div id="box2">m: 5 25<br>p: 0</div>
	</div>
	<div class="box-container">
		<div id="box3">m: 0<br>p: 10 30 5</div>
	</div>
	<div class="box-container">
		<div id="box4">m: 10<br>p: 10 20</div>
	</div>
	<div class="box-container">
		<div id="box5">m: 10 30 0 50<br>p: 30 0</div>
	</div>
</body>

</html>