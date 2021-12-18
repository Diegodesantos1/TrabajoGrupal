import math
import os
import random
import re
import sys


def compareTriplets(a, b):
    puntosA = 0
    puntosB = 0

    for i in range(0, 3):  # El tipo range es una lista inmutable de números enteros en sucesión aritmética.
        if a[i] < b[i]:
            puntosB += 1
        elif a[i] > b[i]:
            puntosA += 1
        else:
            puntosA += 1
            puntosB += 1
    puntos_totales = [puntosA, puntosB]
    print("Los puntos de Lucía y Carlos son los siguientes:", puntos_totales)
    return puntos_totales


if __name__ == "__main__":
    fptr = sys.stdout
    print("Escribe las notas de Lucía (recuerda que debes introducir 3):")
    a = list(map(int, input().rstrip().split()))

    print("Escribe las notas de Carlos (recuerda que son 3):")
    b = list(map(int, input().rstrip().split()))
    result = compareTriplets(a, b)
    fptr.close()
