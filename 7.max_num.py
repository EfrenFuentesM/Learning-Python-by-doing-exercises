'''Ejercicio: Encontrar el número más grande en una lista
Escribe un programa que:

Solicite al usuario una lista de números enteros separados por comas (por ejemplo: 1, 45, 23, 89, 2).
Encuentre el número más grande en esa lista.
Imprima el número más grande.'''

# Solicitar al usuario una lista de números separados por comas
entrada = input("Ingresa una lista de números enteros separados por comas: ")

# Convertir la entrada en una lista de enteros
numeros = list(map(int, entrada.split(',')))

# Encontrar el número más grande usando max()
maximo = max(numeros)

# Imprimir el resultado
print(f"El número más grande en la lista es: {maximo}")
