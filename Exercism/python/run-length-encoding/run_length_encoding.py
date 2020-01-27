from itertools import groupby


def decode(string):
    pass


def encode(string):
    result = []

    for k, i in groupby(string):
        run = list(i)
        print(len(run))
        if len(run) > 1:
            result.append("{0}{1}".format(len(run), k))
        else:
            result.extend(run)

    return "".join(result)
