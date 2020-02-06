class Allergies:

    def __init__(self, score):
        self.allergy = score
        self.allergies = {
            "eggs": 1,
            "peanuts": 2,
            "shellfish": 4,
            "strawberries": 8,
            "tomatoes": 16,
            "chocolate": 32,
            "pollen": 64,
            "cats": 128
        }

    def allergic_to(self, item):
        return True if self.allergy >= self.allergies[item] else False

    @property
    def lst(self):
        allergies = list()

        for allergy, score in reversed(self.allergies.items()):
            if score <= self.allergy:
                allergies.append(allergy)
                self.allergy -= score

        return allergies
