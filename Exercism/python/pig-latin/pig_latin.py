def translate(text):
    lst = ['sh', 'gl', 'ch', 'ph', 'tr', 'br', 'fr', 'bl', 'gr', 'st', 'sl', 'cl', 'pl', 'fl']
    text = text.split()
    for k in range(len(text)):
        i = text[k]
        if i[0] in ['a', 'e', 'i', 'o', 'u']:
            text[k] = i + 'ay'
        elif t(i) in lst:
            text[k] = i[2:] + i[:2] + 'ay'
        elif not i.isalpha():
            text[k] = i
        else:
            text[k] = i[1:] + i[0] + 'ay'
    return ' '.join(text)


def t(str):
    return str[0] + str[1]
