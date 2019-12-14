
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
import runner.headers.XFrameHeader as content
import runner.config

class TestXFrameMethods(unittest.TestCase):

    def test_sameorigin(self):
        header = content.XFrameHeader("SAMEORIGIN", None)
        self.assertEqual(header.score(), 9)

    def test_sameorigin_lower(self):
        header = content.XFrameHeader("sameorigin", None)
        self.assertEqual(header.score(), 9)

    def test_deny(self):
        header = content.XFrameHeader("DENY", None)
        self.assertEqual(header.score(), 10)

    def test_deny_lower(self):
        header = content.XFrameHeader("deny", None)
        self.assertEqual(header.score(), 10)

    def test_allow_from(self):
        header = content.XFrameHeader("allow-from", None)
        self.assertEqual(header.score(), 5)
    
    def test_allow_from_upper(self):
        header = content.XFrameHeader("ALLOW-FROM", None)
        self.assertEqual(header.score(), 5)

    def test_allow_all(self):
        header = content.XFrameHeader("allow-all", None)
        self.assertEqual(header.score(), 3)
    
    def test_allow_all_upper(self):
        header = content.XFrameHeader("ALLOW-ALL", None)
        self.assertEqual(header.score(), 3)

    def test_unknown(self):
        header = content.XFrameHeader("", None)
        self.assertEqual(header.score(), 3)
        header = content.XFrameHeader("---", None)
        self.assertEqual(header.score(), 3)
        header = content.XFrameHeader("abc", None)
        self.assertEqual(header.score(), 3)
        

    def test_with_nothing(self):
        self.assertEqual(content.XFrameHeader.missingScore, runner.config.MISSING_SCORE_XFRAME_HEADER)

if __name__ == '__main__':
    unittest.main()