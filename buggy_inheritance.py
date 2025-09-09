class Animal:
    def __init__(self, name):
        self.name = name
    def speak(self):
        # Bug fixed: base class should raise NotImplementedError
        raise NotImplementedError("Subclasses must implement speak()")

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

animals = [Dog("Buddy"), Cat("Whiskers")]
for animal in animals:
    print(f"{animal.name} says: {animal.speak()}")
