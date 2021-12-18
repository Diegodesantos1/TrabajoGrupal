import sys


def Suma(numeros):
    suma = 0
    for i in numeros:
        suma = suma + i
    return suma


if __name__ == "__main__":
    fptr = sys.stdout # Arreglado el error que no dejaba funcionar el código, de stackoverflow
    print("¿De qué tamaño quieres la matriz?")
    ar_count = int(input().strip())
    print("Introduzca los elementos de la matriz a sumar separados por un espacio")
    numeros = list(map(int, input().rstrip().split()))

    resultado = Suma(numeros)

    fptr.write(str(f"El resultado de la suma de los elementos de la matriz es {resultado}") + "\n")

    fptr.close()
