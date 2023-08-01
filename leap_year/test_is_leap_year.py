import unittest
import is_leap_year

class MyTestCase(unittest.TestCase):
    def test_is_leap(self):
        year = '1990'
        output = False
        self.assertEqual(output, is_leap_year(year))