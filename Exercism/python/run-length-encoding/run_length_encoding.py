from itertools import groupby


def decode(string):
    pass


def encode(string):
    result = []

    for k, i in groupby(string):
        run = list(i)
        if len(run) > 2:
            result.append("{:02}{}".format(len(run), k))
        else:
            result.extend(run)

    return "".join(result)
