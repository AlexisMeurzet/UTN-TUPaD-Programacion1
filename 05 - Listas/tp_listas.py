import random

'''
Actividad 1 - Crear una lista con las notas de 10 estudiantes.
 * Mostrar la lista completa.
 * Calcular y mostrar el promedio.
 * Indicar la nota mas alta y la mas baja.
'''

print("\n--- Actividad 1 ---\n")

# Inicializo lista de notas
notas = []

# Inicializo variable para acumular la suma de las notas
suma_notas = 0

# Inicializo variables para almacenar la nota más alta y la más baja
nota_maxima = 0
nota_minima = 10

for i in range(1, 11):
    # Agrego una nota aleatoria entre 1 y 10 a la lista de notas
    notas.append(round(random.uniform(1, 10), 2))


print("Alumno\t\tNota",)
print("-" * 20,)

for i in range(len(notas)):
    # Variable para facilitar lectura, calculos y validaciones
    nota = notas[i]
    
    # Acumulo la suma de las notas
    suma_notas += nota

    # Actualizo la nota máxima y mínima
    if nota > nota_maxima:
        nota_maxima = nota

    if nota < nota_minima:
        nota_minima = nota

    # Muestro la nota de cada estudiante
    print(f"{i + 1}\t\t{nota}")

# Muestro el promedio
print(f"\nPromedio de notas: {suma_notas / len(notas):.2f}")

# Muestro la nota más alta y la más baja
print(f"\nNota más alta: {nota_maxima}")
print(f"Nota más baja: {nota_minima}\n")

'''
Actividad 2 - Pedir al usuario que cargue 5 productos en una lista.
 * Mostrar la lista ordenada alfabéticamente.
 * Preguntar al usuario que producto desea eliminar y actualizar la lista.


print("\n--- Actividad 2 ---\n")

# Inicializo lista de productos
productos = [] 

# Solicito al usuario que ingrese 5 productos
for i in range(5):
    # Solicito el producto al usuario
    producto = input(f"Ingrese el producto {i + 1}: ")

    # Si el producto no contiene solo letras, muestro un mensaje de alerta y solicito nuevamente el producto
    while not producto.isalpha():
        print("\nATENCION... El producto debe contener solo letras.\n")
        
        producto = input(f"Ingrese nuevamente el producto {i + 1}: ")

    # Agrego el producto a la lista de productos
    productos.append(producto)

# Ordeno la lista de productos alfabéticamente
productos = sorted(productos)

# Muestro la lista de productos
print(f"\nProductos ingresados: {", ".join(productos)}")

# Solicito al usuario que ingrese el producto que desea eliminar
producto_por_eliminar = input("\nIngrese el producto que desea eliminar: ")

# Mientras el producto no contiene solo letras, muestro un mensaje de alerta y solicito nuevamente el producto
while not producto_por_eliminar.isalpha():
    print("\nATENCION... El producto debe contener solo letras.\n")
    
    producto_por_eliminar = input(f"Ingrese nuevamente el producto a eliminar: ")

# Mientras el producto no se encuentra en la lista, muestro un mensaje de alerta y solicito nuevamente el producto
while producto_por_eliminar not in productos:
    print("\nATENCION... El producto no se encuentra en la lista.\n")
    
    producto_por_eliminar = input(f"Ingrese nuevamente el producto a eliminar: ")

# Elimino el producto de la lista
productos.remove(producto_por_eliminar)

# Muestro la lista actualizada
print(f"\nProductos finales: {", ".join(productos)}\n")
'''

'''
Actividad 3 - Generar una lista con 15 numeros enteros al azar entre 1 y 100.
 * Crear una lista con los pares y otra con los impares.
 * Mostrar cuantos numeros tiene cada lista
'''

print("\n--- Actividad 3 ---\n")\

# Inicializo lista de numeros
numeros = []

# Inicializo listas para pares e impares
pares = []
impares = []

for i in range(15):
    # Genero un numero entero aleatorio entre 1 y 100
    numero = random.randint(1, 100)

    # Mientras el numero se encuentre en la lista de numeros, genero un nuevo numero
    while numero in numeros:
        numero = random.randint(1, 100)

    # Agrego el numero a la lista de numeros
    numeros.append(numero)

