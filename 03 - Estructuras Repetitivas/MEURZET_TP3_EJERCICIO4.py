"""
EJERCICIO 4 - ESCAPE ROOM: LA BÓVEDA
Programa que simula un escape room con validaciones, menús y condiciones de victoria/derrota.
"""

# Solicito el nombre del agente
nombre_agente = input("Ingrese el nombre del agente: ")

while not nombre_agente.isalpha():
    print("\nNombre inválido. Solo letras, sin espacios ni números.")
    
    nombre_agente = input("\nIngrese nuevamente el nombre del agente: ")

print(f"\n¡Bienvenido, {nombre_agente}! Comienza el escape room.")

# Variables iniciales
energia = 100
tiempo = 12
cerraduras_abiertas = 0
alarma = False
codigo_parcial = ""
forzar_seguidas = 0  # Contador para regla anti-spam

# Bucle principal del juego
while energia > 0 and tiempo > 0 and cerraduras_abiertas < 3 and not (alarma and tiempo <= 3):
    # Mostrar estado actual
    print("\n--- Estado Actual ---")
    print(f"Energía: {energia}")
    print(f"Tiempo: {tiempo}")
    print(f"Cerraduras abiertas: {cerraduras_abiertas}/3")
    print(f"Código parcial: \"{codigo_parcial}\"")
    print(f"Alarma: {'Activada' if alarma else 'Desactivada'}")

    # Mostrar menú
    print("\n--- Menú de Acciones ---")
    print("1. Forzar cerradura (costo: -20 energía, -2 tiempo)")
    print("2. Hackear panel (costo: -10 energía, -3 tiempo)")
    print("3. Descansar (costo: +15 energía, -1 tiempo)")

    # Pedir opción con validación
    opcion = input("Elija una opción (1-3): ")

    while not (opcion.isdigit() and opcion in "123"):
        print("\nOpción inválida. Ingrese 1, 2 o 3.")
        opcion = input("\nElija nuevamente una opción (1-3): ")

    # Convierto la opción a entero para el menú
    opcion = int(opcion)

    # Opcion 1: Forzar cerradura
    if opcion == 1:
        energia -= 20
        tiempo -= 2

        if energia < 40:
            print("\n¡Riesgo de alarma! Elige un número del 1 al 3:")
            
            numero_riesgo = input("Número (1-3): ")
            
            while not (numero_riesgo.isdigit() and 1 <= int(numero_riesgo) <= 3):
                print("\nNúmero inválido. Ingrese 1, 2 o 3.")
                numero_riesgo = input("\nNúmero (1-3): ")
                
            if int(numero_riesgo) == 3:
                alarma = True
                print("\n¡Alarma activada por riesgo!")
        
        if not alarma:
            if forzar_seguidas == 2:
                alarma = True
                print("\nLa cerradura se trabó por abuso. Alarma activada.")
            else:
                cerraduras_abiertas += 1
                print("\n¡Cerradura forzada exitosamente!")

        # Incremento el contador de forzar cerradura
        forzar_seguidas += 1

    # Opción 2: Hackear panel
    elif opcion == 2:  
        energia -= 10
        tiempo -= 3
        
        print()

        for i in range(4):
            print(f"Paso {i+1}/4: Hackeando...")
            codigo_parcial += "A"
        
        if len(codigo_parcial) >= 8 and cerraduras_abiertas < 3:
            cerraduras_abiertas += 1
            print("\n¡Código completado! Cerradura hackeada.")
        
        # Reiniciar contador de forzar cerradura al hackear exitosamente
        forzar_seguidas = 0

    # Opción 3: Descansar
    elif opcion == 3: 
        energia = min(100, energia + 15)
        tiempo -= 1
        
        if alarma:
            energia -= 10
            print("\nDescanso completado, pero alarma consumió energía extra.")
        else:
            print("\nDescanso completado. Energía recuperada.")
        
        # Reiniciar contador de forzar cerradura al descansar
        forzar_seguidas = 0

# Condiciones de fin
print("\n--- Fin del Juego ---")

if cerraduras_abiertas == 3:
    print("\n¡VICTORIA! Has abierto la bóveda.")
elif energia <= 0 or tiempo <= 0:
    print("\nDERROTA. Te quedaste sin energía o tiempo.")
elif alarma and tiempo <= 3:
    print("\nDERROTA. Sistema bloqueado por alarma.")

print(f"\nEstadísticas finales: Energía {energia}, Tiempo {tiempo}, Cerraduras {cerraduras_abiertas}/3.")