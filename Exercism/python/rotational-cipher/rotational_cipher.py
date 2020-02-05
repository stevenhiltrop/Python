def rotate(text, key):
    return ''.join(map(lambda c: chr(ord('a') + (ord(c) - ord('a') + key) % 26), text))
