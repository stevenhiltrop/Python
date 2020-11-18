def count_to(count):
    numbers_in_german = ["eins", "zwei", "drei", "vier", "funf"]
    iterator = zip(range(count), numbers_in_german)

    for position, number in iterator:
        yield number


for number in count_to(3):
    print(number)
