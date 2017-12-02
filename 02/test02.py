# pylint: disable=missing-docstring

import unittest
from day02 import Checksum

class Test02(unittest.TestCase):

    def test_checksum(self):
        testdata1 = ["5\t1\t9\t5", "7\t5\t3", "2\t4\t6\t8"]
        self.assertEqual(18, Checksum.calculate1(testdata1))

    def test_divisible(self):
        self.assertEqual((True, 5), Checksum.divisible(10, 2))
        self.assertEqual((False, 0), Checksum.divisible(10, 3))
        self.assertEqual((True, 4), Checksum.divisible(2, 8))
        self.assertEqual((False, 0), Checksum.divisible(5, 8))

    def test_checksum2(self):
        testdata2 = ["5\t9\t2\t8", "9\t4\t7\t3", "3\t8\t6\t5"]
        self.assertEqual(9, Checksum.calculate2(testdata2))

if __name__ == '__main__':
    unittest.main()
