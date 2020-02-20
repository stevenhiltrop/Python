import string


class Cipher:
    def __init__(self, key=None):
        self.key = string.ascii_lowercase.index(key[0]) if key else 3
        self.alphabet = string.ascii_lowercase
        self.shifted_alphabet = self.alphabet[self.key:] + self.alphabet[:self.key]

    def encode(self, text):
        table = str.maketrans(self.alphabet, self.shifted_alphabet)
        self.key = text.translate(table)
        return self.key

    def decode(self, text):
        table = str.maketrans(self.shifted_alphabet, self.alphabet)
        self.key = text.translate(table)
        return self.key
