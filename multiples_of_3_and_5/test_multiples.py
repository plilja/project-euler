from unittest import TestCase

from multiples import *


class TestMultiplesOf3And5(TestCase):
    def test_no_multiples(self):
        self.assertEqual(multiples_of_3_and_5(0), 0)
        self.assertEqual(multiples_of_3_and_5(1), 0)
        self.assertEqual(multiples_of_3_and_5(2), 0)
        self.assertEqual(multiples_of_3_and_5(3), 0)

    def test_one_multiple(self):
        self.assertEqual(multiples_of_3_and_5(4), 3)
        self.assertEqual(multiples_of_3_and_5(5), 3)

    def test_two_multiples(self):
        self.assertEqual(multiples_of_3_and_5(6), 8)

    def test_three_multiples(self):
        self.assertEqual(multiples_of_3_and_5(7), 14)

    def test_up_to_10(self):
        self.assertEqual(multiples_of_3_and_5(10), 3 + 5 + 6 + 9)

    def test_up_to_20(self):
        self.assertEqual(multiples_of_3_and_5(20), 3 + 5 + 6 + 9 + 10 + 12 + 15 + 18)

    def test_up_to_1000(self):
        self.assertEqual(multiples_of_3_and_5(1000), 233168)
