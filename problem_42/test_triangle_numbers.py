import os
import unittest

from triangle_numbers import *


class IsTriangleWordTest(unittest.TestCase):
    def test_is_triangle_word(self):
        self.assertTrue(is_triangle_word("a"))
        self.assertTrue(is_triangle_word("c"))
        self.assertTrue(is_triangle_word("aaa"))
        self.assertTrue(is_triangle_word("ab"))
        self.assertTrue(is_triangle_word("sky"))
        self.assertTrue(is_triangle_word("A"))
        self.assertTrue(is_triangle_word("C"))
        self.assertTrue(is_triangle_word("AAA"))
        self.assertTrue(is_triangle_word("AB"))
        self.assertTrue(is_triangle_word("SKY"))

    def test_is_not_triangle_word(self):
        self.assertFalse(is_triangle_word("b"))
        self.assertFalse(is_triangle_word("aa"))
        self.assertFalse(is_triangle_word("aab"))
        self.assertFalse(is_triangle_word("B"))
        self.assertFalse(is_triangle_word("AA"))
        self.assertFalse(is_triangle_word("AAB"))

    def test_project_euler(self):
        infile = open(os.path.join(os.path.dirname(__file__), 'words.txt'))
        words = infile.read().replace('"', '').split(",")
        infile.close()
        words_that_are_triangle_numbers = filter(is_triangle_word, words)
        self.assertEqual(len(words_that_are_triangle_numbers), 162)


if __name__ == '__main__':
    unittest.main()
