
'''Ejercicio: Calculadora de números pares
Escribe un programa que haga lo siguiente:

Solicite al usuario un número entero positivo.
Determine si el número ingresado es par o impar.
Si el número es par, suma todos los números pares desde 0 hasta ese número (incluyéndolo).
Si el número es impar, muestra un mensaje indicando que no se pueden sumar los números impares.
Ejemplo de entrada y salida:

Entrada: 6
Salida: La suma de los números pares hasta 6 es 12.
Entrada: 7
Salida: El número ingresado es impar, no se pueden sumar los números impares.'''

num = int(input('Ingresa un número par positivo '))

if num % 2 == 0:
    result = 0
    for i in range(0, num + 1, 2):
        result += i
    print(f'La suma de los números pares hasta {num} es {result}')

else:
    print('El número no es par, no se pueden sumar impares')