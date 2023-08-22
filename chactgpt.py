class Person:
    def __init__(self, ID, name):
        self.ID = ID
        self.name = name
        
    def printinfo(self):
        print(f"ID: {self.ID}, 이름: {self.name}")  # ID와 이름 출력


class Manager(Person):
    def __init__(self, ID, name, skill):
        super().__init__(ID, name)
        self.skill = skill
        
    def printinfo(self):
        super().printinfo()
        print(f"기술: {self.skill}")  # 부모 클래스의 정보 출력 후 기술 정보 출력


class Employee(Person):
    def __init__(self, ID, name, role):
        super().__init__(ID, name)
        self.role = role
        
    def printinfo(self):
        super().printinfo()
        print(f"역할: {self.role}")  # 부모 클래스의 정보 출력 후 역할 정보 출력


# 테스트 예제
if __name__ == "__main__":
    # Person 클래스 테스트
    person1 = Person("P001", "John Doe")
    person1.printinfo()

    # Manager 클래스 테스트
    manager1 = Manager("M001", "Alice Smith", "프로젝트 관리")
    manager1.printinfo()

    # Employee 클래스 테스트
    employee1 = Employee("E001", "Bob Johnson", "소프트웨어 개발자")
    employee1.printinfo()

    person2 = Person("P002", "Jane Smith")
    person2.printinfo()

    manager2 = Manager("M002", "Eve Brown", "팀 리더십")
    manager2.printinfo()

    employee2 = Employee("E002", "Charlie Williams", "데이터 분석가")
    employee2.printinfo()

    person3 = Person("P003", "Lisa Garcia")
    person3.printinfo()

    manager3 = Manager("M003", "David Lee", "제품 관리")
    manager3.printinfo()

    employee3 = Employee("E003", "Sophia Martinez", "UX 디자이너")
    employee3.printinfo()

    person4 = Person("P004", "Michael Johnson")
    person4.printinfo()
