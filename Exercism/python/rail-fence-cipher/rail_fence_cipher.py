def encode(message, rails):
    rail = [['\n' for i in range(len(message))]
            for j in range(rails)]
    dir_down = False
    row, col = 0, 0

    for i in range(len(message)):
        if (row == 0) or (row == rails - 1):
            dir_down = not dir_down

        rail[row][col] = message[i]
        col += 1
        if dir_down:
            row += 1
        else:
            row -= 1
    result = []
    for i in range(rails):
        for j in range(len(message)):
            if rail[i][j] != '\n':
                result.append(rail[i][j])
    return "".join(result)


def decode(encoded_message, rails):
    rail = [['\n' for i in range(len(encoded_message))]
            for j in range(rails)]
    dir_down = None
    row, col = 0, 0
    for i in range(len(encoded_message)):
        if row == 0:
            dir_down = True
        if row == rails - 1:
            dir_down = False
        rail[row][col] = '*'
        col += 1
        if dir_down:
            row += 1
        else:
            row -= 1
    index = 0
    for i in range(rails):
        for j in range(len(encoded_message)):
            if ((rail[i][j] == '*') and
                    (index < len(encoded_message))):
                rail[i][j] = encoded_message[index]
                index += 1
    result = []
    row, col = 0, 0
    for i in range(len(encoded_message)):
        if row == 0:
            dir_down = True
        if row == rails - 1:
            dir_down = False

        if (rail[row][col] != '*'):
            result.append(rail[row][col])
            col += 1
        if dir_down:
            row += 1
        else:
            row -= 1
    return "".join(result)
