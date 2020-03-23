def classify(number: int) -> str:
    """
    Classify the given number according to Nicomachus classification.

    :param:
    number: int

    :return:
    classification: str
    """
    if type(number) is not int or number <= 0:
        raise ValueError("Not a natural number.")

    aliquots = list()
    for i in range(1, number):
        if divmod(number, i)[1] == 0:
            aliquots.append(i)

    if sum(aliquots) == number:
        return "perfect"
    elif sum(aliquots) > number:
        return "abundant"
    elif sum(aliquots) < number:
        return "deficient"
