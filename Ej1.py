total_bruto = 0
total_final = 0
total_unidades = 0
suma_precios = 0

cont_efectivo = 0
cont_tarjeta = 0
cont_transferencia = 0

mayor_tarjeta = 0
bandera = False

for i in range(25):

    print(f"\nVenta {i + 1}")

    # Tipo de producto
    tipo = input("Tipo (alimento/limpieza/perfumeria): ")
    while tipo != "alimento" and tipo != "limpieza" and tipo != "perfumeria":
        tipo = input("Error. Reingrese: ")

    # Cantidad
    cantidad = int(input("Cantidad (1-20): "))
    while cantidad < 1 or cantidad > 20:
        cantidad = int(input("Error. Reingrese: "))

    # Precio
    precio = float(input("Precio unitario: "))
    while precio <= 0:
        precio = float(input("Error. Reingrese: "))

    # Forma de pago
    pago = input("Pago (efectivo/tarjeta/transferencia): ")
    while pago != "efectivo" and pago != "tarjeta" and pago != "transferencia":
        pago = input("Error. Reingrese: ")

    subtotal = cantidad * precio

    total_bruto += subtotal
    total_unidades += cantidad
    suma_precios += precio

    # Descuento efectivo
    if pago == "efectivo":
        subtotal = subtotal - (subtotal * 0.05)
        cont_efectivo += 1

    elif pago == "tarjeta":
        cont_tarjeta += 1

        if bandera == False or subtotal > mayor_tarjeta:
            mayor_tarjeta = subtotal
            bandera = True

    else:
        cont_transferencia += 1

    total_final += subtotal

# Descuento general
if total_unidades > 400:
    total_final = total_final - (total_final * 0.20)

elif total_unidades > 200:
    total_final = total_final - (total_final * 0.10)

# Promedio
promedio = suma_precios / 25

# Forma más usada
if cont_efectivo > cont_tarjeta and cont_efectivo > cont_transferencia:
    forma = "efectivo"

elif cont_tarjeta > cont_transferencia:
    forma = "tarjeta"

else:
    forma = "transferencia"

# Resultados
print("\nTOTAL BRUTO:", total_bruto)
print("TOTAL FINAL:", total_final)

if bandera == True:
    print("VENTA MAS CARA CON TARJETA:", mayor_tarjeta)
else:
    print("NO HUBO PAGOS CON TARJETA")

print("PROMEDIO PRECIOS:", promedio)
print("FORMA MAS UTILIZADA:", forma)
