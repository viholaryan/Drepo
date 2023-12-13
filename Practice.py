# Class definition
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        print("Woof!")

# Object creation and method call
my_dog = Dog("Buddy", 3)
print(my_dog.name)
my_dog.bark()

