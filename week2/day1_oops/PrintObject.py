class Person:
    name=""
    age=0
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def __str__(self):
        return f"{self.name}({self.age})"

p = Person("Nivi",16)
print(p) # when no __str_(Self) it will print memory location of object


