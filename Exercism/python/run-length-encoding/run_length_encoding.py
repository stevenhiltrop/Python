from itertools import groupby


def decode(string):
    result = ""

    for index, char in enumerate(string):
        if char.isdigit():
            result += int(char) * string[index + 1]

    return "".join(result)


def encode(string):
    result = ""

    for k, i in groupby(string):
        run = list(i)

        if len(run) > 1:
            result += "{0}{1}".format(len(run), k)
        else:
            result += run

    return "".join(result)
