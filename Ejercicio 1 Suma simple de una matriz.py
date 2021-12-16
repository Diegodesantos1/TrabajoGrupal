import math
import os
import random
import re
import sys
def Suma(numeros):
    suma=0
    for i in numeros:
        suma= suma+i
    return suma

if __name__ == '__main__':
    fptr = sys.stdout #Arreglado el error que no dejaba funcionar el código, de stackoverflow
    print("¿De qué tamaño quieres la matriz?")
    ar_count = int(input().strip())
    print("Introduzca los números a sumar separados por un espacio")
    numeros = list(map(int, input().rstrip().split()))

    resultado = Suma(numeros)

    fptr.write(str(resultado) + '\n')

    fptr.close()
