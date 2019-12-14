
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
import runner.headers.XSSHeader as content
import runner.config

class TestContentEncodingMethods(unittest.TestCase):

    def test_with_zero(self):
        header = content.XSSHeader("0", None)
        self.assertEqual(header.score(), 10)

    def test_with_block(self):
        header = content.XSSHeader("1; block", None)
        self.assertEqual(header.score(), 10)

    def test_with_zero_error_sytax(self):
        header = content.XSSHeader("0;", None)
        self.assertEqual(header.score(), 0)

    def test_with_block_extra_syntax(self):
        header = content.XSSHeader("1;block", None)
        self.assertEqual(header.score(), 10)

    def test_with_error(self):
        header = content.XSSHeader("1", None)
        self.assertEqual(header.score(), 0)
        header = content.XSSHeader("", None)
        self.assertEqual(header.score(), 0)
        header = content.XSSHeader(";", None)
        self.assertEqual(header.score(), 0)
        header = content.XSSHeader("123", None)
        self.assertEqual(header.score(), 0)
        header = content.XSSHeader("nop", None)
        self.assertEqual(header.score(), 0)

    def test_with_nothing(self):
        self.assertEqual(content.XSSHeader.missingScore, runner.config.MISSING_SCORE_XSS)

if __name__ == '__main__':
    unittest.main()