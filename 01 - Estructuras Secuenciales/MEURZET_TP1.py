# Actividad 1 - Crear un programa que imprima por pantalla el mensaje: "Hola Mundo!".

print("\n-- Actividad 1 --\n")

# Imprimo el mensaje
print("Hola Mundo!\n")


# Actividad 2 - Crear un programa que pida al usuario su nombre e imprima por pantalla un saludo usando
# el nombre ingresado. Por ejemplo: si el usuarion ingrasa "Marcos", el programa debe imprimir
# por pantalla "Hola Marcos!". Consejo: esto será mas sencillo si utilizas print(f...) para 
# realizar la impresion por pantalla.

print("\n-- Actividad 2 --\n")

# Solicito el nombre al usuario
nombre = input("Ingrese su nombre: ")

# Imprimo el saludo
print(f"\nHola {nombre}! Un gusto saludarte.\n")


# Actividad 3 - Crear un programa que pida al usuario su nombre, apellido, edad y lugar de residencia e 
# imprima por pantalla una oracion con los datos ingresados. Por ejemplo: si el usuario ingresa 
# "Marcos", "Pérez", "30" y "Argentina", el programa debe imprimir "Soy Marcos Pérez, tengo 30
# años y vivo en Argentina". Consejo: esto será mas sencillo si utilizas print(f...) para 
# realizar la impresion por pantalla.

print("\n-- Actividad 3 --\n")

# Solicito el nombre
nombre = input("Ingrese su nombre: ")

# Solicito el apellido
apellido = input("\nIngrese su apellido: ")

# Solicito su edad
edad = int(input("\nIngrese su edad: "))

# Solicito su lugar de residencia
residencia = input("\nIngrese su lugar de residencia: ")

# Imprimo la oracion
print(f"\nHola, soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}.\n")


# Actividad 4 - Crear un programa que pida al usuario el radio de un círculo e imprima por pantalla 
# su área y su perímetro.

print("\n-- Actividad 4 --\n")

# importo libreria math para utilizar el numero pi
import math

# Solicito el radio del círculo
radio = float(input("Ingrese el radio del circulo: "))

# Calculo el área
area = round(math.pi * (radio ** 2), 2)

# Calculo el perímetro
perimetro = round(2 * math.pi * radio, 2)

# Imprimo el resultado
print(f"\nEl area del círculo es de {area} y su perímetro es igual a {perimetro}.\n")


# Actividad 5 - Crear un programa que pida al usuario una cantidad de segundos e imprima por pantalla 
# a cuantas horas equivale.

print("\n-- Actividad 5 --\n")

# Solicito al usuario una cantidad de segundos
segundos = int(input("Ingrese la cantidad de segundos: "))

# Imprimo el resultado en hrs
print(f"\n{segundos} segundos equivalen a {round(segundos / 3600, 2)} horas.\n")


# Actividad 6 - Crear un programa que pida al usuario un número e imprima por pantalla la tabla de 
# multiplicar de dicho número.

print("\n-- Actividad 6 --\n")

# Solicito al usuario el número a multiplicar
numero = int(input("Ingrese el numero a multiplicar: "))

# Imprimo la tabla de multiplicar del número ingresado
print(
    f"\nTabla del número {numero}\n",
    f"\n{numero} x 0 = {numero * 0}",
    f"\n{numero} x 1 = {numero * 1}",
    f"\n{numero} x 2 = {numero * 2}",
    f"\n{numero} x 3 = {numero * 3}",
    f"\n{numero} x 4 = {numero * 4}",
    f"\n{numero} x 5 = {numero * 5}",
    f"\n{numero} x 6 = {numero * 6}",
    f"\n{numero} x 7 = {numero * 7}",
    f"\n{numero} x 8 = {numero * 8}",
    f"\n{numero} x 9 = {numero * 9}",
    f"\n{numero} x 10 = {numero * 10}\n",
)


# Actividad 7 - Crear un programa que pida al usuario dos números enteros distintos de 0 y muestre por
# pantalla el resultado de sumarlos, dividirlos, multiplicarlos y restarlos.

print("\n-- Actividad 7 --\n")

# Solicito el primer numero
numero1 = int(input("Ingrese el primer número (distinto de 0): "))

# Solicito el segundo numero
numero2 = int(input("Ingrese el segundo número (distinto de 0): "))

# Imprimo resultados
print(
    f"\n{numero1} + {numero2} = {numero1 + numero2}",
    f"\n{numero1} ÷ {numero2} = {round(numero1 / numero2, 2)}",
    f"\n{numero1} x {numero2} = {numero1 * numero2}",
    f"\n{numero1} - {numero2} = {numero1 - numero2}\n"
)


# Actividad 8 - Crear un programa que pida al usuario su altura y su peso e imprima por pantalla su índice
# de masa corporal. Tener en cuenta que el índice de masa corporal se calcula del siguiente modo:
#
#            peso en kg
#   IMC = -----------------
#           (altura en m)²

print("\n-- Actividad 8 --\n")

# Solucito al usuario su altura
altura = float(input("Ingrese su altura (mts): "))

# Solicito al usuario su peso
peso = float(input("Ingrese su peso (kg): "))

# imprimo el resultado
print(f"\nSu índice de masa corporal (IMC) es de: {round(peso / altura ** 2, 2)}\n")


# Actividad 9 - Crear un programa que pida al usuario una temperatura en grados Celsius e imprima por pantalla
# su equivalente en grados Fahrenheit. Tener en cuenta la siguiente equivalencia:
#
#                                9
#   Temperatura en Fahrenheit = --- . Temperatura en Celsius + 32
#                                5

print("\n-- Actividad 9 --\n")

# Solicito temperatura
temperatura = int(input("Ingrese una temperatura en ˚C: "))

# Imprimo resultado
print(f"\nEl equivalente a {temperatura}˚C es {round((9 / 5) * temperatura + 32, 2)} ˚F.\n")


# Actividad 10 - Crear un programa que pida al usuario 3 números e imprima por pantalla el promedio de dichos
# números

print("\n-- Actividad 10 --\n")

# Solicito el primer número
numero1 = int(input("Ingrese un número: "))

# Solicito el segundo número
numero2 = int(input("Ingrese otro número: "))

# Solicito el tercer número
numero3 = int(input("Ingrese un número más: "))

# Imprimo el resultado
print(f"\nEl promedio de los números ingresados es: {round((numero1 + numero2 + numero3) / 3, 2)}.\n")