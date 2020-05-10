from operator import add, mul, truediv as div, sub


def answer(question):
    solution = 0
    operators = {
        '+': add,
        '-': sub,
        '/': div,
        '*': mul
    }
    question_str = question.strip("What is ").strip("?").replace(
        'plus', '+').replace('minus', '-').replace('divided by', '/').replace('multiplied by', '*')
    question_list = question_str.split()
    question_list.reverse()

    try:
        first = int(question_list.pop())
        while question_list:
            operator = question_list.pop()
            second = int(question_list.pop())
            solution = operators[operator](first, second)

            first = solution
    except ValueError:
        raise ValueError

    return int(solution)
