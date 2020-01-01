def recite(start_verse, end_verse):
    days = {
        1: "first",
        2: "second",
        3: "third",
        4: "fourth",
        5: "fifth",
        6: "sixth",
        7: "seventh",
        8: "eighth",
        9: "ninth",
        10: "tenth",
        11: "eleventh",
        12: "twelfth"
    }
    christmas_presents = [
        "and a Partridge in a Pear Tree.",
        "two Turtle Doves",
        "three French Hens",
        "four Calling Birds",
        "five Gold Rings",
        "six Geese-a-Laying",
        "seven Swans-a-Swimming",
        "eight Maids-a-Milking",
        "nine Ladies Dancing",
        "ten Lords-a-Leaping",
        "eleven Pipers Piping",
        "twelve Drummers Drumming"
    ]

    if end_verse > 1:
        presents = ', '.join(present for present in christmas_presents[end_verse - 1::-1])
    else:
        presents = christmas_presents[0].replace('and ', '')

    return "On the {0} day of Christmas my true love gave to me: {1}".format(days[start_verse], presents)
