from datetime import time


class Clock:
    def __init__(self, hour, minute):
        self.hour = (hour + int(minute / 60)) % 24
        self.minute = minute % 60

        self.clock = time(hour=self.hour, minute=self.minute)

    def __repr__(self):
        return self.clock.isoformat(timespec='minutes')

    def __eq__(self, other):
        pass

    def __add__(self, minutes):
        pass

    def __sub__(self, minutes):
        pass
