class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def printname(self):
        print(self.name,self.age)

class Student(Person):
   # pass
   def __init__(self,name,age):
       super().__init__(name,age) # super make the child class inherit all the methods and properties from its parent:

x=Student("john","23")
x.printname()

