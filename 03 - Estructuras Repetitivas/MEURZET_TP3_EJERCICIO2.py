"""
EJERCICIO 2 - ACCESO AL CAMPUS Y MENÚ SEGURO
Programa que simula login con intentos y menú seguro.
"""

# Defino credenciales fijas
USUARIO_CORRECTO = "alumno"
CLAVE_CORRECTA = "python123"

# Inicializo variables para intentos y clave actual
intentos = 0
max_intentos = 3
clave_actual = CLAVE_CORRECTA

# Proceso de login con máximo 3 intentos
while intentos < max_intentos:
    print(f"Intento {intentos + 1}/3 - Usuario:", end=" ")

    usuario = input()
    clave = input("Clave: ")

    # Verifico credenciales
    if usuario == USUARIO_CORRECTO and clave == clave_actual:
        print("Acceso concedido.")
        break
    else:
        print("Error: credenciales inválidas.")
        intentos += 1

# Si se superan los intentos, bloqueo la cuenta
if intentos == max_intentos:
    print("Cuenta bloqueada.")
else:
    salir = False

    # Menú principal repetitivo hasta elegir salir
    while not salir:
        print("\n1) Estado  2) Cambiar clave  3) Mensaje  4) Salir")
        opcion = input("Opción: ")

        # Valido que la opción sea un número
        if not opcion.isdigit():
            print("Error: ingrese un número válido.")
            continue
        
        # Convierto la opción a entero para validación de rango
        opcion = int(opcion)

        # Valido que la opción esté en rango
        if opcion < 1 or opcion > 4:
            print("Error: opción fuera de rango.")
            continue

        # Opción 1: Ver estado de inscripción
        if opcion == 1:
            print("Inscripto")

        # Opción 2: Cambiar clave
        elif opcion == 2:
            nueva_clave = input("Nueva clave: ")

            # Valido longitud mínima de la nueva clave
            if len(nueva_clave) < 6:
                print("Error: mínimo 6 caracteres.")
                continue

            confirmacion = input("Confirme nueva clave: ")

            # Valido coincidencia de claves
            if nueva_clave != confirmacion:
                print("Error: las claves no coinciden.")
                continue

            clave_actual = nueva_clave

            print("Clave cambiada exitosamente.")

        # Opción 3: Mensaje motivacional
        elif opcion == 3:
            print("¡Sigue adelante, puedes lograrlo!")

        # Opción 4: Salir
        elif opcion == 4:
            salir = True
            print("Sesión finalizada.")
