#Types of variables:
#1. Instance variable; ("Variable that are defined inside cnstructor.")
#2. Class variable; ("Variable that are defined inside class.")

class Truck:
    brand = "BMW"
    #to call this, either you can use self.variableName OR ClassName.VariableName
    #for example: self.brand OR Truck.brand

    def __init__(self,x):
        self.name = x
        self.age = x

    def getName(self):
        print(f"Name: {self.name} {self.brand}")

    def getAge(self):
        print(f"Age:  {self.age} {self.brand}")

#object creation
obj1 = Truck("Sachin")
obj2 = Truck("55")

obj1.getName()
obj2.getAge()