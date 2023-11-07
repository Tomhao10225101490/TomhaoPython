class Animal:
    name  = "Animal"
class Dog(Animal):
    def say(self):
        print("dog")
class Cat(Animal):
    def say(self):
        print("cat")
dog = Dog()
cat = Cat()
print(dog.name)
print(cat.name)
print(Animal.name)
dog.name = "pop"
cat.name = "Amy"
print(dog.name)
print(cat.name)
print(Animal.name)
Animal.name = "sea animal"
print(dog.name)
print(cat.name)
print(Animal.name)
fish = Dog()
print(fish.name)
