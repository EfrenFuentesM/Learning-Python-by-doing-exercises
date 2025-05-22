'''Crea un programa que sume dos números dados por el usuario, mostrando el resultado en decimal y 
luego en octal'''

# Solicitar dos números al usuario
num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))

# Calcular la suma
suma = num1 + num2

# Mostrar el resultado en decimal y octal
print(f"Resultado en decimal: {suma}")
print(f"Resultado en octal: {oct(suma)}")
