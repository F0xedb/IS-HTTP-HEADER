
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
import runner.headers.DateHeader as content
import runner.config

class TestDateMethods(unittest.TestCase):

    def test_with_date(self):
        header = content.DateHeader("Sat, 14 Dec 2019 18:39:15 GMT", None)
        self.assertEqual(header.score(), 5)

    def test_with_none_RFC_7231_date(self):
        header = content.DateHeader("14-12-2019 18:39:15 GMT", None)
        self.assertEqual(header.score(), 5)
        self.assertEqual(header.reason, "Date format is not defined as per RFC 7231")

    def test_with_nothing(self):
        header = content.DateHeader("", None)
        self.assertEqual(content.DateHeader.missingScore, runner.config.MISSING_SCORE_DATE)

if __name__ == '__main__':
    unittest.main()