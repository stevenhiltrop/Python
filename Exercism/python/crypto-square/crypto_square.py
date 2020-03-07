from math import ceil, sqrt
from string import punctuation


def normalize(plain_text):
    plain_text = plain_text.lower()
    plain_text = plain_text.translate(str.maketrans('', '', punctuation))
    plain_text = plain_text.replace(' ', '')
    return plain_text


def cipher_text(plain_text):
    text = normalize(plain_text)
    if len(text) == 1 or not text:
        return text
    else:
        rectangle_size = int(ceil(len(text)) / ceil(sqrt(len(text))))
        rectangle = [text[i:i + rectangle_size] for i in range(0, len(text), rectangle_size)]
        result = [str()] * rectangle_size

        for index in range(rectangle_size):
            for word in rectangle:
                result[index] = result[index] + word[index]

        return ' '.join(result)
