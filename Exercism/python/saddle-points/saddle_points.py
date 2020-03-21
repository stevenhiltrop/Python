import numpy as np


def saddle_points(matrix: list) -> set:
    """
    Returns the list of all saddle points of the input matrix

    :param:
    matrix: list

    :return:

    """
    if len(set(map(len, matrix))) > 1:
        raise ValueError

    mt = list(zip(*matrix))
    points = set()
    for i, row in enumerate(matrix):
        for j, x in enumerate(row):
            if x == max(row) and x == min(mt[j]):
                points.add((i, j))
    return points
