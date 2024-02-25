#lineas de codigo de la función
def dividir(a, b):
    if b == 0:
        raise ValueError("No se puede dividir por cero.")
    return a / b

from calculadora import dividir

#codigo principal
while True:
    try:
        num1 = float(input("Ingrese el primer número: "))
        num2 = float(input("Ingrese el segundo número: "))
        resultado = dividir(num1, num2)
        print(f"Resultado de la división: {resultado}")
        break  # Romper el bucle si la división se realiza correctamente
    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"Error inesperado: {e}")