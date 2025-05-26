'''Ejercicio: Contar vocales en una cadena
Escribe un programa que:

Pida al usuario que ingrese una cadena de texto.
Cuente cuántas vocales (a, e, i, o, u) hay en la cadena (tanto mayúsculas como minúsculas).
Imprima el número total de vocales encontradas.'''

# Solicitar al usuario que ingrese una cadena de texto
texto = input("Ingresa una cadena de texto: ")

# Definir las vocales
vocales = "aáeéiíoóuúAÁEÉIÍOÓUÚ"

# Inicializar un contador para las vocales
contador = 0

# Recorrer cada carácter en la cadena de texto
for c in texto:
    if c in vocales:
        contador += 1

# Imprimir el número total de vocales encontradas
print(f"El texto contiene {contador} vocales.")
