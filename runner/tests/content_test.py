import unittest
import runner.headers.contentEncodingHeader as content
import runner.config

class TestContentEncodingMethods(unittest.TestCase):

    def test_with_gzip(self):
        header = content.ContentEncodingHeader("gzip", None)
        self.assertEqual(header.score(), 10)

    def test_without_encoding(self):
        header = content.ContentEncodingHeader("gzup", None)
        self.assertEqual(header.score(), 8)

    def test_with_nothing(self):
        header = content.ContentEncodingHeader("", None)
        self.assertEqual(content.ContentEncodingHeader.missingScore, runner.config.MISSING_SCORE_CONTENT_ENCODING)

if __name__ == '__main__':
    unittest.main()