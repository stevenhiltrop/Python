from random import randint, choice

ABILITIES = [
    "charisma",
    "wisdom",
    "intelligence",
    "constitution",
    "dexterity",
    "strength"
]


def modifier(mod):
    return round((mod - 10) / 2)


def roll_dice():
    rolls = [randint(1, 6) for roll in range(4)]
    return sum(sorted(rolls)[-3:])


class Character:
    def __init__(self):
        self.charisma = roll_dice()
        self.wisdom = roll_dice()
        self.intelligence = roll_dice()
        self.constitution = roll_dice()
        self.dexterity = roll_dice()
        self.strength = roll_dice()
        self.hitpoints = 10 + modifier(self.constitution)

    def ability(self):
        return self.__getattribute__(choice(ABILITIES))
