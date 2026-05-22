# EJERCICIO 1
# Contar los vocales

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
# BUSCAR PRIMERA INCIDENCIA

def buscar_caracter(cadena, caracter):

    for i in range(len(cadena)):

        if cadena[i] == caracter:

            return i

    return -1

# PRUEBA

print(buscar_caracter("Python", "t"))

# EJERCICIO 3
# PALINDROMO

def es_palindromo(cadena):

    invertida = ""

    for i in range(len(cadena) - 1, -1, -1):

        invertida += cadena[i]

    if cadena == invertida:

        return True

    return False

# PRUEBA

print(es_palindromo("neuquen"))
print(es_palindromo("python"))

# EJERCICIO 4
# SUPRIMIR REPETIDOS

def suprimir_repetidos(cadena):

    nueva = ""

    for caracter in cadena:

        if caracter not in nueva:

            nueva += caracter

    return nueva


# PRUEBA

print(suprimir_repetidos("Hooola"))

# EJERCICIO 5
# SUPRIMIR VOCALES


def suprimir_vocales(cadena):

    nueva = ""

    for caracter in cadena:

        if caracter != "a" and caracter != "e" and caracter != "i" and caracter != "o" and caracter != "u":

            nueva += caracter

    return nueva


# PRUEBA

print(suprimir_vocales("Hola"))


# EJERCICIO 6
# CONTAR SUBCADENAS

def contar_subcadena(cadena, subcadena):

    contador = 0

    largo = len(subcadena)

    for i in range(len(cadena) - largo + 1):

        parte = ""

        for j in range(largo):

            parte += cadena[i + j]

        if parte == subcadena:

            contador += 1

    return contador


# PRUEBA

print(contar_subcadena("El pan del panadero", "pan"))
