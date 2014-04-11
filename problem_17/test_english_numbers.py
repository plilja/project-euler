import unittest

from english_numbers import *


class TestEnglishNumbers(unittest.TestCase):
    def test_digits(self):
        self.assertEqual('zero', english_number(0))
        self.assertEqual('one', english_number(1))
        self.assertEqual('two', english_number(2))
        self.assertEqual('three', english_number(3))
        self.assertEqual('four', english_number(4))
        self.assertEqual('five', english_number(5))
        self.assertEqual('six', english_number(6))
        self.assertEqual('seven', english_number(7))
        self.assertEqual('eight', english_number(8))
        self.assertEqual('nine', english_number(9))

    def test_10_through_19(self):
        self.assertEqual('ten', english_number(10))
        self.assertEqual('eleven', english_number(11))
        self.assertEqual('twelve', english_number(12))
        self.assertEqual('thirteen', english_number(13))
        self.assertEqual('fourteen', english_number(14))
        self.assertEqual('fifteen', english_number(15))
        self.assertEqual('sixteen', english_number(16))
        self.assertEqual('seventeen', english_number(17))
        self.assertEqual('eighteen', english_number(18))
        self.assertEqual('nineteen', english_number(19))

    def test_20_through_29(self):
        self.assertEqual('twenty', english_number(20))
        self.assertEqual('twenty-one', english_number(21))
        self.assertEqual('twenty-two', english_number(22))
        self.assertEqual('twenty-three', english_number(23))
        self.assertEqual('twenty-four', english_number(24))
        self.assertEqual('twenty-five', english_number(25))
        self.assertEqual('twenty-six', english_number(26))
        self.assertEqual('twenty-seven', english_number(27))
        self.assertEqual('twenty-eight', english_number(28))
        self.assertEqual('twenty-nine', english_number(29))

    def test_between_30_and_39(self):
        self.assertEqual('thirty', english_number(30))
        self.assertEqual('thirty-five', english_number(35))
        self.assertEqual('thirty-nine', english_number(39))

    def test_between_100_and_199(self):
        self.assertEqual('one hundred', english_number(100))
        self.assertEqual('one hundred and one', english_number(101))
        self.assertEqual('one hundred and three', english_number(103))
        self.assertEqual('one hundred and eight', english_number(108))
        self.assertEqual('one hundred and nine', english_number(109))
        self.assertEqual('one hundred and twenty-nine', english_number(129))
        self.assertEqual('one hundred and eighty-eight', english_number(188))
        self.assertEqual('one hundred and ninety-nine', english_number(199))

    def test_between_200_and_299(self):
        self.assertEqual('two hundred', english_number(200))
        self.assertEqual('two hundred and one', english_number(201))
        self.assertEqual('two hundred and twenty-three', english_number(223))
        self.assertEqual('two hundred and forty-five', english_number(245))
        self.assertEqual('two hundred and sixty-five', english_number(265))
        self.assertEqual('two hundred and seventy-two', english_number(272))

    def test_between_300_and_999(self):
        self.assertEqual('three hundred', english_number(300))
        self.assertEqual('four hundred and forty', english_number(440))
        self.assertEqual('five hundred and forty-three', english_number(543))
        self.assertEqual('six hundred and thirty-one', english_number(631))
        self.assertEqual('seven hundred and nine', english_number(709))
        self.assertEqual('eight hundred and ninety-four', english_number(894))
        self.assertEqual('nine hundred and ninety-nine', english_number(999))

    def test_larger_than_1000(self):
        self.assertEqual('one thousand', english_number(1000))
        self.assertEqual('one thousand and one', english_number(1001))
        self.assertEqual('one thousand and twenty', english_number(1020))
        self.assertEqual('one thousand one hundred and twenty', english_number(1120))
        self.assertEqual('two thousand', english_number(2000))
        self.assertEqual('eight thousand seven hundred and thirty-four', english_number(8734))
        self.assertEqual('nine thousand nine hundred and ninety-nine', english_number(9999))


class TestProjectEuler(unittest.TestCase):
    def test_1_through_5(self):
        self.assertEqual(19, len_numbers(range(1, 6)))

    def test_342(self):
        self.assertEqual(23, len_numbers([342]))

    def test_115(self):
        self.assertEqual(20, len_numbers([115]))

    def test_1_through_1000(self):
        self.assertEqual(21124, len_numbers(range(1, 1001)))


if __name__ == '__main__':
    unittest.main()
