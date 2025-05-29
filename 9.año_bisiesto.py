'''Ejercicio: Determinar si un año es bisiesto
Escribe un programa que:

Solicite al usuario ingresar un año (un número entero positivo).
Determine si el año es bisiesto o no.
Imprima uno de los siguientes mensajes:
"El año es bisiesto."
"El año no es bisiesto."
Un año es bisiesto si cumple estas reglas:

Es divisible entre 4.
Pero no es divisible entre 100, a menos que también sea divisible entre 400.'''

# Solicitar al usuario que ingrese un año
year = int(input("Ingresa un año: "))

# Verificar si el año es bisiesto
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"El año {year} es bisiesto.")
else:
    print(f"El año {year} no es bisiesto.")
