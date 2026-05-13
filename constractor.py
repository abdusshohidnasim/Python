class Student:


    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)
    def __init__(self, name, age,):
        self.name = name
        self.age = age



student1 = Student("Naiem", 22, )
student1.display()