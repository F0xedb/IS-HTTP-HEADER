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