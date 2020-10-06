from Basics.Constructor02 import Truck


class Child(Truck):
    def __init__(self):
        Truck.__init__(self, "Raman")

    def childfunc(self):
        print(f"child text {self.getName()}")


obj = Child()
obj.childfunc()
