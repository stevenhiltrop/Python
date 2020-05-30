"""
Exercism solution for "wordy"
"""
import operator
import re
from collections import deque

OPS = {
    "plus": operator.add,
    "minus": operator.sub,
    "multiplied by": operator.mul,
    "divided by": operator.truediv,
    "to the power of": operator.pow,
}
INTS = re.compile(r"\s*(-?(?=\d)\d+)\s*")


def answer(question: str) -> int:
    """
    Given a wordy question, calculate the answer.
    """
    ops = deque(INTS.split(question))
    if ops[0] != "What is" or ops[-1] != "?":
        raise ValueError("Improperly phrased question.")
    ops.popleft()
    accum = int(ops.popleft())
    while ops[0] != "?":
        try:
            accum = OPS[ops.popleft()](accum, int(ops.popleft()))
        except KeyError:
            raise ValueError("Unrecognized operator!")
    return accum