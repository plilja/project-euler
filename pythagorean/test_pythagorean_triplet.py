import unittest

from pythagorean_triplet import pythagorean_triplet


class MyTestCase(unittest.TestCase):
    def test_should_fail_when_sum_is_0_or_less(self):
        for i in range(-10, 0, 1):
            with self.assertRaises(ValueError):
                pythagorean_triplet(i)

    def test_when_sum_equals_20_no_solution_exists(self):
        self.assertEqual(pythagorean_triplet(20), [])

    def test_when_sum_equals_14_no_solution_exists(self):
        self.assertEqual(pythagorean_triplet(14), [])

    def test_when_sum_equals_25_numbers_should_equal_3_4_5(self):
        self.assertEqual(pythagorean_triplet(12), [(3, 4, 5)])

    def test_when_sum_equals_1000_numbers_should_equal_3_4_5(self):
        self.assertEqual(pythagorean_triplet(1000), [(200, 375, 425)])
        print("Answer to problem is %s" % (200 * 375 * 425))


if __name__ == '__main__':
    unittest.main()
