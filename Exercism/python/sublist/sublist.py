SUBLIST = None
SUPERLIST = None
EQUAL = None
UNEQUAL = None


def sublist(list_one: list, list_two: list) -> [SUPERLIST, SUBLIST, EQUAL, UNEQUAL]:
    """
    Check if the given lists are sublist, superlist, equal lists or is unequal from eachother.

    :param
    list_one: list
    list_two: list

    :return:
    list_type: bool
    """
    if all(item in list_two for item in list_one):
        return SUBLIST
    elif all(item in list_one for item in list_two):
        return SUPERLIST

    if set(list_one) == set(list_two):
        return EQUAL
    else:
        return UNEQUAL
