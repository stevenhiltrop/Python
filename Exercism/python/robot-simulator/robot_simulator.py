# Globals for the directions
# Change the values as you see fit
EAST = 1
NORTH = 1
WEST = -1
SOUTH = -1


class Robot:
    def __init__(self, direction=NORTH, x=0, y=0):
        self.position_x = x
        self.position_y = y
        self.direction = direction
        self.movement = None

    @property
    def coordinates(self):
        return tuple((self.position_x, self.position_y))

    def move(self, direction):
        pass
