import re


def add(numbers):
    return sum(numbers)


def subtract(numbers):
    return numbers[0] - numbers[1]


def multiply(numbers):
    return pow(numbers)


def divide(numbers):
    return numbers[0] / numbers[1]


def contains_digits(d):
    _digits = re.compile('\d')
    return bool(_digits.search(d))


def answer(question):
    words = question.replace('?', '').split()
    actions = list()
    operators = {
        "plus": add,
        "minus": subtract,
        "multiplied": multiply,
        "divided": divide
    }

    for word in words:
        if contains_digits(word):
            actions.append(int(word))
        elif word in operators:
            actions.append(word)

    if len(actions) == 1:
        return actions.pop()
    if 1 < len(actions):
        solution = 0
        number = actions.pop(0)
        for action in actions:
            number_to_be_calculated = actions.pop(1)
            solution = operators[action]([number, number_to_be_calculated])
        return solution
