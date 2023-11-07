class animal:
    def __init__(self,name):
        self.name = name
class Dog(animal):
    def __init__(self,name):
        super(Dog,self).__init__(name)
    def speak(self):
        print(self.name)
a = Dog('tom')
a.speak()
print(isinstance(Dog,animal))
print(isinstance(a,animal))
print(isinstance(a,Dog))
print(issubclass(Dog,animal))
