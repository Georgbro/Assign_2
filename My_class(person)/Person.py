class Person:
    def __init__(self, age, name, hight):
        self.age = age
        self.name = name
        self.hight = hight
    
    def birthday(self):
        self.age += 1
        print(f"Happy brithday. You are now {self.age}")

person1 = Person(21, "Sam", 182)

person1.birthday()
