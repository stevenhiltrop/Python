import re


def count_words(sentence):
    word_list = re.split(",| |\"|\n|\t|\_|\.", sentence.lower())
    word_dict = dict()

    for word in word_list:
        if not word.isalnum() and word:  # Remove special and empty characters
            if word is "'":
                pass
            else:
                word = ''.join(character for character in word if character.isalnum())

        if word in word_dict:
            word_dict[word] += 1
        else:
            word_dict[word] = 1

    if '' in word_dict:
        word_dict.pop('')

    return word_dict
