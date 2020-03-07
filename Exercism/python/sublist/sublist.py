SUBLIST = 0
SUPERLIST = 1
EQUAL = 2
UNEQUAL = 3


def sublist(list_one, list_two):
    """
    Check if the given lists are sublist, superlist, equal lists or is unequal from eachother.

    :param
    list_one: list
    list_two: list

    :return:
    list_type: bool
    """
    A = ','.join([str(element) for element in list_one])
    B = ','.join([str(element) for element in list_two])

    if A == B:
        return EQUAL

    if A in B:
        return SUBLIST

    if B in A:
        return SUPERLIST

    return UNEQUAL
