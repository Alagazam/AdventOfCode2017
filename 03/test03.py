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


    def test_grid_init(self):
        testgrid = Grid(25)
        self.assertEqual(51*51, len(testgrid.matrix)*len(testgrid.matrix[0]))

    def test_grid_setget(self):
        testgrid = Grid(25)
        testgrid.Set(5,-5,5)
        testgrid.Set(25,25,25)
        testgrid.Set(-25,-25,-25)
        self.assertEqual(5, testgrid.Get(5,-5))
        self.assertEqual(25, testgrid.Get(25,25))
        self.assertEqual(-25, testgrid.Get(-25,-25))
        self.assertRaises(IndexError, testgrid.Get, 26, -26)
        self.assertRaises(IndexError, testgrid.Get, -26, 26)
        self.assertRaises(IndexError, testgrid.Set, 26, -26, 1)
        self.assertRaises(IndexError, testgrid.Set, -26, 26, 2)

#    def test_distance2(self):
#        self.fail("Not implemented")

if __name__ == '__main__':
    unittest.main()
