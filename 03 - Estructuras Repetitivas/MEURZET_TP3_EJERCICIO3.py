
"""
EJERCICIO 3 - AGENDA DE TURNOS CON NOMBRES (SIN LISTAS)
Programa que simula una agenda de turnos para dos días.
"""

# Solicito el nombre del operador
operador = input("\nPor favor, ingrese su nombre: ")

while not operador.isalpha():
    print("\nATENCION! El nombre es obligatorio y solo debe contener letras...\n")
    operador = input("Por favor, ingrese nuevamente su nombre: ")

# Inicializo los turnos de lunes y martes
lunes1 = ""
lunes2 = ""
lunes3 = ""
lunes4 = ""
martes1 = ""
martes2 = ""
martes3 = ""

# Menú principal
salir = False

while not salir:
    print("\n1) Reservar turno  2) Cancelar turno  3) Ver agenda del día  4) Ver resumen general  5) Cerrar sistema")

    # Solicito una opción válida
    opcion = input("Opción: ")

    # Valido que la opción sea un número
    if not opcion.isdigit():
        print("\nATENCION! Debe ingresar un número válido...\n")
        continue
    
    # Convierto la opción a entero para validación de rango
    opcion = int(opcion)

    # Valido que la opción esté en rango
    if opcion < 1 or opcion > 5:
        print("\nATENCION! Opción fuera de rango...\n")
        continue

    # Opción 1: Reservar turno
    if opcion == 1:
        while True:
            print("\n1) Lunes  2) Martes")
            dia = input("Seleccione el día: ")

            if dia not in "12":
                print("\nATENCION! Día inválido...\n")
                continue
            
            # Solicito el nombre del paciente
            nombre_paciente = input("Ingrese nombre del paciente: ")

            if not nombre_paciente.isalpha():
                print("\nATENCION! El nombre solo debe contener letras...\n")
                continue

            # Verifico si el nombre ya está en el día
            repetido = False

            if dia == "1":
                if (nombre_paciente == lunes1 or nombre_paciente == lunes2 or nombre_paciente == lunes3 or nombre_paciente == lunes4):
                    repetido = True
            else:
                if (nombre_paciente == martes1 or nombre_paciente == martes2 or nombre_paciente == martes3):
                    repetido = True

            if repetido:
                print("\nATENCION! El paciente ya tiene turno ese día...\n")
                continue

            # Asigno al primer espacio libre
            asignado = False

            if dia == "1":
                if lunes1 == "":
                    lunes1 = nombre_paciente
                    asignado = True
                elif lunes2 == "":
                    lunes2 = nombre_paciente
                    asignado = True
                elif lunes3 == "":
                    lunes3 = nombre_paciente
                    asignado = True
                elif lunes4 == "":
                    lunes4 = nombre_paciente
                    asignado = True
            else:
                if martes1 == "":
                    martes1 = nombre_paciente
                    asignado = True
                elif martes2 == "":
                    martes2 = nombre_paciente
                    asignado = True
                elif martes3 == "":
                    martes3 = nombre_paciente
                    asignado = True

            if asignado:
                print("\nTurno reservado exitosamente.\n")
                break
            else:
                print("\nATENCION! No hay turnos disponibles para ese día...\n")
                break

    # Opción 2: Cancelar turno
    elif opcion == 2:
        while True:
            print("\n1) Lunes  2) Martes")
            
            # Solicito el día para cancelar el turno
            dia = input("Seleccione el día: ")

            if dia not in "12":
                print("\nATENCION! Día inválido...\n")
                continue
            
            # Solicito el nombre del paciente para cancelar el turno
            nombre_paciente = input("Ingrese nombre del paciente a cancelar: ")

            if not nombre_paciente.isalpha():
                print("\nATENCION! El nombre solo debe contener letras...\n")
                continue
            
            # Busco el nombre en el día correspondiente y lo elimino si lo encuentro
            encontrado = False

            if dia == "1":
                if lunes1 == nombre_paciente:
                    lunes1 = ""
                    encontrado = True
                elif lunes2 == nombre_paciente:
                    lunes2 = ""
                    encontrado = True
                elif lunes3 == nombre_paciente:
                    lunes3 = ""
                    encontrado = True
                elif lunes4 == nombre_paciente:
                    lunes4 = ""
                    encontrado = True
            else:
                if martes1 == nombre_paciente:
                    martes1 = ""
                    encontrado = True
                elif martes2 == nombre_paciente:
                    martes2 = ""
                    encontrado = True
                elif martes3 == nombre_paciente:
                    martes3 = ""
                    encontrado = True

            if encontrado:
                print("\nTurno cancelado exitosamente.\n")
                break
            else:
                print("\nATENCION! El paciente no tiene turno ese día...\n")

    # Opción 3: Ver agenda del día
    elif opcion == 3:
        while True:
            print("\n1) Lunes  2) Martes")

            # Solicito el día para mostrar la agenda
            dia = input("Seleccione el día: ")

            if dia not in "12":
                print("\nATENCION! Día inválido...\n")
                continue

            print("\nAgenda del día:")

            if dia == "1":
                print(f"Lunes 1: {lunes1 if lunes1 else 'Libre'}")
                print(f"Lunes 2: {lunes2 if lunes2 else 'Libre'}")
                print(f"Lunes 3: {lunes3 if lunes3 else 'Libre'}")
                print(f"Lunes 4: {lunes4 if lunes4 else 'Libre'}")
            else:
                print(f"Martes 1: {martes1 if martes1 else 'Libre'}")
                print(f"Martes 2: {martes2 if martes2 else 'Libre'}")
                print(f"Martes 3: {martes3 if martes3 else 'Libre'}")
            break

    # Opción 4: Ver resumen general
    elif opcion == 4:
        print("\nResumen general de turnos:")
        print(f"Lunes 1: {lunes1 if lunes1 else 'Libre'}")
        print(f"Lunes 2: {lunes2 if lunes2 else 'Libre'}")
        print(f"Lunes 3: {lunes3 if lunes3 else 'Libre'}")
        print(f"Lunes 4: {lunes4 if lunes4 else 'Libre'}")
        print(f"Martes 1: {martes1 if martes1 else 'Libre'}")
        print(f"Martes 2: {martes2 if martes2 else 'Libre'}")
        print(f"Martes 3: {martes3 if martes3 else 'Libre'}")

    # Opción 5: Cerrar sistema
    elif opcion == 5:
        salir = True
        print("\nSistema cerrado.\n")
