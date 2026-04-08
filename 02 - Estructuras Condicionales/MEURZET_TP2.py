# Actividad 1 - Escribir un programa que solicite la edad del usuario. Si el usuario es mayor de 18 
# años, deberá mostrar un mensaje en pantalla que diga “Es mayor de edad”.

print("\n-- Actividad 1 --\n")

# Solicito la edad del usuario
edad = int(input("Ingrese su edad: "))

# Evaluo la edad ingresada y segun la condicion imprimo el mensaje en pantalla.
if edad >= 18:
    print("\nEs mayor de edad\n")
else:
    print("\nEs menor de edad\n")


# Actividad 2 - Escribir un programa que solicite su nota al usuario. Si la nota es mayor o igual a 6, 
# deberá mostrar por pantalla un mensaje que diga “Aprobado”; en caso contrario deberá mostrar el
# mensaje “Desaprobado”.

print("\n-- Actividad 2 --\n")

# Solicito una nota al usuario
nota = int(input("Ingrese su nota: "))

# Imprimo el resultado al evaluar la nota
print("\nAprobado!\n") if nota >= 6 else print("\nDesaprobado...\n")


# Actividad 3 - Escribir un programa que permita ingresar solo números pares. Si el usuario ingresa 
# un número par, imprimir por en pantalla el mensaje "Ha ingresado un número par"; en caso contrario,
# imprimir por pantalla "Por favor, ingrese un número par". 

print("\n-- Actividad 3 --\n")

# Solicito un numero al usuario
numero = int(input("Ingrese un número: "))

# Imprimo el resultado de evaluar el numero ingresado
print("\nHa ingresado un número par.\n") if numero % 2 == 0 else print("\nPor favor, ingrese un número par.\n")


# Actividad 4 - Escribir un programa que solicite al usuario su edad e imprima por pantalla a cuál de 
# las siguientes categorías pertenece:
# • Niño/a: menor de 12 años.
# • Adolescente: mayor o igual que 12 años y menor que 18 años.
# • Adulto/a joven: mayor o igual que 18 años y menor que 30 años.
# • Adulto/a: mayor o igual que 30 años.

print("\n-- Actividad 4 --\n")

# Solicito la edad al usuario
edad = int(input("Ingrese su edad: "))

# Evaluo la edad ingresada y segun la condicion imprimo la categoria.
if edad < 12:
    print("\nNiño/a\n")
elif edad >= 12 and edad < 18:
    print("\nAdolescente\n")
elif edad >= 18 and edad < 30:
    print("\nAdulto/a joven\n")
else:
    print("\nAdulto/a\n")


# Actividad 5 - Escribir un programa que permita introducir contraseñas de entre 8 y 14 caracteres
# (incluyendo 8 y 14). Si el usuario ingresa una contraseña de longitud adecuada, imprimir por en
# pantalla el mensaje "Ha ingresado una contraseña correcta"; en caso contrario, imprimir por
# pantalla "Por favor, ingrese una contraseña de entre 8 y 14 caracteres".

print("\n-- Actividad 5 --\n")

# Solicito una contraseña
contraseña = input("Ingrese una contraseña de entre 8 y 14 caracteres: ")

# Evaluo la contraseña ingresada e imprimo el mensaje correspondiente en pantalla
if 8 <= len(contraseña) <= 14:
    print("\nHa ingresado una contraseña correcta.\n")
else:
    print("\nPor favor, ingrese una contraseña de entre 8 y 14 caracteres.\n")


# Actividad 6 - Escribir un programa que solicite al usuario el consumo mensual de energía eléctrica en
# kilovatios (kWh) e indique la categoría del consumo según el siguiente criterio:
# • Menor que 150 kWh: “Consumo bajo”.
# • Entre 150 y 300 kWh (inclusive): “Consumo medio”.
# • Mayor que 300 kWh: “Consumo alto”.
# Además, si el consumo supera los 500 kWh, mostrar un mensaje adicional que diga: “Considere medidas
# de ahorro energético”.
# El programa debe imprimir por pantalla la categoría correspondiente.

print("\n-- Actividad 6 --\n")

# Solicito al usuario su consumo
kilovatios = int(input("Ingrese su consumo mensual de energía eléctrica en kilovatios (kWh): "))

# Evaluo el consumo ingresado e imprimo la categoria correspondiente.
if kilovatios < 150:
    print("\nConsumo bajo\n")
elif 150 <= kilovatios <= 300:
    print("\nConsumo medio\n")
elif 300 < kilovatios <= 500:
    print("\nConsumo alto\n") 
else:
    print("\nConsidere medidas de ahorro energético\n")


# Actividad 7 - Escribir un programa que solicite una frase o palabra al usuario. Si el string ingresado
# termina con vocal, añadir un signo de exclamación al final e imprimir el string resultante por
# pantalla; en caso contrario, dejar el string tal cual lo ingresó el usuario e imprimirlo por
# pantalla.

print("\n-- Actividad 7 --\n")

# Declaro las vocales
vocales = "AEIOUaeiou"

# Solicito una frase o palabra al usuario
texto = input("Ingrese una frase o palabra: ")

# Si la frase o palabra finaliza con vocal, imprimo la frase con el signo de exclamación al final.
# Sino imprimo la frase o palabra tal cual se ingresó.
print(f"\n{texto}!\n") if texto[-1] in vocales else print(f"\n{texto}\n")


