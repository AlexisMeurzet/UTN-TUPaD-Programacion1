"""
EJERCICIO 1 - CAJA DEL KIOSCO
Programa que simula una compra con validaciones y cálculo de totales.
"""

# Constante para el porcentaje de descuento
DESCUENTO_PORCENTAJE = 0.1

# Solicito el nombre del cliente
nombre = input("\nPor favor, ingrese su nombre: ")

# Si el nombre no contiene solo letras, lo solicito nuevamente
while not nombre.isalpha():
    print("\nATENCION! El nombre es obligatorio y solo debe contener letras...\n")

    nombre = input("Por favor, ingrese nuevamente su nombre: ")

# Solicito la cantidad de productos a comprar
cant_productos = input("\n¿Cuántos productos desea?: ")

# Si no es un numero entero positivo o es cero, lo solicito nuevamente
while not cant_productos.isdigit() or int(cant_productos) == 0:
    print("\nATENCION! La cantidad debe estar compuesta por dígitos entre 1 y 9...\n")

    cant_productos = input("Ingrese nuevamente ¿cuántos productos desea?: ")

# Inicializo variable para almacenar la información de los productos
info_productos = ""

# Inicializo variables para calcular totales
total = 0
total_con_descuentos = 0
ahorro = 0

# Proceso la cantidad de productos
for i in range(int(cant_productos)):
    # Nombre del producto
    producto = f"Producto {i + 1}"

    # Solicito el precio del producto
    precio = input(f"\nIngrese el precio de {producto}: ")

    # Si no es un numero entero positivo, lo solicito nuevamente
    while not precio.isdigit():
        print("\nATENCION! El precio debe estar compuesto por dígitos entre 0 y 9...\n")

        precio = input(f"Ingrese nuevamente el precio de {producto}: ")
    
    # Transformo el precio a numero entero
    precio = int(precio)

    # Sumo el precio al total
    total += precio

    # Solicito si tiene descuento
    tiene_descuento = input("¿Posee descuento (S/N)?: ")

    # Solicito nuevamente mientras descuento != s o descuento != n
    while tiene_descuento not in "sSnN":
        print("\nATENCION! Debe ingresar 'S' para sí o 'N' para no...\n")

        tiene_descuento = input("Ingrese nuevamente ¿posee descuento (S/N)?: ")

    # Concateno la información del producto
    info_productos += f"{producto} - Precio: {precio} Descuento (S/N): {tiene_descuento}\n"

    # Si posee descuento, aplico el 10% al producto
    if tiene_descuento in "sS":
        # Calculo el descuento
        monto_descuento = precio * DESCUENTO_PORCENTAJE

        # Acumulo el valor descontado en ahorro
        ahorro += monto_descuento

        # Resto el descuento al precio del producto
        precio -= monto_descuento

    # Sumo el precio con descuento al total con descuento
    total_con_descuentos += precio

# Formateo los resultados para el print
total_sin_descuentos_formateado = f"${total:.2f}"
total_con_descuentos_formateado = f"${total_con_descuentos:.2f}"
ahorro_formateado = f"${ahorro:.2f}"
promedio_formateado = f"${(total_con_descuentos / int(cant_productos)):.2f}"

# Imprimo los resultados
print(
    f"\nCliente: {nombre}\n" + 
    f"Cantidad de productos: {cant_productos}\n" +
    info_productos + "\n"
    f"Total sin descuentos: {total_sin_descuentos_formateado}\n" +
    f"Total con descuentos: {total_con_descuentos_formateado}\n" +
    f"Ahorro: {ahorro_formateado}\n" +
    f"Promedio por producto: {promedio_formateado}"
)