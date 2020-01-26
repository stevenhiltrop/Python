def is_valid(isbn):
    """
    Check if the given ISB Number is valid

    :param
    isbn: string

    :return:
    ISBN validation: bool
    """
    formatted_number = isbn.replace("-", "")

    if len(formatted_number) != 10 or formatted_number[9].isdigit():
        return False

    check_sum = sum(int(formatted_number[i]) * (10 - i) for i in range(8))
    check_sum %= 11
    check_digit = 11 - check_sum

    if formatted_number.endswith("X"):
        return check_digit == 10
    elif formatted_number[-1].isdigit():
        return check_digit == int(formatted_number[-1])
    else:
        return False
