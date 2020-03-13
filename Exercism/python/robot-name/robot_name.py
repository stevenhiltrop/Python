from random import randint, choice
from string import ascii_uppercase


class Robot:
    def __init__(self):
        """
        Define a random name for the new robot
        """
        self.initials = ''.join(choice(ascii_uppercase) for x in range(2))
        self.numbers = ''.join(str(randint(0, 9)) for number in range(3))

    def name(self):
        return self.initials + self.numbers
