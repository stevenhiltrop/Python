import re


def abbreviate(words):
    acronym = str()

    for word in re.findall(r"[\w']+", words):
        acronym += ''.join(word[:1].capitalize())

    return acronym.upper()
