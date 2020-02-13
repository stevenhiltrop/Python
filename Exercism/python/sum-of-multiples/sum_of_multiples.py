def sum_of_multiples(limit, multiples):  # 7, [3]), 9 --> 3 + 6 = 9
    multipliers = list()

    for multiplier in multiples:
        for number in range(1, limit):
            if number % multiplier == 0:
                multipliers.append(number)

    return sum(set(multipliers))
