import unittest
from src.palindrome import is_palindrome

class TestPalindrome(unittest.TestCase):
    def test_simple_palindromes(self):
        self.assertTrue(is_palindrome("madam"))
        self.assertTrue(is_palindrome("racecar"))
        self.assertTrue(is_palindrome("level"))
        self.assertTrue(is_palindrome("reconocer"))
        self.assertTrue(is_palindrome("somos"))
        self.assertTrue(is_palindrome("rayar"))
        self.assertTrue(is_palindrome("oso"))
        self.assertTrue(is_palindrome("salas"))
    
    def test_phrase_palindromes(self):
        self.assertTrue(is_palindrome("A man, a plan, a canal: Panama"))
        self.assertTrue(is_palindrome("Was it a car or a cat I saw?"))
        self.assertTrue(is_palindrome("No lemon, no melon"))
        self.assertTrue(is_palindrome("Anita lava la tina"))
        self.assertTrue(is_palindrome("Dábale arroz a la zorra el abad"))
        self.assertTrue(is_palindrome("La ruta nos aportó otro paso natural"))
        self.assertTrue(is_palindrome("Yo hago yoga hoy"))
        self.assertTrue(is_palindrome("Amo la pacífica paloma"))
    
    def test_frase_vacia(self):
        with self.assertRaises(ValueError):
            is_palindrome("")  
    
    def test_un_solo_caracter(self):
        self.assertTrue(is_palindrome("a"))  
    
    def test_solo_espacios(self):
        with self.assertRaises(ValueError):
            is_palindrome("     ")  
    
    def test_caracteres_especiales(self):
        self.assertTrue(is_palindrome("¿Acaso hubo búhos acá?"))  
    
    def test_mayusculas_acentos_y_puntuacion(self):
        self.assertFalse(is_palindrome("Ánita, la Va LavÁ!"))  

if __name__ == '__main__':
    unittest.main()