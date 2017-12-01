import unittest
from day01 import captcha

class Test_test01(unittest.TestCase):
    def test_calculate1a(self):
        self.assertEqual(3, captcha.calculate("1122"))

    def test_calculate1b(self):
        self.assertEqual(4, captcha.calculate("1111"))

    def test_calculate1c(self):
        self.assertEqual(0, captcha.calculate("1234"))

    def test_calculate1d(self):
        self.assertEqual(9, captcha.calculate("91212129"))

class Test_test02(unittest.TestCase):
    def test_calculate2a(self):
        self.assertEqual(6, captcha.calculate2("1212"))

    def test_calculate2b(self):
        self.assertEqual(0, captcha.calculate2("1221"))

    def test_calculate2c(self):
        self.assertEqual(4, captcha.calculate2("123425"))

    def test_calculate2e(self):
        self.assertEqual(12, captcha.calculate2("123123"))

    def test_calculate2f(self):
        self.assertEqual(4, captcha.calculate2("12131415"))

if __name__ == '__main__':
    unittest.main()
