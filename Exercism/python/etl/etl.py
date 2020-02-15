def transform(legacy_data: dict):
    data = dict()

    for score, letters in legacy_data.items():
        for letter in letters:
            data[letter] = score

# legacy_data = {1: ["A", "E", "I", "O", "U"]}
# data = {"a": 1, "e": 1, "i": 1, "o": 1, "u": 1}
