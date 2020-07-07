def equilateral(sides):
    """
    An equilateral triangle has all three sides the same length

    :param
    sides: list

    :return
    is_equilateral: bool
    """
    return len(set(sides)) == 1 and 0 not in set(sides)


def isosceles(sides):
    """
    An isosceles triangle has at least two sides the same length

    :param
    sides: list

    :return
    is_isosceles: bool
    """
    return len(set(sides)) <= 2 and 1 not in set(sides)


def scalene(sides):
    pass
