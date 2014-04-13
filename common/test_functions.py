import unittest

from functions import *


class TestFactorial(unittest.TestCase):
    def test_factorial(self):
        self.assertEqual(factorial(1), 1)
        self.assertEqual(factorial(2), 2)
        self.assertEqual(factorial(3), 6)
        self.assertEqual(factorial(4), 24)
        self.assertEqual(factorial(5), 120)
        self.assertEqual(factorial(6), 720)
        self.assertEqual(factorial(20), 2432902008176640000)


class TestFibonacci(unittest.TestCase):
    def test_fibonacci(self):
        self.assertEqual(fibonacci(1), 1)
        self.assertEqual(fibonacci(2), 1)
        self.assertEqual(fibonacci(3), 2)
        self.assertEqual(fibonacci(4), 3)
        self.assertEqual(fibonacci(5), 5)
        self.assertEqual(fibonacci(12), 144)
        self.assertEqual(fibonacci(40), 102334155)


class TestNumberAsDigits(unittest.TestCase):
    def test_number_as_digits(self):
        self.assertEqual(number_as_digits(1), [1])
        self.assertEqual(number_as_digits(0), [0])
        self.assertEqual(number_as_digits(3), [3])
        self.assertEqual(number_as_digits(10), [1, 0])
        self.assertEqual(number_as_digits(101), [1, 0, 1])
        self.assertEqual(number_as_digits(901952842935213741234153143120),
                         [9, 0, 1, 9, 5, 2, 8, 4, 2, 9, 3, 5, 2, 1, 3, 7, 4, 1, 2, 3, 4, 1, 5, 3, 1, 4, 3, 1, 2, 0])


if __name__ == '__main__':
    unittest.main()
