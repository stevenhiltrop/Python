from itertools import groupby


def decode(string: str) -> str:
    """
    Decode a run length code

    :param
    string: str

    :return:
    result: str
    """
    result = ""

    for index, char in enumerate(string):
        if char.isdigit():
            result += int(char) * string[index + 1]

    return "".join(result)


def encode(string: str) -> str:
    """
        Encode a long string

        :param
        string: str

        :return:
        result: str
        """
    result = ""

    for k, i in groupby(string):
        run = list(i)

        if len(run) > 1:
            result += "{0}{1}".format(len(run), k)
        else:
            result += run

    return "".join(result)
