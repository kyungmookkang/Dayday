'''
1. "test.txt"라는 파일에 "big data" 문자열을 저장한 후 다시 그 파일을 읽어서 출력하는 프로그램을 작성하시오.

f = open("test.txt","w")
f.write("big data")
f.close()

with open("test.txt", "r") as f:
    s = f.read()
    print(s)

2. 다음과 같은 문자열에서 휴대폰 번호 뒷자리인 숫자 4개를 ####로 바꾸는 프로그램을 정규식을 사용하여 작성하시오.
"""
park 010-9999-9988
kim 010-9909-7789
lee 010-8789-7768
"""

import re

s = """
park 010-9999-9988
kim 010-9909-7789
lee 010-8789-7768
"""

pat = re.compile("(\d{3}[-]\d{4})[-]\d{4}")
result = pat.sub("\g<1>-####", s)

print(result)


3. utf-8로 인코딩하기 위한 meta 태그를 적으시오.

<meta charset="UTF-8">

4. 네이버 또는 다음에 실린 신문기사를 스크래핑하는 코드를 작성하시오. (신문사 및 카테고리는 자유롭게 선택 가능, 1page만)

from bs4 import BeautifulSoup
import urllib.request as req
import re
from selenium import webdriver
driver=webdriver.Chrome("/Users/coolmuk/chromedriver")
url = "https://news.naver.com/main/read.nhn?mode=LSD&mid=shm&sid1=105&oid=030&aid=0002925183"
driver.get(url)
html = driver.page_source
soup = BeautifulSoup(html,'html.parser')

article = soup.select("#main_content > div.article_header > div.article_info")
print(article[0:])


'''


from bs4 import BeautifulSoup
import urllib.request as req
import re
from selenium import webdriver
driver=webdriver.Chrome("/Users/coolmuk/chromedriver")
url = "https://news.naver.com/main/read.nhn?mode=LSD&mid=shm&sid1=105&oid=030&aid=0002925183"
driver.get(url)
html = driver.page_source
soup = BeautifulSoup(html,'html.parser')

article = soup.select("#main_content > div.article_header > div.article_info")
print(str(article[0:]))