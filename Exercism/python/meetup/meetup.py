from datetime import datetime

def meetup(year, month, week_of_month, day_of_week):  # Monday = 0 -> Sunday = 6
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

    week = {
        "teenth": 0,
        "1st": 0,
        "2nd": 7,
        "3rd": 14,
        "4th": 21,
        "5th": 28,
        "last": 28
    }[week_of_month]

    day = datetime.weekday(week + days.index(day_of_week))

    return datetime.date(year, month, day)

class MeetupDayException(Exception):
    def __init__(self):
        raise ValueError("The given input is wrong. Please use: {}".format(help(meetup)))

# class Week(IntEnum):
#     FIRST =  1,
#     SECOND = 8,
#     THIRD = 15,
#     FOURTH = LAST = 21
