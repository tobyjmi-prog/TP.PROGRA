
# 1) SUMAR NUMEROS NATURALES

def sumar_naturales(numero: int) -> int:

    if numero == 1:
        return 1

    return numero + sumar_naturales(numero - 1)


# 2) CALCULAR POTENCIA


def calcular_potencia(base: int, exponente: int) -> int:

    if exponente == 0:
        return 1

    return base * calcular_potencia(base, exponente - 1)


# 3) SUMAR DIGITOS


def sumar_digitos(numero: int) -> int:

    if numero < 10:
        return numero

    return (numero % 10) + sumar_digitos(numero // 10)


# 4) FIBONACCI

def calcular_fibonacci(numero: int) -> int:

    if numero == 0:
        return 0

    if numero == 1:
        return 1

    return calcular_fibonacci(numero - 1) + calcular_fibonacci(numero - 2)



# PRUEBAS


print("Suma naturales:", sumar_naturales(5))
print("Potencia:", calcular_potencia(2, 4))
print("Suma digitos:", sumar_digitos(1234))
print("Fibonacci:", calcular_fibonacci(9))
