import unittest
from day02 import checksum

class Test_test02(unittest.TestCase):

    def test_checksum(self):
        testdata1 = ["5\t1\t9\t5", "7\t5\t3", "2\t4\t6\t8"]
        self.assertEqual(18, checksum.calculate(testdata1))

    def test_checksum2(self):
        testdata2 = ["5\t9\t2\t8", "9\t4\t7\t3", "3\t8\t6\t5"]
        self.assertEqual(9, checksum.calculate2(testdata2))

if __name__ == '__main__':
    unittest.main()
