SUBLIST = None
SUPERLIST = None
EQUAL = None
UNEQUAL = None


def sublist(list_one, list_two):
    if all(item in list_two for item in list_one):
        return SUBLIST
    elif all(item in list_one for item in list_two):
        return SUPERLIST

    if set(list_one) == set(list_two):
        return EQUAL
    else:
        return UNEQUAL
