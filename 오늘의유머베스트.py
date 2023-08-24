# coding:utf-8
from bs4 import BeautifulSoup
#웹서버에 요청
import urllib.request
#검색(키워드)
import re 

#User-Agent를 조작하는 경우(아이폰에서 사용하는 사파리 브라우져의 헤더) 
hdr = {'User-agent':'Mozilla/5.0 (iPhone; CPU iPhone OS 10_3 like Mac OS X) AppleWebKit/603.1.23 (KHTML, like Gecko) Version/10.0 Mobile/14E5239e Safari/602.1'}

f = open("c:\\work\\today.txt", "wt", encoding="utf-8")

for n in range(1,11):
        #클리앙의 중고장터 주소 
        data ='https://www.todayhumor.co.kr/board/list.php?table=bestofbest&page=' + str(n)
        print(data)
        #웹브라우져 헤더 추가 
        req = urllib.request.Request(data, \
                                    headers = hdr)
        data = urllib.request.urlopen(req).read()
        #한글이 깨지는 경우에 사용
        page = data.decode('utf-8', 'ignore')
        soup = BeautifulSoup(page, 'html.parser')
        list = soup.find_all('td', attrs={'class' :'subject'})

#<a href="/board/view.php?table=bestofbest&amp;no=470312&amp;s_no=470312&amp;page=1" target="_top">오펜하이머 한국판 리메이크 결정 ㄷㄷㄷ</a>
   # <span class="subject_fixed" data-role="list-title-text" title="맥북프로 m1 13인치 512GB 판매합니다(가격인하)">
	# 	  맥북프로 m1 13인치 512GB 판매합니다(가격인하)
	# </span>

        for item in list:
                try:
                        #<a class='list_subject'><span>text</span><span>text</span>
                        title = item.find("a").text.strip() 
                        link = item.find("a")["href"]
                        print(title)
                        #print(link)
                        # if (re.search('아이패드', title)):
                        #         print(title)
                        #         f.write(title + "\n")
                except:
                        pass
        
f.close()