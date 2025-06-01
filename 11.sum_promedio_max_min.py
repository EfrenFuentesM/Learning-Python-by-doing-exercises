'''Ejercicio: Escribe un programa que reciba una lista de números enteros del usuario, luego calcule y muestre:

La suma de todos los números en la lista.
El promedio de los números.
El número más grande y el más pequeño.'''

# Pedir al usuario que ingrese una lista de números separados por espacios
entrada = input("Ingresa una lista de números enteros separados por espacios: ")

# Convertir la entrada en una lista de números enteros
numeros = list(map(int, entrada.split()))

# Calcular la suma de los números
suma_total = sum(numeros)

# Calcular el promedio
promedio = suma_total / len(numeros) if numeros else 0  # Evita la división por cero

# Encontrar el número más grande y el más pequeño
maximo = max(numeros)
minimo = min(numeros)

# Mostrar los resultados
print(f"Suma total: {suma_total}")
print(f"Promedio: {promedio:.2f}")
print(f"Número más grande: {maximo}")
print(f"Número más pequeño: {minimo}")
