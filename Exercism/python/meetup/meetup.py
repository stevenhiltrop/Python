import calendar
from datetime import date, timedelta


def meetup(year, month, week, day_of_week):
    """
    Calculate the date of the meetup

    :param
    year: int
    month: int
    week: str
        "teenth", "1st", "2nd", "3rd", "4th", "5th", "last"
    day_of_week: str
        "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"

    :return:
    datetime.date
    """
    day = {
        "Monday": calendar.MONDAY,
        "Tuesday": calendar.TUESDAY,
        "Wednesday": calendar.WEDNESDAY,
        "Thursday": calendar.THURSDAY,
        "Friday": calendar.FRIDAY,
        "Saturday": calendar.SATURDAY,
        "Sunday": calendar.SUNDAY
    }[day_of_week]

    if week[0].isdigit():
        month_range = calendar.monthrange(year, month, w=int(week[0]))
    elif week == "last":
        month_range = calendar.monthrange(year, month, w=month_range[1])
    elif week == "teenth":
        pass
    else:
        raise MeetupDayException

    date_corrected = date(year, month, month_range[1])
    delta = (day - month_range[0]) % 7

    return date_corrected + timedelta(days=delta)


class MeetupDayException(Exception):
    def __init__(self):
        raise ValueError("The given input is wrong. Please use: {}".format(help(meetup)))

# class Week(IntEnum):
#     FIRST =  1,
#     SECOND = 8,
#     THIRD = 15,
#     FOURTH = LAST = 21
