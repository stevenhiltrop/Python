class Dog:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "Woof!"


class Cat:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "Meow!"


def get_pet(pet="dog"):
    """ the factory function """

    pets = dict(dog=Dog("Hope"), cat=Cat("Peace"))

    return pets[pet]
