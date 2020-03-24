def commands(number):
    binary = f'{number:b}'
    secrets = list()
    handshakes = ["wink", "double blink", "close your eyes", "jump"]

    for index, char in enumerate(binary[-4:]):
        if char == 1:
            secrets.append(handshakes[index])

    return reversed(secrets) if len(binary) >= 5 and binary else secrets
