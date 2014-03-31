import datetime


def count_sundays_on_the_first_between(date1, date2):
    return _count_days_between_no_builtin_functions(date1, date2, lambda d: d.weekday == 7 and d.day == 1)
    #return _count_days_between_using_builtin_functions(
    #    datetime.date(date1.year, date1.month, date1.day),
    #    datetime.date(date2.year, date2.month, date2.day),
    #    lambda d : d.weekday() == 6 and d.day == 1)


def count_sundays_between(date1, date2):
    return _count_days_between_no_builtin_functions(date1, date2, lambda d: d.weekday == 7)
    #return _count_days_between_using_builtin_functions(
    #    datetime.date(date1.year, date1.month, date1.day),
    #    datetime.date(date2.year, date2.month, date2.day),
    #    lambda d: d.weekday() == 6
    #)


def _count_days_between_no_builtin_functions(date1, date2, filter_function):
    num_days = 0
    iter_date = date1
    while iter_date <= date2:
        if filter_function(iter_date):
            num_days += 1
        iter_date = iter_date.next_day()
    return num_days


def _count_days_between_using_builtin_functions(python_date1, python_date2, filter_function):
    num_days = 0
    iter_date = python_date1
    while iter_date <= python_date2:
        if filter_function(iter_date):
            num_days += 1
        iter_date += datetime.timedelta(days=1)
    return num_days


_default_days_per_month = {1: 31,
                           2: 28,
                           3: 31,
                           4: 30,
                           5: 31,
                           6: 30,
                           7: 31,
                           8: 31,
                           9: 30,
                           10: 31,
                           11: 30,
                           12: 31, }


class Date():
    def __init__(self, year, month, day, weekday=None):
        self._year = year
        self._month = month
        self._day = day
        self._weekday = weekday if weekday else self._calc_weekday()


    def _calc_weekday(self):
        earliest_supported_date = Date(1900, 1, 1, 1)
        iter_date = earliest_supported_date
        while self != iter_date:
            iter_date = iter_date.next_day()
        return iter_date._weekday

    @property
    def year(self):
        return self._year

    @property
    def month(self):
        return self._month

    @property
    def day(self):
        return self._day

    @property
    def weekday(self):
        return self._weekday

    def _next_weekday(self):
        return self._weekday % 7 + 1

    def next_day(self):
        if self._day < self._days_in_current_month():
            return Date(self.year, self.month, self.day + 1, self._next_weekday())
        elif self.month < 12:
            return Date(self.year, self.month + 1, 1, self._next_weekday())
        else:
            return Date(self.year + 1, 1, 1, self._next_weekday())

    def _days_in_current_month(self):
        if self.month != 2:
            return _default_days_per_month[self.month]
        elif self.is_in_leap_year():
            return 29
        else:
            return 28

    def is_in_leap_year(self):
        if self.year % 400 == 0:
            return True
        elif self.year % 100 == 0:
            return False
        elif self.year % 4 == 0:
            return True
        else:
            return False

    def __hash__(self):
        return self.year * 10000 + self.month * 100 + self.day

    def __cmp__(self, other):
        return self.__hash__() - other.__hash__()

