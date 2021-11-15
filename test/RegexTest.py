import unittest
from src.Regex import *


CN1 = "Louie DiBernardo"


class MyTestCase(unittest.TestCase):

    def test_CN1(self):
        self.assertRegex(CN1, contactNamePattern, "Did not match!")


if __name__ == '__main__':
    unittest.main()
