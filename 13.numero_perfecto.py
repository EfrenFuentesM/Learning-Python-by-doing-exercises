'''Escribe un programa en Python que determine si un número ingresado por el usuario es perfecto.
Un número perfecto es aquel que es igual a la suma de sus divisores propios positivos (excluyendo el mismo número).'''

# Pedir al usuario un número entero
num = int(input("Ingresa un número para verificar si es perfecto: "))

# Calcular la suma de sus divisores propios
suma_divisores = sum(i for i in range(1, num) if num % i == 0)

# Verificar si es un número perfecto
if suma_divisores == num:
    print(f"El número {num} es un número perfecto.")
else:
    print(f"El número {num} no es un número perfecto.")
