import calendar
from datetime import date

DAYS = [day.lower() for day in calendar.day_name]
COUNTS = ['1st', '2nd', '3rd', '4th', '5th', 'last', 'teenth']
LAST = 5
TEENTH = 6


class MeetupDayException(Exception):
    pass


def meetup(year, month, week, day_of_week):
    week = week.lower()
    day_of_week = day_of_week.lower()
    try:
        weekday = DAYS.index(day_of_week)
        week_index = COUNTS.index(week)

        if week_index == TEENTH:
            first_teenth_weekday = calendar.weekday(year, month, 13)
            delta_days = 12 + (weekday - first_teenth_weekday) % 7
        else:
            first_weekday = calendar.weekday(year, month, 1)
            if week_index == LAST:
                delta_days = (weekday - first_weekday) % 7
                delta_days += ((calendar.monthlen(year, month) - delta_days - 1) // 7) * 7
            else:
                delta_days = (weekday - first_weekday) % 7 + 7 * week_index
        return date(year, month, delta_days + 1)
    except:
        raise MeetupDayException("That date is no good")
