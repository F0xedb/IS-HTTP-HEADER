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