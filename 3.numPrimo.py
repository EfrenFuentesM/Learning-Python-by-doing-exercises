'''Ejercicio: Determinar si un número es primo
Crea un programa que haga lo siguiente:

Solicite al usuario un número entero positivo.
Determine si el número es primo o no.
Imprima un mensaje indicando el resultado.'''

# Solicitar un número al usuario
n = int(input('Ingresa un número entero positivo: '))

# Comprobar si el número es menor que 2 (no es primo)
if n < 2:
    print(f'{n} no es un número primo.')
else:
    # Asumimos que el número es primo
    es_primo = True

    # Verificar divisores desde 2 hasta la raíz cuadrada de n
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:  # Si es divisible por i, no es primo
            es_primo = False
            break

    # Imprimir el resultado
    if es_primo:
        print(f'{n} es un número primo :)')
    else:
        print(f'{n} no es un número primo.')
