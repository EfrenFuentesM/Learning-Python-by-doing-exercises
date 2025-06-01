'''Ejercicio: Números de la serie de Fibonacci
Escribe un programa que:

Solicite al usuario ingresar un número entero positivo, 
𝑛
n.
Calcule y muestre los primeros 
𝑛
n números de la serie de Fibonacci.
La serie de Fibonacci comienza con 0 y 1, y cada número siguiente es la suma de los dos anteriores. Es decir:
0, 1, 1, 2, 3, 5, 8, 13, 21, ...'''


# Solicitar al usuario la cantidad de términos
n = int(input("Ingresa la cantidad de términos de Fibonacci que deseas: "))

# Verificar que el usuario ingrese un número válido
if n <= 0:
    print("Por favor, ingresa un número entero positivo.")
else:
    # Inicializar la serie de Fibonacci
    fibonacci = [0, 1]  # Los dos primeros términos
    
    # Generar los términos restantes si n > 2
    for i in range(2, n):  # Comenzamos desde el tercer término
        siguiente = fibonacci[i - 1] + fibonacci[i - 2]  # Sumar los dos anteriores
        fibonacci.append(siguiente)
    
    # Mostrar la serie hasta el término n
    print(f"Los primeros {n} términos de Fibonacci son: {', '.join(map(str, fibonacci[:n]))}") # el slicing [:n] en este caso es opcional
