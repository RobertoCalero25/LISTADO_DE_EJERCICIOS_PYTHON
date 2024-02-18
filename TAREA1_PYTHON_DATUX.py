# Programa para ingresar y mostrar datos personales

nombre = input("Ingresa tu nombre: ")
edad = input("Ingresa tu edad: ")
direccion = input("Ingresa tu dirección: ")
telefono = input("Ingresa tu número de teléfono: ")

print("\nDatos personales:")
print("Nombre:", nombre)
print("Edad:", edad)
print("Dirección:", direccion)
print("Teléfono:", telefono)

# Programa para calcular área y perímetro de un polígono
import math
def calcular_area_perimetro(poligono, *dimensiones):
    if poligono == "triangulo":
        base, altura, lado1, lado2 = dimensiones
        area = 0.5 * base * altura
        perimetro = lado1 + lado2 + base
    elif poligono == "cuadrado":
        lado = dimensiones[0]
        area = lado * lado
        perimetro = 4 * lado
    elif poligono == "circulo":
        radio = dimensiones[0]
        area = math.pi * radio**2
        perimetro = 2 * math.pi * radio
    else:
        area = perimetro = 0

    return area, perimetro

poligono_elegido = input("Ingresa el polígono (triangulo, cuadrado, circulo): ").lower()
dimensiones_ingresadas = [float(input(f"Ingrese la {dimension}: ")) for dimension in ["base", "altura", "lado1", "lado2"]]

area_resultado, perimetro_resultado = calcular_area_perimetro(poligono_elegido, *dimensiones_ingresadas)

print(f"\nÁrea del {poligono_elegido}: {area_resultado}")
print(f"Perímetro del {poligono_elegido}: {perimetro_resultado}")

# Programa para calcular gastos y ahorro

ingreso_total = float(input("Ingrese el ingreso total del hogar: "))
gastos = []
total_gastos = 0

while True:
    gasto = input("Ingrese un gasto (o 'fin' para terminar): ")
    if gasto.lower() == 'fin':
        break
    monto = float(input("Ingrese el monto del gasto: "))
    gastos.append((gasto, monto))
    total_gastos += monto

ahorro = ingreso_total - total_gastos

print("\nEgresos:")
for gasto, monto in gastos:
    print(f"{gasto}: ${monto}")

print(f"\nAhorro: ${ahorro}")

# Programa para verificar aptitud para abrir un negocio

edad = input("¿Eres mayor de edad? (si/no): ").lower() == 'si'
tiene_ruc = input("¿Tienes RUC? (si/no): ").lower() == 'si'
nombre_comercial = input("¿Tienes un nombre comercial? (si/no): ").lower() == 'si'

if edad and tiene_ruc and nombre_comercial:
    print("¡Estás apto para abrir un negocio!")
else:
    print("No cumples con las condiciones para abrir un negocio.")
