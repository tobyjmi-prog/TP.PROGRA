
# EJERCICIO 1

def contar_letra(letra, cadena):

    contador = 0

    for caracter in cadena:

        if caracter == letra:

            contador += 1

    return contador


# PRUEBA

texto = "programacion"

print(contar_letra("a", texto))

# EJERCICIO 2

def recortar_cadena(cadena, indice_inicio, indice_fin):

    if indice_inicio < 0 or indice_fin >= len(cadena):

        return "Indices invalidos"

    if indice_inicio > indice_fin:

        return "Indices invalidos"

    nueva_cadena = ""

    for i in range(indice_inicio, indice_fin + 1):

        nueva_cadena += cadena[i]

    return nueva_cadena


# PRUEBA

texto = "Python"

print(recortar_cadena(texto, 1, 4))

# EJERCICIO 3

def char_at(cadena, posicion):

    if posicion < 0 or posicion >= len(cadena):

        return "Posicion invalida"

    return cadena[posicion]


# PRUEBA

texto = "Hola"

print(char_at(texto, 2))
