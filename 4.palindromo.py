
'''Ejercicio: Verificar si una palabra es un palíndromo
Problema:
Crea un programa que pida al usuario ingresar una palabra o frase, y determine si es un palíndromo. 
Un palíndromo es una palabra o frase que se lee igual al derecho y al revés (ignorando espacios, mayúsculas y acentos).

Ejemplo 1:

Entrada: anita lava la tina
Salida: ¡Es un palíndromo!
Ejemplo 2:

Entrada: Hola mundo
Salida: No es un palíndromo.'''

import unicodedata

def es_palindromo(texto):
    # 1. Preprocesar el texto
    # Eliminar espacios y convertir a minúsculas
    texto = texto.replace(" ", "").lower()
    
    # Quitar acentos y caracteres especiales
    texto = ''.join(
        c for c in unicodedata.normalize('NFD', texto)
        if unicodedata.category(c) != 'Mn'
    )
    
    # 2. Invertir el texto
    texto_invertido = texto[::-1]
    
    # 3. Comparar el texto original con el invertido
    if texto == texto_invertido:
        return "¡Es un palíndromo!"
    else:
        return "No es un palíndromo."

# Entrada del usuario
frase = input("Ingresa una palabra o frase: ")

# Llamada a la función y salida
resultado = es_palindromo(frase)
print(resultado)
