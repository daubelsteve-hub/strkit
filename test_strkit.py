import unittest

from strkit import reverse_string


class TestStrkit(unittest.TestCase):
    def test_reverse_string(self):
        self.assertEqual(reverse_string("hello"), "olleh")
        self.assertEqual(reverse_string(""), "")


if __name__ == "__main__":
    unittest.main()
