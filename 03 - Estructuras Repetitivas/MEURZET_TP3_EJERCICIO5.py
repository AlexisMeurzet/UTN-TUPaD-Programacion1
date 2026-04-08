"""
EJERCICIO 5 - ESCAPE ROOM: LA ARENA DEL GLADIADOR
Programa que simula una batalla por turnos.
"""

print("\n--- BIENVENIDO A LA ARENA ---\n")

# Solicito nombre del Gladiador
nombre_gladiador = input("Nombre del Gladiador: ")

# Mientras el nombre este compuesto solo por letras, vuelvo a solicitarlo
while not nombre_gladiador.isalpha():
    print("\nError: Solo se permiten letras.")
    nombre_gladiador = input("\nIngrese nuevamente el nombre del Gladiador: ")

# Variables iniciales
vida_gladiador = 100
vida_enemigo = 100
pociones = 3
ataque_pesado = 15
ataque_enemigo = 12
turno_gladiador = True

print("\n=== INICIO DEL COMBATE ===")

# Ciclo de combate
while vida_gladiador > 0 and vida_enemigo > 0:
    if turno_gladiador:
        print(f"\n{nombre_gladiador} (HP: {vida_gladiador}) vs Enemigo (HP: {vida_enemigo}) | Pociones: {pociones}")
        print("\nElige acción:")
        print("1. Ataque Pesado")
        print("2. Ráfaga Veloz")
        print("3. Curar")

        # Solicito una opción válida
        opcion = input("\nOpción: ")

        # Mientras la opción no sea válida, vuelvo a solicitarla
        while not (opcion.isdigit() and opcion in "123"):
            print("\nError: Ingrese un número válido.")
            opcion = input("\nOpción: ")

        # Convierto la opción a entero para el menú
        opcion = int(opcion)

        # Ejecuto la acción elegida
        if opcion == 1:
            daño_final = ataque_pesado

            if vida_enemigo < 20:
                daño_final = ataque_pesado * 1.5

            vida_enemigo -= daño_final

            print(f"\n¡Atacaste al enemigo por {daño_final} puntos de daño!")

        elif opcion == 2:
            print("\n>> ¡Inicias una ráfaga de golpes!")

            for i in range(3):
                vida_enemigo -= 5
                print("> Golpe conectado por 5 de daño")

        elif opcion == 3:
            if pociones > 0:
                vida_gladiador += 30
                pociones -= 1

                print("\n>> ¡Usaste una poción y recuperaste 30 puntos de vida!")
            else:
                print("\n>> ¡No quedan pociones!")

        turno_gladiador = False
    else:
        vida_gladiador -= ataque_enemigo
        print(f"\n>> ¡El enemigo contraataca por {ataque_enemigo} puntos!")
        turno_gladiador = True

    if vida_enemigo <= 0 or vida_gladiador <= 0:
        break

    if turno_gladiador:
        print("\n=== NUEVO TURNO ===")

print("\n=== FIN DEL COMBATE ===")

# Verifico resultado final
if vida_gladiador > 0:
    print(f"\n¡VICTORIA! {nombre_gladiador} ha ganado la batalla.")
else:
    print("\nDERROTA. Has caído en combate.")
