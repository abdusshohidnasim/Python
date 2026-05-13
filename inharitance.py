class phone: 
    def massate(self):
        print("This is a message from the phone class.")
    def call(self):
        print("This is a call from the phone class.")
s3= phone()
print("phone")
print(s3.massate())

class smartphone(phone):
    def massate(self):
        print("This is a smarphone.")
    def call(self):
        print("This is a call from the smartphone class.")

s1 = smartphone()
s2 = phone()
s1.massate()
s1.call()   
print(s1.massate())
print("phone")
print(s2.massate())
print(isinstance(s1, smartphone))
print(isinstance(s1, phone))

print(issubclass(smartphone, phone))

print(issubclass(phone, smartphone))
