class Student: 
    roll = ""
    gpa = ""

korim = Student()
korim.roll = "12345"
korim.gpa = "3.5"    
print(korim.roll)
print(korim.gpa)
print(isinstance(korim, Student))

print("------------- class in funtion -------------")
class Student2:
    roll = ""
    gpa = ""
    def set_value(self, roll, gpa):
        self.roll = roll
        self.gpa = gpa
    def display(self):
        print("Roll:", self.roll)
        print("GPA:", self.gpa)

korim2 = Student2()
korim2.set_value("54321", "3.8")
korim2.display()