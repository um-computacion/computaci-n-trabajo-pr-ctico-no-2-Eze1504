# src/palindrome.py

def es_palindromo(palabra):
    # Convertir la palabra a minúsculas y eliminar espacios
    palabra = palabra.lower().replace(" ", "")
    # Comprobar si la palabra es igual a su reverso
    return palabra == palabra[::-1]
