class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
        
    def displayInfo(self):
        print(f"name = {self.name}, age = {self.age}, gender = {self.gender}")
        
p1 = Person("lmao", 6969, "gay")

p1.displayInfo()



class student(Person):
    def stu_init(self, name, age, gender, grade, dpt):
        pass