#1
class Base1:
    def greet1(self):
        print("Hello from Base1")

class Base2:
    def greet2(self):
        print("Hello from Base2")

class Child(Base1, Base2):
    pass

c = Child()
c.greet1()
c.greet2()



