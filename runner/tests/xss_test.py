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