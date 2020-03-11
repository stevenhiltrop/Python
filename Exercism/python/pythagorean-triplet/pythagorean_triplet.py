from math import sqrt


def triplets_with_sum(number):
    divisors = [num for num in range(1, number + 1) if number % num == 0]
    middle_element = int(len(divisors) / 2)
    a, b = pow(middle_element, 2), pow(middle_element + 1, 2)
    return a + b if is_triplet([a, b, a + b]) else list()


def triplets_in_range(start, end):
    pass


def is_triplet(triplet):
    root = sqrt(triplet[0] + triplet[1])
    return int(root + 0.5) ** 2 == triplet[2]
