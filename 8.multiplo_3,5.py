'''Ejercicio: Comprobar si un número es un múltiplo de 3 o 5
Escribe un programa que:

Solicite al usuario que ingrese un número entero positivo.
Verifique si el número es múltiplo de 3, de 5 o de ambos.
Imprima un mensaje indicando el resultado:
Si el número es múltiplo de 3: "El número es múltiplo de 3."
Si es múltiplo de 5: "El número es múltiplo de 5."
Si es múltiplo de ambos: "El número es múltiplo de 3 y 5."
Si no es múltiplo de ninguno: "El número no es múltiplo de 3 ni de 5."'''


# Solicitar al usuario un número entero positivo
num = int(input('Ingresa un número entero positivo: '))

# Verificar las condiciones en orden
if num % 3 == 0 and num % 5 == 0:
    resultado = f'{num} es múltiplo de 3 y 5'
elif num % 3 == 0:
    resultado = f'{num} es múltiplo de 3'
elif num % 5 == 0:
    resultado = f'{num} es múltiplo de 5'
else:
    resultado = f'{num} no es múltiplo de 3 ni de 5'

# Imprimir el resultado final
print(resultado)
