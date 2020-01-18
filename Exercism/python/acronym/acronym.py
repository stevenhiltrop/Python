def abbreviate(words):
    acronym = str()

    for word in words.split():
        if word[:1].isaplha():
            acronym += ''.join(word[:1])

    return acronym.upper()
