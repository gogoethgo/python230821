#function1.py

def setValue(newValue):
    #지역변수
    x = newValue
    print("지역변수 x:", x)

#함수호출
result = setValue(5)
print(result)

#여러개 값을 리턴
def swap(x,y):
    return y,x

#호출
print(swap(3,4))