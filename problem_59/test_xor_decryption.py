import unittest
import os
from xor_decryption import decrypt


def encrypt(message, key):
    for i in xrange(len(message)):
        c1 = ord(message[i])
        c2 = ord(key[i % len(key)])
        yield c1 ^ c2


class XorDecryptionTest(unittest.TestCase):
    def test_decrypt_single_char_key(self):
        self.assertEqual("in the fire", decrypt(encrypt('in the fire', 'A'), 1).lower())
        self.assertEqual("in the moment", decrypt(encrypt('in the moment', 'A'), 1).lower())
        self.assertEqual("in the mood", decrypt(encrypt('in the mood', 'B'), 1).lower())
        self.assertEqual("in the midst", decrypt(encrypt('in the midst', 'C'), 1).lower())

    def test_decrypt_two_char_key(self):
        self.assertEqual("in the fire", decrypt(encrypt('in the fire', 'AB'), 2).lower())
        self.assertEqual("in the mood", decrypt(encrypt('in the mood', 'BA'), 2).lower())
        self.assertEqual("in the midst", decrypt(encrypt('in the midst', 'CD'), 2).lower())

    def test_project_euler(self):
        infile = open(os.path.join(os.path.dirname(__file__), 'cipher1.txt'))
        encrypted = map(int, infile.read().split(","))
        infile.close()
        res = sum(map(ord, decrypt(encrypted, 3)))
        self.assertEqual(107359, res)


if __name__ == '__main__':
    unittest.main()
