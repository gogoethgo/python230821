import requests
from bs4 import BeautifulSoup
import openpyxl
import os

def crawl_blog_info(search_keyword):
    base_url = f"https://search.naver.com/search.naver?where=view&sm=tab_jum&query={search_keyword}"
    
    response = requests.get(base_url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")
        
        blog_entries = soup.find_all("li", class_="bx")
        
        data_list = []
        for entry in blog_entries:
            blog_name = entry.find("a", class_="sub_txt").text
            blog_url = entry.find("a", class_="sub_txt")["href"]
            posting_date = entry.find("span", class_="sub_time").text
            
            data_list.append([blog_name, blog_url, posting_date])
        
        return data_list
    else:
        print("Failed to retrieve the page.")
        return []

def save_to_excel(data_list, file_path):
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = "Blog Info"
    
    header = ["블로그명", "블로그글 주소", "포스팅 날짜"]
    ws.append(header)
    
    for data in data_list:
        ws.append(data)
    
    wb.save(file_path)

# 사용 예시
search_keyword = input("검색 키워드를 입력하세요: ")
data_list = crawl_blog_info(search_keyword)

if data_list:
    folder_path = "c:\\work"
    if not os.path.exists(folder_path):
        os.mkdir(folder_path)
    
    file_path = os.path.join(folder_path, f"{search_keyword}_blog_info.xlsx")
    save_to_excel(data_list, file_path)
    print(f"데이터를 엑셀 파일로 저장했습니다: {file_path}")
else:
    print("검색 결과가 없습니다.")

