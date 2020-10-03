#Types of variables:
#1. Instance variable; ("Variable that are defined inside cnstructor.")
#2. Class variable; ("Variable that are defined inside class.")

class Truck:
    brand = "BMW"
    #to call this, either you can use self.variableName OR ClassName.VariableName
    #for example: self.brand OR Truck.brand

    def __init__(self,x):
        self.name = x

    def getSomeText(self):
        print("Some dummy text")

    def getName(self):
        return self.name

#object creation
obj1 = Truck("Sachin")

obj1.getSomeText()
print(obj1.getName())