def is_armstrong_number(number):
    numbers = list(str(number))
    total = 0
    for digit in numbers:
        total += pow(int(digit), len(numbers))

    return True if total == number else False

    # numbers = list(str(number))
    # armstrong = lambda digit: pow(int(digit), len(numbers))
    # total = sum(list(map(armstrong, numbers)))
    # return True if total == number else False