'''Escribe un programa en Python que haga lo siguiente:

Solicite al usuario un número entero positivo n.
Solicite al usuario un número entero positivo m.
Muestre todos los múltiplos de m que sean menores o iguales a n.
Si no hay múltiplos, muestra un mensaje indicando que no se encontraron múltiplos de m menores o iguales a n.'''

# Solicitar los números n y m al usuario
n = int(input("Ingresa un número n: "))
m = int(input("Ingresa un número m: "))

# Obtener los múltiplos de m menores o iguales a n
múltiplos = [i for i in range(m, n + 1, m)]

# Verificar si se encontraron múltiplos
if múltiplos:
    print(f"Los múltiplos de {m} menores o iguales a {n} son: {', '.join(map(str, múltiplos))}.")
else:
    print(f"No se encontraron múltiplos de {m} menores o iguales a {n}.")
