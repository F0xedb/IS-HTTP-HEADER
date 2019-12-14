
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
import runner.headers.CookieHeader as content
import runner.config

class TestCookieMethods(unittest.TestCase):

    def test_with_random_data(self):
        header = content.CookieHeader("abc", None)
        header2 = content.CookieHeader("", None)
        header3 = content.CookieHeader("-z-ad-q-dz", None)
        header4 = content.CookieHeader(None, None)
        header5 = content.CookieHeader(1, None)
        self.assertEqual(header.score(), 9)
        self.assertEqual(header2.score(), 9)
        self.assertEqual(header3.score(), 9)
        self.assertEqual(header4.score(), 9)
        self.assertEqual(header5.score(), 9)

    def test_with_nothing(self):
        self.assertEqual(content.CookieHeader.missingScore, runner.config.MISSING_SCORE_COOKIE)

if __name__ == '__main__':
    unittest.main()