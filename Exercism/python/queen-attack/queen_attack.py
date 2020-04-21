def validate_input(row, column):
    if row < 0 or column < 0:
        raise ValueError("Position cannot be negative.")
    if row >= 8 or column >= 8:
        raise ValueError("The board is 0 - 7 squares. Given position is out of bounds.")


class Queen:
    def __init__(self, row, column):
        validate_input(row, column)
        self.row = row
        self.column = column

    def can_attack(self, another_queen):
        if (self.row, self.column) == (another_queen.row, another_queen.column):
            raise ValueError("Opponents on same position.")

        def horizontally(row):
            return self.row == row

        def vertically(column):
            return self.column == column

        def diagonally(row, column):
            left_column = right_column = column

            for position in range(row, 8):
                left_column -= 1
                right_column += 1
                return False if (row, left_column) == (row, column) or \
                               (row, right_column) == (row, column) \
                    else True

            for position in range(8, row, -1):
                left_column -= 1
                right_column += 1
                return False if (row, left_column) == (row, column) or \
                               (row, right_column) == (row, column) \
                    else True

        return horizontally(another_queen.row) or \
               vertically(another_queen.column) or \
               diagonally(another_queen.row, another_queen.column)
