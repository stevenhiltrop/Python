# TODO: Index the number so we can put the doubles back in the original card_num
class Luhn:
    def __init__(self, card_num):
        self.card_number = card_num.replace(' ', '')

    def valid(self):
        numbers = list()

        for number in self.card_number[::2]:
            double = int(number) * 2
            if double > 10:
                numbers.append(double - 9)
            else:
                numbers.append(double)

        return sum(numbers) % 10 == 0
