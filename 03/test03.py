# pylint: disable=missing-docstring

import unittest
from day03 import Manhattan

class Test03(unittest.TestCase):
    def test_coordinate(self):
        self.assertEqual((0, 0), Manhattan.coordinate(1))
        self.assertEqual((1, 0), Manhattan.coordinate(2))
        self.assertEqual((1, 1), Manhattan.coordinate(3))
        self.assertEqual((0, 1), Manhattan.coordinate(4))
        self.assertEqual((-1, 1), Manhattan.coordinate(5))
        self.assertEqual((-1, 0), Manhattan.coordinate(6))
        self.assertEqual((-1, -1), Manhattan.coordinate(7))
        self.assertEqual((0, -1), Manhattan.coordinate(8))
        self.assertEqual((1, -1), Manhattan.coordinate(9))
        self.assertEqual((2, -1), Manhattan.coordinate(10))
        self.assertEqual((-2, 2), Manhattan.coordinate(17))
        self.assertEqual((-2, -1), Manhattan.coordinate(20))
        self.assertEqual((1, -2), Manhattan.coordinate(24))

    def test_distance1(self):
        self.assertEqual(0, Manhattan.distance1(1))
        self.assertEqual(3, Manhattan.distance1(12))
        self.assertEqual(2, Manhattan.distance1(23))
        self.assertEqual(31, Manhattan.distance1(1024))

#    def test_distance2(self):
#        self.fail("Not implemented")

if __name__ == '__main__':
    unittest.main()
