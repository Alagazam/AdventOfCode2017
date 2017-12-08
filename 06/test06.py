# pylint: disable=missing-docstring

import unittest
from day06 import Realloc

class Test05(unittest.TestCase):

    def test_maxindex(self):
        self.assertEqual(2, Realloc.maxindex([0, 2, 7, 0]))
        self.assertEqual(1, Realloc.maxindex([2, 4, 1, 2]))
        self.assertEqual(0, Realloc.maxindex([3, 1, 2, 3]))
        self.assertEqual(3, Realloc.maxindex([0, 2, 3, 4]))

    def test_redistribute(self):
        self.assertEqual([2, 4, 1, 2], Realloc.redistribute([0, 2, 7, 0]))
        self.assertEqual([3, 1, 2, 3], Realloc.redistribute([2, 4, 1, 2]))
        self.assertEqual([0, 2, 3, 4], Realloc.redistribute([3, 1, 2, 3]))
        self.assertEqual([1, 3, 4, 1], Realloc.redistribute([0, 2, 3, 4]))
        self.assertEqual([2, 4, 1, 2], Realloc.redistribute([1, 3, 4, 1]))

    def test_find_loop(self):
        testdata = [0, 2, 7, 0]
        self.assertEqual((5, 4), Realloc.find_loop(testdata))

if __name__ == '__main__':
    unittest.main()
