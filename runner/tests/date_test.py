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