#web1.py
#크롤링을 위한 선언
from bs4 import BeautifulSoup

#페이지 로딩(매서드 체인, 함수체인)
page = open("c:\\work\\test01.html", "rt", encoding="utf-8").read()
#검색을 위한 객체(웹에 있는 일반 문서)
soup = BeautifulSoup(page, "html.parser")
#print(soup.prettify())
#문서 전체에서 <P> 검색
#print(soup.find_all("p"))
#천번쨰 <p>를 검색
#print(soup.find("p"))
#조건이 있는 경우:<p clss "outer"-text>
#class 는 키워드 충돌 때문에 사용#
#print(soup.find_all("p", class_="outer-test"))
#특정 속성을 지정할 때 : attrs
#print(soup.find_all("p" , attrs={"class":"outer-text"}))
#특정 ID만 지정
#print(soup.find_all(id="first" ))

for tag in soup.find_all("p"):
    title = tag.text.strip()
    print(title)