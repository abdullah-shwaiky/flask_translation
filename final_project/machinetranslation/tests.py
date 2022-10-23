import unittest

from translator import english_to_french, french_to_english

class TestE2F(unittest.TestCase):
    def test1(self):
        self.assertEqual(english_to_french(""), "")
        self.assertEqual(english_to_french("Hello"), "Bonjour")
        self.assertEqual(english_to_french("China"), "Chine")
class TestF2E(unittest.TestCase):
    def test2(self):
        self.assertEqual(french_to_english(""), "")
        self.assertEqual(french_to_english("Bonjour"), "Hello")
        self.assertEqual(french_to_english("Chine"), "China")

unittest.main()
