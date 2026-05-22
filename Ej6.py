
# EJERCICIO 1


def contar_vocales(cadena):

    matriz = [
        ["a", 0],
        ["e", 0],
        ["i", 0],
        ["o", 0],
        ["u", 0]
    ]

    for caracter in cadena:

        if caracter == "a":

            matriz[0][1] += 1

        elif caracter == "e":

            matriz[1][1] += 1

        elif caracter == "i":

            matriz[2][1] += 1

        elif caracter == "o":

            matriz[3][1] += 1

        elif caracter == "u":

            matriz[4][1] += 1

    return matriz


# PRUEBA

resultado = contar_vocales("murcielaguito")

for fila in resultado:

    print(fila[0], fila[1])


# EJERCICIO 2


def buscar_caracter(cadena, caracter):

    for i in range(len(cadena)):

        if cadena[i] == caracter:

            return i

    return -1


# PRUEBA

print(buscar_caracter("Python", "t"))


# EJERCICIO 3

def es_palindromo(cadena):

    invertida = ""

    for i in range(len(cadena) - 1, -1, -1):

        invertida += cadena[i]

    if cadena == invertida:

        return True

    else:

        return False

# PRUEBA 

print(es_palindromo("neuquen"))
print(es_palindromo("python"))

# EJERCICIO 4

def suprimir_repetidos(cadena):

    nueva = ""

    for caracter in cadena:

        existe = False

        for letra in nueva:

            if letra == caracter:

                existe = True

        if existe == False:

            nueva += caracter

    return nueva


# PRUEBA

print(suprimir_repetidos("Hooola"))


# EJERCICIO 5

def suprimir_vocales(cadena):

    nueva = ""

    for caracter in cadena:

        if caracter != "a" and caracter != "e" and caracter != "i" and caracter != "o" and caracter != "u":

            nueva += caracter

    return nueva


# PRUEBA

print(suprimir_vocales("Hola"))

# EJERCICO 6


def contar_subcadena(cadena, subcadena):

    contador = 0

    largo_subcadena = len(subcadena)

    for i in range(len(cadena) - largo_subcadena + 1):

        coincide = True

        for j in range(largo_subcadena):

            if cadena[i + j] != subcadena[j]:

                coincide = False

        if coincide == True:

            contador += 1

    return contador


# PRUEBA

print(contar_subcadena("El pan del panadero", "pan"))
