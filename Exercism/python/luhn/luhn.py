class Luhn:
    def __init__(self, card_num):
        self.card_number = card_num.replace(' ', '')
        self.num_digits = len(self.card_number)
        self.odd_even = self.num_digits & 1
        self.sum = 0

    def valid(self):
        if self.card_number.isdigit():
            for count in range(0, self.num_digits):
                digit = int(self.card_number[count])

                if not ((count & 1) ^ self.odd_even):
                    digit = digit * 2
                if digit > 9:
                    digit = digit - 9

                self.sum = self.sum + digit

            return (self.sum % 10) == 0
        else:
            return False
