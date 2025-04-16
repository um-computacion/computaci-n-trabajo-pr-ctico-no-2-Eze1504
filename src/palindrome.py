import re
import unicodedata

def is_palindrome(texto: str) -> bool:
    if not isinstance(texto, str):
        raise TypeError("El argumento debe ser una cadena de texto.")

    texto_normalizado = unicodedata.normalize('NFD', texto)
    texto_sin_tildes = ''.join(
        c for c in texto_normalizado if unicodedata.category(c) != 'Mn'
    )

    texto_minusculas = texto_sin_tildes.lower()

    texto_limpio = re.sub(r'[^a-z]', '', texto_minusculas)

    return texto_limpio == texto_limpio[::-1]
