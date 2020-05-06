def add(numbers):
    return sum(numbers)


def subtract(numbers):
    return lambda q, p: p - q, numbers


def multiply(numbers):
    return pow(numbers)


def divide(numbers):
    return lambda q, p: p / q, numbers


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
        if word.isdigit() or word in operators:
            actions.append(word)

    if len(actions) == 1:
        return int(actions.pop())
    if 1 < len(actions):
        solution = 0
        number = int(actions.pop(0))
        for action in actions:
            number_to_be_calculated = int(actions.pop(1))
            solution = operators[action]([number, number_to_be_calculated])
        return solution
