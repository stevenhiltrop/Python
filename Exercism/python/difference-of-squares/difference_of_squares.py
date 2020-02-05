def square_of_sum(number):  # (1 + 2 + ... + 10)² = 55² = 3025.
    return pow(sum(range(number+1)), 2)


def sum_of_squares(number):  # 1² + 2² + ... + 10² = 385.
    return sum([pow(num, 2) for num in range(number+1)])


def difference_of_squares(number):  # 3025 - 385 = 2640.
    return square_of_sum(number) - sum_of_squares(number)
