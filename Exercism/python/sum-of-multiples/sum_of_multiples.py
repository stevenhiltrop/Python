from typing import List


def sum_of_multiples(limit: int, multiples: List[int]) -> int:
    """
    Return the sum of all the unique multiples of particular numbers up to but not including that number.

    :param:
    limit: int
    multiples: list

    :return:
    sum_of_multiples: int
    """
    multipliers = list()

    for multiplier in multiples:
        if multiplier != 0:
            for number in range(1, limit):
                if number % multiplier == 0:
                    multipliers.append(number)

    return sum(set(multipliers))
