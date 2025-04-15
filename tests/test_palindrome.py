import unittest
from src.palindrome import is_palindrome

class TestPalindrome(unittest.TestCase):
    def test_simple_palindromes(self):
        # Ejemplos en inglés
        self.assertTrue(is_palindrome("madam"))
        self.assertTrue(is_palindrome("racecar"))
        self.assertTrue(is_palindrome("level"))
        
        # Ejemplos en español
        self.assertTrue(is_palindrome("reconocer"))
        self.assertTrue(is_palindrome("somos"))
        self.assertTrue(is_palindrome("rayar"))
        self.assertTrue(is_palindrome("oso"))
        self.assertTrue(is_palindrome("salas"))

if __name__ == '__main__':
    unittest.main()