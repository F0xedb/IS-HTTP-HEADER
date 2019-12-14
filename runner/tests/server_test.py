import unittest
import runner.headers.ServerHeader as content
import runner.config

class TestServerMethods(unittest.TestCase):

    def test_with_apache(self):
        header = content.ServerHeader("Apache", None)
        self.assertEqual(header.score(), 10)

    def test_with_nginx(self):
        header = content.ServerHeader("nginx", None)
        self.assertEqual(header.score(), 10)

    def test_with_google(self):
        header = content.ServerHeader("gws", None)
        self.assertEqual(header.score(), 10)

    def test_with_unknown(self):
        header = content.ServerHeader("abcdefijand", None)
        self.assertEqual(header.score(), 7)

    def test_with_nothing(self):
        self.assertEqual(content.ServerHeader.missingScore, runner.config.MISSING_SCORE_SERVER_HEADER)

if __name__ == '__main__':
    unittest.main()