# pylint: disable=missing-docstring

import unittest
from day04 import PassPhraseCheck

class Test04(unittest.TestCase):
    def test_check_pass_valid(self):
        self.assertTrue(PassPhraseCheck.is_pass_phrase_valid("aa bb cc dd ee"))
        self.assertFalse(PassPhraseCheck.is_pass_phrase_valid("aa bb cc dd aa"))
        self.assertTrue(PassPhraseCheck.is_pass_phrase_valid("aa bb cc dd aaa"))

    def test_check_pass_phrases(self):
        testdata = ["aa bb cc dd ee", "aa bb cc dd aa", "aa bb cc dd aaa"]
        self.assertEqual(2, PassPhraseCheck.check_pass_phrases(testdata))

if __name__ == '__main__':
    unittest.main()
