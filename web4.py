# id 를 이용한 다양한 데이터 참조 방
import urllib

from bs4 import BeautifulSoup
# fp = open("lang.html", mode="r")
# soup = BeautifulSoup(fp, "html.parser")
# print(soup)
# print("="*50)
# print(soup.select_one("ul > li"))
# print("-"*50)
# print(soup.select("ul > li"))   #리스트
#
# # python 추출하기 feat. select_one
# print(soup.select_one("ul > li#py"))    # id가 py인 데이터 추출 #을 이용
# print(soup.select_one("#py"))    # 선택자(selector)
# print("-"*50)
# print(soup.select_one("ul#language > li#py")) # 복잡한 과정이나 이해를 높이기 위한 표현
# print(soup.select_one("#language > #py"))
# print(soup.select_one("#language #py"))
# print(soup.select_one("li[id='py']"))
# print("-"*50)
# print(soup.select_one("li:nth-of-type(3)"))
# print(soup.select("li")[2].string)
# print("-"*50)
# print("-"*50)
print("-"*50)

# 네이버 달러 환율 정보 가져오기
# import ssl
# context = ssl._create_unverified_context()
# import urllib.request
# req = urllib.request.urlopen(ssl, context=context).read()
# import urllib.request as req
# url = "https://finance.naver.com/marketindex/?tabSel=exchange#tab_section"
# res = req.urlopen(url)
'''
# import ssl
# context = ssl._create_unverified_context()  # MAC 용 ! 이거 없으면 안된다
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

import urllib.request as req
url = "https://ko.wikisource.org/wiki/%EC%A0%80%EC%9E%90:%EC%9C%A4%EB%8F%99%EC%A3%BC"
res = req.urlopen(url)
soup = BeautifulSoup(res, "html.parser")
print(soup.select_one("#mw-content-text > div.mw-parser-output > ul:nth-child(6) > li > b > a").string)

mylist = soup.select("#mw-content-text > div.mw-parser-output > ul:nth-child(6) > li > ul > li")
for li in mylist:
    print(li.string)
# print(len(mylist))
'''
fp=open("fruits-vegetables.html")
soup = BeautifulSoup(fp, "html.parser")
print(soup.select("div"))
print(soup.select("li"))

print(soup.select("li.black")[1].string)

print(soup.select("#ve-list > li:nth-of-type(4)")[0].string)
print(soup.select("#ve-list > li"))

dic = {"data-lo":"us", "class":"black"}  # {속성명:속성값,...}
print(soup.find("li")) #find함수 == select_one함수, findAll==select함수

print(soup.findAll("li",dic))
print(soup.find("li",dic))

print(soup.find(id="ve-list").find("li", dic).string)

# Selenium : 웹 브라우저를 제어하는 프로그램
from selenium import webdriver


