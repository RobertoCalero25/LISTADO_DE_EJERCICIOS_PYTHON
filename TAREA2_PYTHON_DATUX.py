# Declaración de variables globales
alumnos = []

# Función para calcular el promedio de las notas
def calcular_promedio(notas):
    return sum(notas) / len(notas) if len(notas) > 0 else 0

# Menú iterativo
while True:
    print("\nMenu:")
    print("1. Saludar y pedir datos personales")
    print("2. Realizar operación matemática y pedir 2 números")
    print("3. Agregar a lista un diccionario con datos de alumnos")
    print("4. Calcular promedio de notas y agregar a lista de notas finales")
    print("5. Mostrar listado de alumnos aprobados")
    print("6. Mostrar listado de alumnos desaprobados")
    print("7. Generar lista de números múltiplos de 2, 5 y 7 hasta 10^10")
    print("8. Llamar a función para obtener el mayor de 2 números")
    print("9. Salir")

    opcion = input("\nIngrese el número de la opción deseada: ")

    if opcion == "1":
        # Opción 1: Saludar y pedir datos personales
        nombre = input("Ingrese su nombre: ")
        edad = input("Ingrese su edad: ")
        correo = input("Ingrese su correo: ")
        print(f"\n¡Hola, {nombre}! Gracias por proporcionar tus datos.\n")

    elif opcion == "2":
        # Opción 2: Realizar operación matemática y pedir 2 números
        num1 = float(input("Ingrese el primer número: "))
        num2 = float(input("Ingrese el segundo número: "))
        resultado = num1 + num2
        print(f"\nEl resultado de la operación es: {resultado}\n")

    elif opcion == "3":
        # Opción 3: Agregar a lista un diccionario con datos de alumnos
        nombre = input("Ingrese nombre del alumno: ")
        edad = input("Ingrese edad del alumno: ")
        correo = input("Ingrese correo del alumno: ")
        cursos = []
        num_cursos = int(input("Ingrese la cantidad de cursos: "))
        for _ in range(num_cursos):
            curso_nombre = input("Ingrese nombre del curso: ")
            notas = [float(nota) for nota in input("Ingrese las notas separadas por espacio: ").split()]
            cursos.append({"nombre_curso": curso_nombre, "notas": notas})
        alumnos.append({"nombre": nombre, "edad": edad, "correo": correo, "cursos": cursos})
        print("\nDatos del alumno agregados a la lista.\n")

    elif opcion == "4":
        # Opción 4: Calcular promedio de notas y agregar a lista de notas finales
        for alumno in alumnos:
            for curso in alumno["cursos"]:
                notas_finales = calcular_promedio(curso["notas"])
                curso["notas_finales"] = notas_finales
        print("\nPromedio de notas calculado y agregado a la lista.\n")

    elif opcion == "5":
        # Opción 5: Mostrar listado de alumnos aprobados
        for alumno in alumnos:
            for curso in alumno["cursos"]:
                if calcular_promedio(curso["notas"]) >= 6.0:
                    print(f"{alumno['nombre']} - Aprobado en {curso['nombre_curso']}")
        print()

    elif opcion == "6":
        # Opción 6: Mostrar listado de alumnos desaprobados
        for alumno in alumnos:
            for curso in alumno["cursos"]:
                if calcular_promedio(curso["notas"]) < 6.0:
                    print(f"{alumno['nombre']} - Desaprobado en {curso['nombre_curso']}")
        print()

    elif opcion == "7":
        # Opción 7: Generar lista de números múltiplos de 2, 5 y 7 hasta 10^10
        rango_maximo = int(1e10)
        step = int(input("Ingrese el valor del step para el rango: "))
        lista_multiplos = [num for num in range(1, rango_maximo + 1, step) if num % 2 == 0 and num % 5 == 0 and num % 7 == 0]
        print(f"\nTamaño de la lista de múltiplos: {len(lista_multiplos)}\n")

    elif opcion == "8":
        # Opción 8: Llamar a función para obtener el mayor de 2 números
        num1 = float(input("Ingrese el primer número: "))
        num2 = float(input("Ingrese el segundo número: "))
        mayor = max(num1, num2)
        print(f"\nEl número mayor es: {mayor}\n")

    elif opcion == "9":
        # Opción 9: Salir
        print("Saliendo del programa.")
        break

    else:
        print("Opción no válida. Por favor, ingrese un número del 1 al 9.")
