import unittest
import runner.csvgen as content
from datetime import datetime

class TestCSVMethods(unittest.TestCase):

    def test_date(self):
        date = content.getDate()
        self.assertTrue(str(datetime.now().day) in date)
        self.assertTrue(str(datetime.now().month) in date)
        self.assertTrue(str(datetime.now().year) in date)

    def test_csv(self):
        self.assertTrue("http" in content.generateCSV("http", 9, "Test reason"))
        self.assertTrue("9" in content.generateCSV("http", 9, "Test reason"))
        self.assertTrue("Test" in content.generateCSV("http", 9, "Test reason"))
        self.assertTrue("|" in content.generateCSV("http", 9, "Test reason"))
        self.assertTrue("reason" in content.generateCSV("http", 9, "Test reason"))

if __name__ == '__main__':
    unittest.main()