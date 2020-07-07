def valid(function):
    """
    Check if sum of 2 sides are biger then the other
    Example:
        (a + b < c) or (a + c < b) or (b + c < a)

    :param
    function:
    """
    return lambda side: all(side) and 2 * max(side) < sum(side) and function(side)


@valid
def equilateral(sides: list) -> bool:
    """
    An equilateral triangle has all three sides the same length

    :param
    sides: list

    :return
    is_equilateral: bool
    """
    return len(set(sides)) == 1 and 0 not in set(sides)


@valid
def isosceles(sides: list) -> bool:
    """
    An isosceles triangle has at least two sides the same length

    :param
    sides: list

    :return
    is_isosceles: bool
    """
    return len(set(sides)) < 3


@valid
def scalene(sides: list) -> bool:
    """
    A scalene triangle has all sides of different lengths

    :param
    sides: list

    :return
    is_scalene: bool
    """
    return len(set(sides)) == 3
