# demodict.py
colors = {"apple":"red", "banana":"yello"}
print(len(colors))
#입력
colors["kiwi"] = "green"
#검색
print(colors["apple"])

for item in colors.items():
    print(item)

phone = {"kim":"1111", "lee":"2222", "park":"3333"}
print("kim" in phone)
p = phone
p["kang"] = "1234"
print(p)
print(phone)
print(id(phone), id(p))

#원본과 별도의 복사본을 생성하는 경우
import copy
device = {"아이폰":5, "아이패드":10}
#별도의 복사본을 생성
#device
device2 = copy.deepcopy(device)
device2["맥북"] = 20
print(device)
print(device2)