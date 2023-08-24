#web1.py
#크롤링을 위한 선언
from bs4 import BeautifulSoup

#페이지 로딩(매서드 체인, 함수체인)
page = open("c:\\work\\test01.html", "rt", encoding="utf-8").read()
#검색을 위한 객체
soup = BeautifulSoup(page, "html.parser")
print(soup.prettify())
