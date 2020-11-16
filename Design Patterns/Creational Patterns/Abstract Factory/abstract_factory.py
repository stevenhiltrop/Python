class Dog:
    def speak(self):
        return "Woof"

    def __str__(self):
        return "dog"


class DogFactory:
    def get_pet(self):
        return Dog()

    def get_food(self):
        return "dog food!"


class PetStore:
    def __init__(self, pet_factory=None):
        self._pet_factory = pet_factory

    def show_pet(self):
        pet = self._pet_factory.get_pet()
        pet_food = self._pet_factory.get_food()
        print(
            f"Our pet is {pet}.\n"
            f"Our pet says hello by {pet.speak()}.\n"
            f"Its food is {pet_food}"
        )


factory = DogFactory()
shop = PetStore(factory)
shop.show_pet()
