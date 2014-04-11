from unittest import TestCase

from largest_product import *


class TestLargestProductInSeries(TestCase):
    def test_largest_1_digit_product_in_1_digit_number_digit_number_is_the_number_itself(self):
        self.assertEqual(largest_product_in_series(1, '5'), 5)
        self.assertEqual(largest_product_in_series(1, '8'), 8)

    def test_largest_1_digit_product_in_2_digit_number_digit_number_is_the_greatest_digit(self):
        self.assertEqual(largest_product_in_series(1, '55'), 5)
        self.assertEqual(largest_product_in_series(1, '66'), 6)
        self.assertEqual(largest_product_in_series(1, '65'), 6)
        self.assertEqual(largest_product_in_series(1, '56'), 6)

    def test_largest_2_digit_product_in_3_digit_number_is_the_digits_multiplied_by_each_other(self):
        self.assertEqual(largest_product_in_series(2, '55'), 25)
        self.assertEqual(largest_product_in_series(2, '66'), 36)
        self.assertEqual(largest_product_in_series(2, '56'), 30)
        self.assertEqual(largest_product_in_series(2, '65'), 30)

    def test_largest_3_digit_product_in_3_digit_number_is_the_digits_multiplied_by_each_other(self):
        self.assertEqual(largest_product_in_series(3, '222'), 8)
        self.assertEqual(largest_product_in_series(3, '333'), 27)
        self.assertEqual(largest_product_in_series(3, '323'), 18)

    def test_largest_2_digit_product_in_3_digit_number(self):
        self.assertEqual(largest_product_in_series(2, '222'), 4)
        self.assertEqual(largest_product_in_series(2, '333'), 9)
        self.assertEqual(largest_product_in_series(2, '332'), 9)
        self.assertEqual(largest_product_in_series(2, '233'), 9)
        self.assertEqual(largest_product_in_series(2, '323'), 6)
        self.assertEqual(largest_product_in_series(2, '303'), 0)
        self.assertEqual(largest_product_in_series(2, '033'), 9)
        self.assertEqual(largest_product_in_series(2, '330'), 9)

    def test_largest_3_digit_product_in_63683278_is_144(self):
        self.assertEqual(largest_product_in_series(3, '63683278'), 144)

    def test_largest_4_digit_product_in_448715875_is_1400(self):
        self.assertEqual(largest_product_in_series(4, '448715875'), 1400)

    def test_project_euler_case(self):
        inp = """73167176531330624919225119674426574742355349194934
96983520312774506326239578318016984801869478851843
85861560789112949495459501737958331952853208805511
12540698747158523863050715693290963295227443043557
66896648950445244523161731856403098711121722383113
62229893423380308135336276614282806444486645238749
30358907296290491560440772390713810515859307960866
70172427121883998797908792274921901699720888093776
65727333001053367881220235421809751254540594752243
52584907711670556013604839586446706324415722155397
53697817977846174064955149290862569321978468622482
83972241375657056057490261407972968652414535100474
82166370484403199890008895243450658541227588666881
16427171479924442928230863465674813919123162824586
17866458359124566529476545682848912883142607690042
24219022671055626321111109370544217506941658960408
07198403850962455444362981230987879927244284909188
84580156166097919133875499200524063689912560717606
05886116467109405077541002256983155200055935729725
71636269561882670428252483600823257530420752963450"""
        inp = inp.replace('\n', '')
        self.assertEqual(largest_product_in_series(5, inp), 40824)

