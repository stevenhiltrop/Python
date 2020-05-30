def filter_numbers(number: str) -> str:
    return ''.join(filter(str.isdigit, number))


def validate(number: str) -> bool:
    n_digit = number[:1]
    x_digit = number[1:]

    if 2 > int(n_digit) or not n_digit.isdigit() or not x_digit.isdigit():
        raise ValueError
    else:
        return number


class PhoneNumber:
    def __init__(self, number):
        digits = filter_numbers(number)
        country_code = digits[:1] if digits.startswith('1') else None

        self.number = digits[1:] if country_code else digits
        self.area_code = validate(self.number[:3])
        self.pretty = f"({self.area_code}) {number[3:6]}-{number[6:]}"
