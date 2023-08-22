#전역 변수
str = "Not Class Member"
class GString:
    def __init__(self):
        #인스턴스 맴버 변수
        self.str = "" 
    def set(self, msg):
        self.str = msg
    def print(self):
        #버그 (모호한거 보다는 명시적인 것이 좋다)
        print(self.str)

g = GString()
g.set("First Message")
g.print()
