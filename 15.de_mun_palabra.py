'''Ejercicio: Convertir números a palabras
Instrucciones:
Escribe un programa en Python que convierta un número del 0 al 9 en su equivalente en palabras.'''


# Diccionario con la conversión de números a palabras
numeros_a_palabras = {
    0: "cero",
    1: "uno",
    2: "dos",
    3: "tres",
    4: "cuatro",
    5: "cinco",
    6: "seis",
    7: "siete",
    8: "ocho",
    9: "nueve"
}

# Solicitar al usuario un número del 0 al 9
try:
    num = int(input("Ingresa un número (0-9): "))
    
    # Verificar si el número está en el rango permitido
    if 0 <= num <= 9:
        print(f"El número {num} se escribe como '{numeros_a_palabras[num]}'.")
    else:
        print("Error: Debes ingresar un número entre 0 y 9.")
        
except ValueError:
    print("Error: Ingresa solo números enteros.")
