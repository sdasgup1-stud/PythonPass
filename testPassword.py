#https://codereview.stackexchange.com/questions/208567/strong-password-detection
#UnitTest
import re
import unittest
import Password

PASSWORD_CHECKS = [
    re.compile(r'[A-Z]'),
    re.compile(r'.{8,}'),
    re.compile(r'[a-z]'),
    re.compile(r'[0-9]'),
]

def strong_password(password):
    """
    Validate if passed password is considered "strong",
    Password is considered strong if:
      - is eight characters or longer
      - contains uppercase and lowercase characters
      - has one digit or more
    """
    return all(check.search(password) for check in PASSWORD_CHECKS)

class TestIsStrongPassword(unittest.TestCase):
    """Test of strong password detection function."""
    def test_strong_password(self):
        """
        Test strong password function. Passed strings have to pass 
        all tests in valid_length, uppper, lower and digit functions.
        """

        # Test from single functions should all fail 
        # (not met all criteria)
        self.assertFalse(strong_password('abcd'))
        self.assertFalse(strong_password('abcdefg'))
        self.assertFalse(strong_password('abcdefgh'))
        self.assertFalse(strong_password('abcdefghi'))

        self.assertFalse(strong_password('abcd'))
        self.assertFalse(strong_password('aBcd'))
        self.assertFalse(strong_password('aBCd'))
        self.assertFalse(strong_password('Abcd'))
        self.assertFalse(strong_password('abcD'))
        self.assertFalse(strong_password('ABCD'))

        self.assertFalse(strong_password('abcd'))
        self.assertFalse(strong_password('a1cd'))
        self.assertFalse(strong_password('a12d'))
        self.assertFalse(strong_password('1bcd'))
        self.assertFalse(strong_password('abc1'))
        self.assertFalse(strong_password('1234'))

        # Combinations which met more than one cirteria
        self.assertFalse(strong_password('12345678'))
        self.assertFalse(strong_password('Abcdefgh'))
        self.assertFalse(strong_password('A12345678'))
        self.assertFalse(strong_password('Abcdfg1'))
        self.assertTrue(strong_password('A12345678b'))
        self.assertTrue(strong_password('Abcdefg1'))
        self.assertTrue(strong_password('123456aB'))
        self.assertTrue(strong_password('aB345678'))

if __name__ == '__main__':
    unittest.main()
