class bike: 
    def __init__(self, name, model): 
        self.name = name 
        self.model = model 
    def __str__(self): 
        return f"Bike Name: {self.name}, Bike Model: {self.model}"
    def __eq__(self, value):
        return self.name == value.name and self.model == value.model
    def display(self): 
        print("Bike Name:", self.name) 
        print("Bike Model:", self.model)

bike1 = bike("Yamaha", "R15")
bike2 = bike("Yamaha", "R15")
print(bike1)
print(bike2)
print(bike1 == bike2)
