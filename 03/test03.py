# pylint: disable=missing-docstring

import unittest
from day03 import Manhattan
from day03 import Grid

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

    def test_distance2(self):
        self.assertEqual(0, Manhattan.distance2(1))
        self.assertEqual(3, Manhattan.distance2(12))
        self.assertEqual(2, Manhattan.distance2(23))
        self.assertEqual(31, Manhattan.distance2(1024))

    def test_first_larger(self):
        self.assertEqual(1, Manhattan.first_larger(1))
        self.assertEqual(23, Manhattan.first_larger(12))
        self.assertEqual(122, Manhattan.first_larger(100))
        self.assertEqual(747, Manhattan.first_larger(700))

    def test_grid_init(self):
        testgrid = Grid(25)
        self.assertEqual(51*51, len(testgrid.matrix)*len(testgrid.matrix[0]))

    def test_grid_setget(self):
        testgrid = Grid(25)
        testgrid.set(5, -5, 5)
        testgrid.set(25, 25, 25)
        testgrid.set(-25, -25, -25)
        self.assertEqual(5, testgrid.get(5, -5))
        self.assertEqual(25, testgrid.get(25, 25))
        self.assertEqual(-25, testgrid.get(-25, -25))
        self.assertRaises(IndexError, testgrid.get, 26, -26)
        self.assertRaises(IndexError, testgrid.get, -26, 26)
        self.assertRaises(IndexError, testgrid.set, 26, -26, 1)
        self.assertRaises(IndexError, testgrid.set, -26, 26, 2)

#    def test_distance2(self):
#        self.fail("Not implemented")

if __name__ == '__main__':
    unittest.main()