# Muestro la lista de numeros generados
print(f"Numeros generados: {numeros}\n")

# Itero sobre la lista de numeros y separo los pares de los impares
for numero in numeros:
    if numero % 2 == 0:
        pares.append(numero)
    else:
        impares.append(numero)

print(f"Numeros pares: {pares}")
print(f"Cantidad de numeros pares: {len(pares)}\n")

print(f"Numeros impares: {impares}")
print(f"Cantidad de numeros impares: {len(impares)}\n")


'''
Actividad 4 - Dada una lista con valores repetidos;

    datos = [1, 3, 5, 3, 7, 1 , 9, 5, 3]

 * Crear una nueva lista sin elementos repetidos.
 * Mostrar el resultado.
'''

print("\n--- Actividad 4 ---\n")

# Declaro la lista con valores repetidos
datos = [1, 3, 5, 3, 7, 1 , 9, 5, 3]

# Inicializo lista final sin elementos repetidos
lista_final = []

# Itero sobre la lista de datos y agrego a la lista final solo los elementos que no se encuentren en ella
for dato in datos:
    print(f"Procesando el elemento {dato}...")

    if dato not in lista_final:
        lista_final.append(dato)
    else:
        print(f"\nEl elemento {dato} se encuentra repetido en la lista de datos.\n")


# Muestro el resultado
print(f"Lista inicial: {datos}")
print(f"Lista final: {lista_final}\n")


'''
Actividad 5 - Crear una lista con los nombres de 8 estudiantes presentes en clase.
 * Preguntar al usuario si quiere agregar un nuevo estudiante o eliminar uno existente.
 * Mostrar la lista final actualizada.
'''

print("\n--- Actividad 5 ---\n")

# Creo una lista con los nombres de 8 estudiantes presentes en clase
estudiantes = ["Juan", "María", "Pedro", "Ana", "Luis", "Sofía", "Carlos", "Lucía"]

# Muestro la lista de estudiantes
print(f"Estudiantes presentes en clase: {estudiantes}")

# Inicializo variable para controlar el menú principal
salir = False

# Mientras la acción ingresada no sea válida, muestro un mensaje de alerta y solicito nuevamente la acción
while not salir:
    print("\nMenu de opciones:")
    print("1 - Agregar un nuevo estudiante")
    print("2 - Eliminar un estudiante existente")
    print("3 - Salir del programa\n")

    # Solicito una opción válida
    opcion = input("Opción: ")

    # Valido que la opción sea un número
    if not opcion.isdigit() or opcion not in "123":
        print("\nATENCION! Debe ingresar un número válido...")
        continue

    if opcion == "1":
        # Solicito el nombre del nuevo estudiante al usuario
        nuevo_estudiante = input("\nIngrese el nombre del nuevo estudiante: ")

        # Mientras el nombre del nuevo estudiante no csontenga solo letras, muestro un mensaje de alerta y solicito nuevamente el nombre
        while not nuevo_estudiante.isalpha():
            print("\nATENCION... El nombre del estudiante debe contener solo letras.\n")
            
            nuevo_estudiante = input("Ingrese nuevamente el nombre del nuevo estudiante: ")

        # Agrego el nuevo estudiante a la lista de estudiantes
        estudiantes.append(nuevo_estudiante)
    elif opcion == "2":
        # Solicito el nombre del estudiante a eliminar al usuario
        estudiante_a_eliminar = input("\nIngrese el nombre del estudiante a eliminar: ")

        # Mientras el nombre del estudiante a eliminar no se encuentre en la lista de estudiantes, muestro un mensaje de alerta y solicito nuevamente el nombre
        while estudiante_a_eliminar not in estudiantes:
            print("\nATENCION... El estudiante ingresado no se encuentra en la lista.\n")
            
            estudiante_a_eliminar = input("Ingrese nuevamente el nombre del estudiante a eliminar: ")

        # Elimino el estudiante de la lista de estudiantes
        estudiantes.remove(estudiante_a_eliminar)
    elif opcion == "3":
        salir = True

