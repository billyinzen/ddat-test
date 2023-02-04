from .relative_time_object import RelativeTimeObject
import datetime
import unittest

class RelativeTimeObjectTests(unittest.TestCase):
    
    def test_should_create(self):
        test_case = datetime.datetime(1990, 2, 6, 11, 42, 12)
        rto = RelativeTimeObject(test_case)
        self.assertIsNotNone(rto)
        self.assertEqual(test_case, rto.toDatetime())

    #region Years

    def test_should_adjust_years(self):
        test_cases = [
            # initial, adjustment, expected
            [ datetime.datetime(1990, 2, 6, 11, 42, 12), 1, datetime.datetime(1991, 2, 6, 11, 42, 12) ],
            [ datetime.datetime(1990, 2, 6, 11, 42, 12), 10, datetime.datetime(2000, 2, 6, 11, 42, 12) ],
            [ datetime.datetime(1990, 2, 6, 11, 42, 12), -1, datetime.datetime(1989, 2, 6, 11, 42, 12) ],
            [ datetime.datetime(1990, 2, 6, 11, 42, 12), -40, datetime.datetime(1950, 2, 6, 11, 42, 12) ]
        ]
        for (initial, adjustment, expected) in test_cases:
            rto = RelativeTimeObject(initial)
            rto.adjustYears(adjustment)
            self.assertEqual(expected, rto.toDatetime())

    def test_should_snap_years(self):
        test_cases = [
            # initial, expected
            [ datetime.datetime(1990, 2, 6, 11, 42, 12), datetime.datetime(1990, 1, 1, 0, 0, 0) ],
            [ datetime.datetime(2023, 2, 4, 21, 39, 12), datetime.datetime(2023, 1, 1, 0, 0, 0) ],
        ]
        for (initial, expected) in test_cases:
            rto = RelativeTimeObject(initial)
            rto.snapToYear()
            self.assertEqual(expected, rto.toDatetime())

    #endregion
    
    #region Months

    def test_should_adjust_months(self):
        test_cases = [
            # initial, adjustment, expected
            [ datetime.datetime(2020, 6, 1, 0, 0, 0), 1, datetime.datetime(2020, 7, 1, 0, 0, 0) ],
            [ datetime.datetime(2020, 6, 1, 0, 0, 0), -1, datetime.datetime(2020, 5, 1, 0, 0, 0) ],
            [ datetime.datetime(2020, 6, 1, 0, 0, 0), 12, datetime.datetime(2021, 6, 1, 0, 0, 0) ],
            [ datetime.datetime(2020, 6, 1, 0, 0, 0), -28, datetime.datetime(2018, 2, 1, 0, 0, 0) ]
        ]
        for (initial, adjustment, expected) in test_cases:
            rto = RelativeTimeObject(initial)
            rto.adjustMonths(adjustment)
            self.assertEqual(expected, rto.toDatetime())


    def test_should_snap_months(self):
        test_cases = [
            # initial, expected
            [ datetime.datetime(1990, 2, 6, 11, 42, 12), datetime.datetime(1990, 2, 1, 0, 0, 0) ],
            [ datetime.datetime(2023, 10, 4, 21, 39, 12), datetime.datetime(2023, 10, 1, 0, 0, 0) ],
        ]
        for (initial, expected) in test_cases:
            rto = RelativeTimeObject(initial)
            rto.snapToMonth()
            self.assertEqual(expected, rto.toDatetime())

    #endregion

    #region Days

    def test_should_adjust_days(self):
        test_cases = [
            # case, initial, adjustment, expected
            [ 'add days', datetime.datetime(2020, 6, 1, 0, 0, 0), 1, datetime.datetime(2020, 6, 2, 0, 0, 0) ],
            [ 'subtract days', datetime.datetime(2020, 6, 1, 0, 0, 0), -1, datetime.datetime(2020, 5, 31, 0, 0, 0) ],
            [ 'add in february of leap year', datetime.datetime(2020, 2, 28, 0, 0, 0), 1, datetime.datetime(2020, 2, 29, 0, 0, 0) ],
            [ 'subtract into february of leap year', datetime.datetime(2021, 3, 1, 0, 0, 0), -1, datetime.datetime(2021, 2, 28, 0, 0, 0) ],
            [ 'add to cross year boundary', datetime.datetime(2021, 12, 31, 0, 0, 0), 1, datetime.datetime(2022, 1, 1, 0, 0, 0) ],
            [ 'subtract to cross year boundary', datetime.datetime(2021, 1, 1, 0, 0, 0), -100, datetime.datetime(2020, 9, 23, 0, 0, 0) ],
        ]
        for (_, initial, adjustment, expected) in test_cases:
            rto = RelativeTimeObject(initial)
            rto.adjustDays(adjustment)
            self.assertEqual(expected, rto.toDatetime())


    def test_should_snap_days(self):
        test_cases = [
            # initial, expected
            [ datetime.datetime(1990, 2, 6, 11, 42, 12), datetime.datetime(1990, 2, 6, 0, 0, 0) ],
            [ datetime.datetime(2023, 10, 4, 21, 39, 12), datetime.datetime(2023, 10, 4, 0, 0, 0) ],
        ]
        for (initial, expected) in test_cases:
            rto = RelativeTimeObject(initial)
            rto.snapToDay()
            self.assertEqual(expected, rto.toDatetime())

    #endregion

    #region Hours

    def test_should_adjust_hours(self):
        test_cases = [
            # initial, adjustment, expected
            [ 'add hours', datetime.datetime(2020, 6, 1, 12, 0, 0), 6, datetime.datetime(2020, 6, 1, 18, 0, 0) ],
            [ 'subtract hours', datetime.datetime(2020, 6, 1, 23, 0, 0), -24, datetime.datetime(2020, 5, 23, 0, 0, 0) ]
        ]
        for (_, initial, adjustment, expected) in test_cases:
            rto = RelativeTimeObject(initial)
            rto.adjustHours(adjustment)
            self.assertEqual(expected, rto.toDatetime())


    def test_should_adjust_hours(self):
        test_cases = [
            # initial, expected
            [ datetime.datetime(1990, 2, 6, 11, 42, 12), datetime.datetime(1990, 2, 6, 11, 0, 0) ],
            [ datetime.datetime(2023, 10, 4, 21, 39, 12), datetime.datetime(2023, 10, 4, 21, 0, 0) ],
        ]
        for (initial, expected) in test_cases:
            rto = RelativeTimeObject(initial)
            rto.snapToHour()
            self.assertEqual(expected, rto.toDatetime())

    #endregion

    #region Minutes

    def test_should_adjust_minutes(self):
        test_cases = [
            # initial, adjustment, expected
            [ datetime.datetime(2020, 6, 1, 12, 0, 0), 65, datetime.datetime(2020, 6, 1, 13, 5, 0) ],
            [ datetime.datetime(2020, 6, 1, 23, 59, 0), -12, datetime.datetime(2020, 6, 1, 23, 47, 0) ]
        ]
        for (initial, adjustment, expected) in test_cases:
            rto = RelativeTimeObject(initial)
            rto.adjustMinutes(adjustment)
            self.assertEqual(expected, rto.toDatetime())


    def test_should_adjust_minutes(self):
        test_cases = [
            # initial, expected
            [ datetime.datetime(1990, 2, 6, 11, 42, 12), datetime.datetime(1990, 2, 6, 11, 42, 0) ],
            [ datetime.datetime(2023, 10, 4, 21, 39, 12), datetime.datetime(2023, 10, 4, 21, 39, 0) ],
        ]
        for (initial, expected) in test_cases:
            rto = RelativeTimeObject(initial)
            rto.snapToMinute()
            self.assertEqual(expected, rto.toDatetime())

    #endregion

    #region Seconds

    def test_should_adjust_seconds(self):
        test_cases = [
            # initial, adjustment, expected
            [ datetime.datetime(2020, 6, 1, 12, 50, 0), 305, datetime.datetime(2020, 6, 1, 13, 55, 5) ],
            [ datetime.datetime(2020, 6, 1, 23, 59, 10), -20, datetime.datetime(2020, 6, 1, 23, 58, 50) ]
        ]
        for (initial, adjustment, expected) in test_cases:
            rto = RelativeTimeObject(initial)
            rto.adjustSeconds(adjustment)
            self.assertEqual(expected, rto.toDatetime())


    def test_should_adjust_seconds(self):
        test_cases = [
            # initial, expected
            [ datetime.datetime(1990, 2, 6, 11, 42, 12), datetime.datetime(1990, 2, 6, 11, 42, 12) ],
            [ datetime.datetime(2023, 10, 4, 21, 39, 12), datetime.datetime(2023, 10, 4, 21, 39, 12) ],
        ]
        for (initial, expected) in test_cases:
            rto = RelativeTimeObject(initial)
            rto.snapToSecond()
            self.assertEqual(expected, rto.toDatetime())

    #endregion

if __name__ == '__main__':
    unittest.main()