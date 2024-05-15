import unittest
from leap_year import is_leap_year

class TestLeapYear(unittest.TestCase):

    def test_leap_years(self):
        # Test known leap years
        self.assertTrue(is_leap_year(2000))
        self.assertTrue(is_leap_year(2004))
        self.assertTrue(is_leap_year(2020))

    def test_non_leap_years(self):
        # Test known non-leap years
        self.assertFalse(is_leap_year(1900))
        self.assertFalse(is_leap_year(2100))
        self.assertFalse(is_leap_year(2021))

    def test_invalid_input(self):
        # Test invalid input
        with self.assertRaises(TypeError):
            is_leap_year("invalid")
        with self.assertRaises(TypeError):
            is_leap_year(None)

if __name__ == '__main__':
    unittest.main()
