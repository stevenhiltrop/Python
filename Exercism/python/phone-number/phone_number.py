def filter_numbers(number: str) -> str:
    return ''.join(filter(str.isdigit, number))


def validate(number: str) -> str:
    n_digit = number[:1]
    x_digit = number[1:]

    if 2 > int(n_digit) or not n_digit.isdigit():
        raise ValueError(f"{n_digit}: {type(n_digit)}")
    elif not x_digit.isdigit():
        raise ValueError(f"{x_digit}")
    else:
        return number


class PhoneNumber:
    def __init__(self, number):
        digits = filter_numbers(number)
        country_code = digits[:1] if digits.startswith('1') else None

        # TODO: number validation

        self.number = digits[1:] if country_code else digits
        self.area_code = validate(self.number[:3])
        self.pretty = f"({self.area_code}) {validate(number[3:6])}-{number[6:]}"
