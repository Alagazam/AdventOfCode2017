# pylint: disable=missing-docstring

import unittest
from day04 import PassPhraseCheck

class Test04(unittest.TestCase):
    def test_check_pass_valid1(self):
        self.assertTrue(PassPhraseCheck.is_pass_phrase_valid1("aa bb cc dd ee"))
        self.assertFalse(PassPhraseCheck.is_pass_phrase_valid1("aa bb cc dd aa"))
        self.assertTrue(PassPhraseCheck.is_pass_phrase_valid1("aa bb cc dd aaa"))

    def test_check_pass_valid2(self):
        self.assertTrue(PassPhraseCheck.is_pass_phrase_valid2("aa bb cc dd ee"))
        self.assertFalse(PassPhraseCheck.is_pass_phrase_valid2("aa bb cc dd aa"))
        self.assertTrue(PassPhraseCheck.is_pass_phrase_valid2("aa bb cc dd aaa"))

        self.assertTrue(PassPhraseCheck.is_pass_phrase_valid2("abcde fghij"))
        self.assertFalse(PassPhraseCheck.is_pass_phrase_valid2("abcde xyz ecdab"))
        self.assertTrue(PassPhraseCheck.is_pass_phrase_valid2("a ab abc abd abf abj"))
        self.assertTrue(PassPhraseCheck.is_pass_phrase_valid2("iiii oiii ooii oooi oooo"))
        self.assertFalse(PassPhraseCheck.is_pass_phrase_valid2("oiii ioii iioi iiio"))

    def test_check_pass_phrases(self):
        testdata = ["aa bb cc dd ee", "aa bb cc dd aa", "aa bb cc dd aaa", "oiii ioii iioi iiio"]
        self.assertEqual((3, 2), PassPhraseCheck.check_pass_phrases(testdata))

if __name__ == '__main__':
    unittest.main()
