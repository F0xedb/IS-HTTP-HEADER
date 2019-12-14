
# MIT License
# 
# Copyright (c) 2019 Meyers Tom
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
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