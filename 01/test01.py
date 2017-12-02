# pylint: disable=missing-docstring

import unittest

from day01 import Captcha

class Test01(unittest.TestCase):
    def test_calculate1a(self):
        self.assertEqual(3, Captcha.calculate1("1122"))

    def test_calculate1b(self):
        self.assertEqual(4, Captcha.calculate1("1111"))

    def test_calculate1c(self):
        self.assertEqual(0, Captcha.calculate1("1234"))

    def test_calculate1d(self):
        self.assertEqual(9, Captcha.calculate1("91212129"))

class Test02(unittest.TestCase):
    def test_calculate2a(self):
        self.assertEqual(6, Captcha.calculate2("1212"))

    def test_calculate2b(self):
        self.assertEqual(0, Captcha.calculate2("1221"))

    def test_calculate2c(self):
        self.assertEqual(4, Captcha.calculate2("123425"))

    def test_calculate2e(self):
        self.assertEqual(12, Captcha.calculate2("123123"))

    def test_calculate2f(self):
        self.assertEqual(4, Captcha.calculate2("12131415"))

if __name__ == '__main__':
    unittest.main()
