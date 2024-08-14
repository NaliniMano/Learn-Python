class Bird:
    def fly(self):
        return "Birds can fly"

class Penguin(Bird):
    def fly(self):
        return "Penguin cannot fly"

def flying_test(bird):
    print(bird.fly())

bird=Bird()
penguin=Penguin()

print(bird.fly())
print(penguin.fly())