# Muestro la lista final actualizada
print(f"\nLista final de estudiantes: {estudiantes}\n")


'''
Actividad 6 - Dada una lista con 7 numeros, rotar todos los elementos a una posicion hacia la derecha
(el ultimo elemento pasa a ser el primero).
'''

print("\n--- Actividad 6 ---\n")

# Declaro la lista con 7 numeros
numeros = list(range(1, 8))

# Muestro la lista original
print(f"Lista original: {numeros}")

# Roto todos los elementos de la lista a una posición hacia la derecha
# Tomo el ultimo elemento de la lista, luego concateno el resto de los elementos sin el ultimo
numeros = [numeros[-1]] + numeros[:-1]

# Muestro la lista rotada
print(f"Lista rotada: {numeros}\n")


'''
Actividad 7 - Crear una matriz (lista anidada) de 7x2 con las temperaturas minimas y máximas de una semana.
 * Calcular el promedio de las minimas y el de las maximas.
 * Mostrar en que dia se registro la mayour amplitud termica.
'''

print("\n--- Actividad 7 ---\n")

# Creo una matriz (lista anidada) de 7x2 con las temperaturas minimas y máximas de una semana
temperaturas = [
    [15, 25], # Lunes
    [17, 28], # Martes
    [14, 22], # Miércoles
    [16, 30], # Jueves
    [13, 27], # Viernes
    [18, 26], # Sábado
    [12, 24]  # Domingo
]

# Inicializo variables para acumular la suma de las temperaturas minimas y maximas
suma_minimas = 0
suma_maximas = 0    

# Inicializo variables para almacenar la mayor amplitud termica y el dia en que se registro
mayor_amplitud = 0
dia_mayor_amplitud = ""

# Itero sobre la matriz de temperaturas y calculo la suma de las temperaturas minimas y maximas, y la amplitud termica de cada dia
for i in range(len(temperaturas)):
    # Variable para facilitar lectura, calculos y validaciones
    minima = temperaturas[i][0]
    maxima = temperaturas[i][1]

    # Acumulo la suma de las temperaturas minimas y maximas
    suma_minimas += minima
    suma_maximas += maxima

    # Calculo la amplitud termica del dia
    amplitud = maxima - minima

    # Actualizo la mayor amplitud termica y el dia en que se registro
    if amplitud > mayor_amplitud:
        mayor_amplitud = amplitud

        if i == 0:
            dia_mayor_amplitud = "Lunes"
            amplitud = mayor_amplitud
        elif i == 1:
            dia_mayor_amplitud = "Martes"
        elif i == 2:
            dia_mayor_amplitud = "Miércoles"
        elif i == 3:
            dia_mayor_amplitud = "Jueves"
        elif i == 4:
            dia_mayor_amplitud = "Viernes"
        elif i == 5:
            dia_mayor_amplitud = "Sábado"
        elif i == 6:
            dia_mayor_amplitud = "Domingo"

# Muestro la matriz de temperaturas
print("Día\t\tMínima\tMáxima")
print("-" * 30)

for i in range(len(temperaturas)):
    # Variable para facilitar lectura, calculos y validaciones
    minima = temperaturas[i][0]
    maxima = temperaturas[i][1]

    if i == 0:
        print(f"Lunes\t\t{minima}\t{maxima}")
    elif i == 1:
        print(f"Martes\t\t{minima}\t{maxima}")
    elif i == 2:
        print(f"Miércoles\t{minima}\t{maxima}")
    elif i == 3:
        print(f"Jueves\t\t{minima}\t{maxima}")
    elif i == 4:
        print(f"Viernes\t\t{minima}\t{maxima}")
    elif i == 5:
        print(f"Sábado\t\t{minima}\t{maxima}")
    elif i == 6:
        print(f"Domingo\t\t{minima}\t{maxima}")

# Calculo y muestro el promedio de las temperaturas minimas y maximas
print(f"\nPromedio de las temperaturas mínimas: {suma_minimas / len(temperaturas)}")
print(f"Promedio de las temperaturas máximas: {suma_maximas / len(temperaturas)}")

