# TODO: Index the number so we can put the doubles back in the original card_num
class Luhn:
    def __init__(self, card_num):
        self.card_number = card_num.replace(' ', '')

    def valid(self):
        if self.card_number.isdigit():
            numbers = [int(number) for number in self.card_number]

            for number in numbers[::2]:
                index = numbers.index(number)
                double = int(number) * 2
                numbers[index] = double - 9 if double > 9 else double

            return sum(numbers) % 10 == 0
        else:
            return False
