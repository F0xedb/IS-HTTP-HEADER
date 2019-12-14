import unittest
import runner.headers.CORSHeader as content
import runner.config

class TestCorsMethods(unittest.TestCase):

    def test_with_glob(self):
        header = content.CORSHeader("*", None)
        self.assertEqual(header.score(), 0)

    def test_without_glob(self):
        header = content.CORSHeader("", None)
        self.assertEqual(header.score(), 5)
    
    def test_with_domain(self):
        header = content.CORSHeader("www.google.com", None)
        self.assertEqual(header.score(), 5)

    def test_with_nothing(self):
        self.assertEqual(content.CORSHeader.missingScore, runner.config.MISSING_SCORE_CORS)

if __name__ == '__main__':
    unittest.main()