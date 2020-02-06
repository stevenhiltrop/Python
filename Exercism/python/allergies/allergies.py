ALLERGIES = {"eggs": 1,
             "peanuts": 2,
             "shellfish": 4,
             "strawberries": 8,
             "tomatoes": 16,
             "chocolate": 32,
             "pollen": 64,
             "cats": 128}


class Allergies:

    def __init__(self, score):
        self.score = score
        self.__lst = [key for key in ALLERGIES if self.allergic_to(key)]

    def allergic_to(self, item):
        return bool(self.score & ALLERGIES.get(item, 0))

    @property
    def lst(self):
        return self.__lst
