import unittest

from counting_sundays import *


class TestCountingDays(unittest.TestCase):
    def test_zero_sundays(self):
        self.assertEqual(count_sundays_between(Date(1900, 1, 1), Date(1900, 1, 1)), 0)
        self.assertEqual(count_sundays_between(Date(1900, 1, 1), Date(1900, 1, 6)), 0)

    def test_one_sunday(self):
        self.assertEqual(count_sundays_between(Date(1900, 1, 1), Date(1900, 1, 7)), 1)
        self.assertEqual(count_sundays_between(Date(1900, 1, 1), Date(1900, 1, 9)), 1)
        self.assertEqual(count_sundays_between(Date(1900, 1, 6), Date(1900, 1, 8)), 1)

    def test_two_sundays(self):
        self.assertEqual(count_sundays_between(Date(1900, 1, 6), Date(1900, 1, 14)), 2)
        self.assertEqual(count_sundays_between(Date(1900, 1, 6), Date(1900, 1, 19)), 2)

    def test_over_turn_of_month(self):
        self.assertEqual(count_sundays_between(Date(2014, 3, 30), Date(2014, 4, 6)), 2)
        self.assertEqual(count_sundays_between(Date(2014, 2, 28), Date(2014, 3, 16)), 3)
        self.assertEqual(count_sundays_between(Date(2014, 8, 30), Date(2014, 9, 3)), 1)
        self.assertEqual(count_sundays_between(Date(2014, 11, 30), Date(2014, 12, 1)), 1)

    def test_over_turn_of_year(self):
        self.assertEqual(count_sundays_between(Date(1950, 12, 31), Date(1951, 1, 1)), 1)
        self.assertEqual(count_sundays_between(Date(1978, 12, 4), Date(1979, 1, 18)), 6)

    def test_over_leap_day(self):
        self.assertEqual(count_sundays_between(Date(1920, 2, 28), Date(1920, 3, 1)), 1)

    def test_over_turn_of_february_century_not_divisable_by_400(self):
        self.assertEqual(count_sundays_between(Date(1900, 2, 28), Date(1900, 3, 7)), 1)

    def test_one_year(self):
        self.assertEqual(count_sundays_between(Date(2014, 1, 1), Date(2014, 12, 31)), 52)

    def test_two_years(self):
        self.assertEqual(count_sundays_between(Date(2013, 1, 1), Date(2014, 12, 31)), 104)

    def test_project_euler_input(self):
        self.assertEqual(count_sundays_between(Date(1900, 1, 1), Date(2000, 12, 31)), 5270)


if __name__ == '__main__':
    unittest.main()
