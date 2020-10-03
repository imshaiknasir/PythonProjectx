#constructor in python...
class Truck:
    brand = "BMW"

    def __init__(self):     #to create constructor is __init__(); this function will be executed while object creation
        print("Constructor is executed first.")

    def getName(self):
        print("Simple method execution.")

obj = Truck() #constructor executed;
obj.getName()
print(obj.brand)