# Muestro el dia en que se registro la mayor amplitud termica
print(f"\nDía con la mayor amplitud térmica ({mayor_amplitud}°): {dia_mayor_amplitud}\n")


'''
Actividad 8 - Crear una matriz con las notas de 5 estudiantes en 3 materias.
 * Mostrar el promedio de cada estudiante.
 * Mostrar el promedio de cada materia.
'''

print("\n--- Actividad 8 ---\n")

# Creo una matriz aleatoria con las notas de 5 estudiantes en 3 materias
notas_estudiantes = []

for i in range(5):
    notas_estudiantes.append([
        round(random.uniform(1, 10), 2) for _ in range(3)
    ])

# Muestro la matriz de notas
print("Estudiante\tMateria 1\tMateria 2\tMateria 3")
print("-" * 57)

for i in range(len(notas_estudiantes)):
    # Variable para facilitar lectura, calculos y validaciones
    notas = notas_estudiantes[i]

    print(f"Alumno {i + 1}\t{notas[0]}\t\t{notas[1]}\t\t{notas[2]}")

# Calculo y muestro el promedio de cada estudiante
print("\nPromedio de cada estudiante:")

for i in range(len(notas_estudiantes)):
    # Variable para facilitar lectura, calculos y validaciones
    notas = notas_estudiantes[i]

    print(f"Alumno {i + 1}: {(sum(notas) / len(notas)):.2f}")

# Calculo y muestro el promedio de cada materia
print("\nPromedio de cada materia:")

for j in range(3):
    # Variable para facilitar lectura, calculos y validaciones
    suma_materia = sum(notas_estudiantes[i][j] for i in range(5))

    print(f"Materia {j + 1}: {(suma_materia / 5):.2f}")


'''
Actividad 9 - Representar un tablero de Ta-Te-Ti como una lista de listas (3x3).
 * Inicializarlo con guiones "-" representando casillas vacías.
 * Permitir que dos jugadores ingresen posiciones (fila, columna) para colocar "X" o "O".
 * Mostrar el tablero después de cada jugada.
'''

print("\n--- Actividad 9 ---\n")

# Inicializo el tablero con guiones "-"
tablero = [["-" for _ in range(3)] for _ in range(3)]

# Muestro el tablero inicial
print("Tablero inicial:")
for fila in tablero:
    print("\t".join(fila))

# Inicializo variable para controlar el turno de los jugadores
turno_jugador_1 = True

# Inicializo variable para controlar el estado del juego
juego_terminado = False

while not juego_terminado:
    # Determino el símbolo del jugador actual
    simbolo_jugador = "X" if turno_jugador_1 else "O"

    # Solicito al jugador actual que ingrese la fila y columna donde desea colocar su símbolo
    print(f"\nTurno del jugador {'1 (X)' if turno_jugador_1 else '2 (O)'}")
    
    fila = input("Ingrese la fila (0, 1 o 2): ")
    columna = input("Ingrese la columna (0, 1 o 2): ")

    # Valido que la fila y columna ingresadas sean números válidos
    if not fila.isdigit() or not columna.isdigit() or int(fila) not in range(3) or int(columna) not in range(3):
        print("\nATENCION! Debe ingresar una fila y columna válidas (0, 1 o 2).")
        continue

    fila = int(fila)
    columna = int(columna)

    # Valido que la casilla seleccionada esté vacía
    if tablero[fila][columna] != "-":
        print("\nATENCION! La casilla seleccionada ya está ocupada.")
        continue

    # Coloco el símbolo del jugador en la casilla seleccionada
    tablero[fila][columna] = simbolo_jugador

    # Muestro el tablero después de la jugada
    print("\nTablero actualizado:")
    for fila in tablero:
        print("\t".join(fila))

    # Aquí se podrían agregar las condiciones para determinar si un jugador ha ganado o si el juego ha terminado en empate

    # Cambio el turno al otro jugador
    turno_jugador_1 = not turno_jugador_1