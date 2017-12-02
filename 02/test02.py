import unittest
from day02 import checksum

class Test_test02(unittest.TestCase):

    testdata = ["5\t1\t9\t5", "7\t5\t3", "2\t4\t6\t8"]

    def test_checksum(self):
        self.assertEqual(18, checksum.calculate(self.testdata))

if __name__ == '__main__':
    unittest.main()
