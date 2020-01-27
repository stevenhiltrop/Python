from collections import OrderedDict


def decode(string):
    pass


def encode(string):
    dictionary = OrderedDict.fromkeys(string, 0)
    output = ''

    for ch in string:
        dictionary[ch] += 1

    for key, value in dictionary.items():
        output = output + str(value) + key
    return output
