#Functions in python:

#defining a function
def Call1():
    print("This is a function.")

def Call2(argu):
    print("This function takes an argument: " + argu)

def AddInts(a,b):
    print(f"Addition of  {a} + {b} is: {a+b}")

def ReturnCall(x, y):
    return x*y

#declating function
Call1()
Call2("Test")
AddInts(2,5)
print(ReturnCall(5,5))