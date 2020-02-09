# Globals for the directions
# Change the values as you see fit
EAST = 2
NORTH = 1
WEST = 0
SOUTH = 3


class Robot:
    def __init__(self, direction=NORTH, x=0, y=0):
        self.position_x = x
        self.position_y = y
        self.direction = direction

    @property
    def coordinates(self):
        return tuple((self.position_x, self.position_y))

    def move(self, movement):
        for direction in movement:
            if direction == 'R':
                self.direction = (self.direction + 1) % 4
            elif direction == 'L':
                self.direction = (self.direction - 1) % 4
            elif direction == 'A':
                if self.direction is NORTH:
                    self.position_y += 1
                elif self.direction is SOUTH:
                    self.position_y -= 1
                elif self.direction is EAST:
                    self.position_x += 1
                elif self.direction is WEST:
                    self.position_x -= 1
            else:
                raise ValueError("Wrong movement entered. Use R/A/L.")
