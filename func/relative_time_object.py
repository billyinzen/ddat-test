from datetime import datetime, timedelta

# utility class implementing time modification commands
class RelativeTimeObject:
    _yy: int = None # year
    _mo: int = None # month
    _dd: int = None # day
    _hh: int = None # hour
    _mi: int = None # minute
    _ss: int = None # second

    def __init__(self, dt: datetime):
        self.__fromDatetime(dt)

    def __str__(self) -> str:
        return f"{self._yy:04}-{self._mo:02}-{self._dd:02} {self._hh:02}:{self._mi:02}:{self._ss:02}"

    def toDatetime(self) -> datetime:
        return datetime(self._yy, self._mo, self._dd, self._hh, self._mi, self._ss)

    # extracts variables from a datetime object to the current RelativeTimeObject
    def __fromDatetime(self, dt: datetime):
        self._yy = dt.year
        self._mo = dt.month
        self._dd = dt.day
        self._hh = dt.hour
        self._mi = dt.minute
        self._ss = dt.second

    # adjusts the current RelativeTimeObject year value by the number defined in the offset
    def adjustYears(self, offset: int):
        self._yy += offset

    # snaps the current RelativeTimeObject to the year value
    def snapToYear(self):
        self._mo = 1
        self.snapToMonth()

    # adjusts the current RelativeTimeObject month value by the number defined in the offset
    #   if resulting month value is lt 1 or gt 12, calls adjustYears accordingly
    def adjustMonths(self, offset: int):
        self._mo += offset
        
        # if irrational month value, normalize months
        while self._mo > 12:
            self._mo -= 12
            self.adjustYears(1)
        while self._mo < 1:
            self._mo += 12
            self.adjustYears(-1)

    # snaps the current RelativeTimeObject to the month value
    def snapToMonth(self):
        self._dd = 1
        self.snapToDay()

    # adjusts the current RelativeTimeObject day value by the number defined in the offset
    def adjustDays(self, offset: int):
        self.__applyTimeDelta(timedelta(days=offset))

    # snaps the current RelativeTimeObject to the day value
    def snapToDay(self):
        self._hh = 0
        self.snapToHour()

    # adjusts the current RelativeTimeObject hour value by the number defined in the offset
    def adjustHours(self, offset: int):
        self.__applyTimeDelta(timedelta(hours=offset))

    # snaps the current RelativeTimeObject to the hour value
    def snapToHour(self):
        self._mi = 0
        self.snapToMinute()

    # adjusts the current RelativeTimeObject minute value by the number defined in the offset
    def adjustMinutes(self, offset: int):
        self.__applyTimeDelta(timedelta(minutes=offset))

    # snaps the current RelativeTimeObject to the minute value
    def snapToMinute(self):
        self._ss = 0
        self.snapToSecond()

    # adjusts the current RelativeTimeObject seconds value by the number defined in the offset
    def adjustSeconds(self, offset: int):
        self.__applyTimeDelta(timedelta(seconds=offset))

    # snaps the current RelativeTimeObject to the second value
    # note: as second is our maximum resolution, this does nothing
    #       the method has been kept as a placeholder in the event that resolution increases
    def snapToSecond(self):
        pass

    # helper function for day, hour, minute, and second adjustment methods
    # applies a generated timedelta to the current timestamp and extracts the
    # resulting values to the RelativeTimeObject
    def __applyTimeDelta(self, delta:timedelta):
        dt = self.toDatetime() + delta
        self.__fromDatetime(dt)