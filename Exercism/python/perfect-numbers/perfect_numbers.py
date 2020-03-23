def classify(number: int) -> str:
    """
    Classify the given number according to Nicomachus classification.

    :param:
    number: int

    :return:
    classification: str
    """
    if 0 < number and type(number) is int:
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

    else:
        raise ValueError("Not a natural number.")
