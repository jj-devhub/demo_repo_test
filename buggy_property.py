class Person:
    def __init__(self, name):
        self._name = name
    @property
    def name(self):
    # Bug fixed: return the stored name
    return self._name
    @name.setter
    def name(self, value):
        self._name = value

p = Person("Alice")
print(p.name)  # Bug: prints None
p.name = "Bob"
print(p.name)
