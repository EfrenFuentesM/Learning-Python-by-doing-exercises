'''Ejercicio
Escribe un programa en Python que genere la tabla de multiplicar de un número ingresado por el usuario.'''


# Pedir al usuario un número
num = int(input("Ingresa un número para ver su tabla de multiplicar: "))

# Generar la tabla de multiplicar del 1 al 10
print(f"Tabla de multiplicar del {num}:")
for i in range(1, 10):
    print(f"{num} x {i} = {num * i}")