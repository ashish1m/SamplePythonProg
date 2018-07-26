class Animal:

    def __init__(self):
        print("Animal is created")

    def speak(self):
        print("Animal is speaking")


class Dog(Animal):

    def __init__(self, name):
        super(Dog, self).__init__()
        self.name = name
        print("Dog is created")

    def speak(self):
        print("WOOF!")


class Cat(Animal):

    def __init__(self, name):
        super(Cat, self).__init__()
        self.name = name
        print("Cat is created")

    def speak(self):
        print("MEOW!")


tommy = Dog("Tommy")
mini = Cat("Mini")

for pet in [tommy, mini]:
    pet.speak()
