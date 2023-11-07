class Animal:
    def __init__(self, name = 'Tom') -> None:
        self.name = name
    def play(self):
        print("I'm", self.name)
class Dog(Animal):
    def __init__(self, name = "Tony") -> None:
        super(Dog,self).__init__(name)
        # self.name = name
    def __eq__(self, __value: object) -> bool:
        return self.name == __value.name
dog = Dog("bitch")

cat = Dog("bitch")
cat.play()
dog.play()
print(cat ==dog)
