import unittest
from src.Regex import *


class MyTestCase(unittest.TestCase):

    def test_CN1(self):
        self.assertRegexpMatches(contactNameExp, contactNamePattern, "Did not match!")


if __name__ == '__main__':
    unittest.main()
