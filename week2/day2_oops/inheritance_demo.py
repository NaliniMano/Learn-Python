class Animal:
     def __init__(self,name):
         self.name=name
     def speak(self):
         return "no sound"
class Cat(Animal):
      def speak(self):
          return f"{self.name} says  MEW MEW"
class Dog(Animal):
      def speak(self):
          return f"{self.name} says WOO WOO"

cat=Cat("Whisker")
dog=Dog("Rocky")

print(cat.speak())
print(dog.speak())
