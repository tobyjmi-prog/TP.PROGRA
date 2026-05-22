# 1
def calcular_area_rectangulo(base, altura):
    area = base * altura
    return area


# 2
def calcular_area_circulo(radio):
    area = 3.14 * (radio ** 2)
    return area


# 3
def verificar_par_impar(numero):

    if numero % 2 == 0:
        print("El numero es par")
    else:
        print("El numero es impar")


# 4
def es_par(numero):

    if numero % 2 == 0:
        return True
    else:
        return False


# 5
def mayor_tres(num1, num2, num3):

    if num1 > num2 and num1 > num3:
        return num1

    elif num2 > num3:
        return num2

    else:
        return num3


# 6
def calcular_potencia(base, exponente):
    resultado = base ** exponente
    return resultado


# 7
def es_primo(numero):

    if numero < 2:
        return False

    for i in range(2, numero):

        if numero % i == 0:
            return False

    return True


# 8
def mostrar_primos(numero):

    contador = 0

    for i in range(1, numero + 1):

        if es_primo(i):
            print(i)
            contador += 1

    return contador


# 9
def tabla_multiplicar(numero, inicio=1, fin=10):

    for i in range(inicio, fin + 1):
        print(f"{numero} x {i} = {numero * i}")


# 10
def pedir_entero():

    numero = int(input("Ingrese un numero entero: "))
    return numero


# 11
def pedir_flotante():

    numero = float(input("Ingrese un numero flotante: "))
    return numero


# 12
def pedir_cadena():

    texto = input("Ingrese una cadena: ")
    return texto


# 13
def pedir_entero_validado(mensaje, minimo, maximo):

    numero = int(input(mensaje))

    while numero < minimo or numero > maximo:
        numero = int(input("Error. Reingrese: "))

    return numero


def pedir_flotante_validado(mensaje, minimo, maximo):

    numero = float(input(mensaje))

    while numero < minimo or numero > maximo:
        numero = float(input("Error. Reingrese: "))

    return numero


def pedir_cadena_validada(mensaje):

    texto = input(mensaje)

    while texto == "":
        texto = input("Error. Reingrese: ")

    return texto
