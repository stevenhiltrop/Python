import re


def abbreviate(words):
    words = re.findall(r"[\w']+", words)
    acronym = str()

    for word in words:
        word = ''.join(e for e in word if e.isalnum())
        acronym += ''.join(word[:1].capitalize())

    return acronym.upper()
