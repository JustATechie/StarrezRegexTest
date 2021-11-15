import unittest
from src.Regex import *

ValidNames = ["Louie DiBernardo", "Louie-Louie DiBernardo", "Jef Mendoza", "Tom-Hatherford Hatherford-Tom",
              "Sanddhya Jayabalan"]

InvalidNames = ["\0", ".", "<none>", "N/A", " ", "-", " -", "- ", " - ", "Louie-Louie ", "Tom Tom-",
               "Bistro-Diner Apple-Juice'", "123", "Mom2", "*", "LDIBERN1"]

ValidPhoneNumbers = []


class MyTestCase(unittest.TestCase):

    def testValidNames(self):
        for i in ValidNames:
            self.assertRegex(i, contactNamePattern, "Did not match!")

    def testInvalidNames(self):
        for i in InvalidNames:
            self.assertNotRegex(i, contactNamePattern, "Did match!")




if __name__ == '__main__':
    unittest.main()
