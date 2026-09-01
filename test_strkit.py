import unittest

from strkit import is_palindrome, reverse_string


class TestStrkit(unittest.TestCase):
    def test_reverse_string(self):
        self.assertEqual(reverse_string("hello"), "olleh")
        self.assertEqual(reverse_string(""), "")

    def test_is_palindrome(self):
        self.assertTrue(is_palindrome("Race car"))
        self.assertTrue(is_palindrome(""))
        self.assertFalse(is_palindrome("hello"))


if __name__ == "__main__":
    unittest.main()
