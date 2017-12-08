# pylint: disable=missing-docstring

import unittest
from day05 import Trampolines

class Test05(unittest.TestCase):
    def test_jumpsteps1(self):
        self.assertEqual(5, Trampolines.jumpsteps1([0, 3, 0, 1, -3]))

if __name__ == '__main__':
    unittest.main()
