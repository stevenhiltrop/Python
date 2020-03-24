from typing import List


def commands(number: int) -> List[str]:
    """
    Get the secret handshake code

    :param:
    number: int

    :return:
    commands: List[str]
    """
    binary = f'{number:b}'
    secrets = list()
    handshakes = ["wink", "double blink", "close your eyes", "jump"]

    for index, char in enumerate(reversed(binary[-4:])):
        if char == '1':
            secrets.append(handshakes[index])

    return list(reversed(secrets)) if len(binary) >= 5 and binary else secrets
