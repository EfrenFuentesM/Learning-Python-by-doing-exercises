'''Ejercicio: Verificar si un número es un palíndromo
Un número es un palíndromo si se lee igual de izquierda a derecha que de derecha a izquierda. 
Por ejemplo, 121, 12321 y 45654 son números palíndromos.

Tu tarea:
Pide al usuario que ingrese un número entero positivo.
Verifica si el número es un palíndromo.
Muestra un mensaje indicando si es o no un palíndromo.'''


# Solicitar al usuario un número entero positivo
numero = input("Ingresa un número entero positivo: ")

# Verificar si el número es un palíndromo
if numero == numero[::-1]:
    print(f"{numero} es un número palíndromo.")
else:
    print(f"{numero} no es un número palíndromo.")
