def filter_numbers(number: str) -> str:
    return ''.join(filter(str.isdigit, number))


def validate(number: str) -> bool:
    n_digit = number[:1]
    x_digit = number[1:]

    if 2 > int(n_digit) or not n_digit.isdigit() or not x_digit.isdigit():
        raise ValueError


class PhoneNumber:
    # TODO: validation
    def __init__(self, number):
        self.digits = filter_numbers(number)
        self.country_code = self.digits[:1] if self.digits.startswith('1') else None
        self.area_code = self.number[:3]

    @property
    def number(self):
        return self.digits[1:] if self.country_code else self.digits

    def pretty(self):
        return f"({self.area_code}) {self.number[3:6]}-{self.number[6:]}"