# Actividad 8 - Escribir un programa que solicite al usuario que ingrese su nombre y el número 1, 2 o 3
# dependiendo de la opción que desee:
#   1. Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO.
#   2. Si quiere su nombre en minúsculas. Por ejemplo: pedro.
#   3. Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro.
# El programa debe transformar el nombre ingresado de acuerdo con la opción seleccionada por el usuario
# e imprimir el resultado por pantalla. 

print("\n-- Actividad 8 --\n")

# Solicito el nombre al usuario
nombre = input("Ingrese su nombre: ")

# Imprimo por pantalla el menú con las opciones
print()
print("-" * 53)
print("Menu")
print("-" * 53)

print("1 - Imprimir nombre en mayúsculas")
print("2 - Imprimir nombre en minúsculas")
print("3 - Imprimir nombre con la primera letra en mayúscula")
print("-" * 53)

# Solicito una opción al usuario
opcion = int(input("Elija una opcion (1, 2 o 3): "))

# Evaluo la opcion ingresada e imprimo el resultado transformado.
if opcion == 1:
    print("\n", f"Su nombre en mayúsculas: {nombre.upper()}\n")
elif opcion == 2:
    print("\n", f"Su nombre en minúsculas: {nombre.lower()}\n")
elif opcion == 3:
    print("\n", f"Su nombre con la primera letra en mayúscula: {nombre.title()}\n")
else:
    print("\n", "La opcion elegida no existe\n")


# Actividad 9 - Escribir un programa que pida al usuario la magnitud de un terremoto, clasifique la
# magnitud en una de las siguientes categorías según la escala de Richter e imprima el resultado
# por pantalla:
# • Menor que 3: "Muy leve" (imperceptible).
# • Mayor o igual que 3 y menor que 4: "Leve" (ligeramente perceptible).
# • Mayor o igual que 4 y menor que 5: "Moderado" (sentido por personas, pero generalmente no causa 
#   daños).
# • Mayor o igual que 5 y menor que 6: "Fuerte" (puede causar daños en estructuras débiles).
# • Mayor o igual que 6 y menor que 7: "Muy Fuerte" (puede causar daños significativos).
# • Mayor o igual que 7: "Extremo" (puede causar graves daños a gran escala).

print("\n-- Actividad 9 --\n")

# Solicito al usuario la magnitud de un terremoto.
magnitud = float(input("Ingrese la magnitud del terremoto: "))

# Evaluo la magnitud ingresada e imprimo por pantalla la categoria del terremoto.
if magnitud < 3:
    print("\nMuy leve\n")
elif 3 <= magnitud < 4:
    print("\nLeve\n")
elif 4 <= magnitud < 5:
    print("\nModerado\n")
elif 5 <= magnitud < 6:
    print("\nFuerte\n")
elif 6 <= magnitud < 7:
    print("\nMuy Fuerte\n")
else:
    print("\nExtremo\n")


# Actividad 10 - Utilizando la información aportada en la siguiente tabla sobre las estaciones del año:
#
# |---------------------------------------------------------------------------|
# |         PERIODO DEL AÑO              |   ESTACION EN EL  | ESTACION EN EL |
# |                                      |  HEMISFERIO NORTE | HEMISFERIO SUR |
# |-------------------------------------------------------------------------- |
# | Desde el 21 de diciembre hasta el 20 |      Invierno     |     Verano     |
# | de marzo (incluidos)                 |                   |                |
# |---------------------------------------------------------------------------|
# | Desde el 21 de marzo hasta el 20 de  |      Primavera    |     Otoño      |
# | junio (incluidos)                    |                   |                |
# |---------------------------------------------------------------------------|
# | Desde el 21 de junio hasta el 20 de  |       Verano      |    Invierno    |
# | septiembre (incluidos)               |                   |                |
# |---------------------------------------------------------------------------|
# | Desde el 21 de septiembre hasta el   |        Otoño      |    Primavera   |
# | 20 de diciembre (incluidos)          |                   |                |
# |---------------------------------------------------------------------------|
#
# Escribir un programa que pregunte al usuario en cuál hemisferio se encuentra (N/S), qué mes
# del año es y qué día es. El programa deberá utilizar esa información para imprimir por pantalla
# si el usuario se encuentra en otoño, invierno, primavera o verano.

print("\n-- Actividad 10 --\n")

# Solicito al usuario el hemisferio en el que se encuentra
hemisferio = input("Ingrese su hemisferio (N/S): ")

# Solicito al usuario el mes actual
mes = int(input("Ingrese el mes en curso (1 al 12): "))

# Solicito al usuario el dia actual
dia = int(input("Ingrese el dia en curso (1 al 31): "))

# Evaluo el día y mes ingresados y asocio los valores correspondientes a dos variables 
# (estacion_norte y estacion_sur)
if (mes == 12 and dia >= 21) or mes <= 2 or (mes == 3 and dia <= 20):
    estacion_norte = "Invierno"
    estacion_sur = "Verano"

elif (mes == 3 and dia >= 21) or mes <= 5 or (mes == 6 and dia <= 20):
    estacion_norte = "Primavera"
    estacion_sur = "Otoño"

elif (mes == 6 and dia >= 21) or mes <= 8 or (mes == 9 and dia <= 20):
    estacion_norte = "Verano"
    estacion_sur = "Invierno"

else:
    estacion_norte = "Otoño"
    estacion_sur = "Primavera"

# Evaluo el hemisferio ingresado e imprimo en pantalla la estacion correspondiente.
if hemisferio == "N":
    print("\nLa estación es:", estacion_norte)
elif hemisferio == "S":
    print("\nLa estación es:", estacion_sur)
else:
    print("\nHemisferio inválido")