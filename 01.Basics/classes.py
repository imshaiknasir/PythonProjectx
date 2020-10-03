#Class in python

#to define a class, start with the keyword "class" followed by the 'className'
class Car:

    #inside class we can have variable and functions
    brand = "Tesla"

    def getName(self):
        print("Simple method execution.")

obj1 = Car()  #create the object of the class.
obj1.getName() #now call the method present inside the class.