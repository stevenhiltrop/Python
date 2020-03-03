import string


def normalize(plain_text):
    plain_text = plain_text.lower()
    plain_text = plain_text.translate(str.maketrans('', '', string.punctuation))
    plain_text = plain_text.replace(' ', '')
    return plain_text


def cipher_text(plain_text):
    text = normalize(plain_text)
    if len(text) == 1:
        return text
    else:
        square = tuple()
        for count in range(len(text + 1)):
            pass
# Then, the normalized characters are broken into rows. These rows can be regarded as forming a rectangle when printed with intervening newlines.
