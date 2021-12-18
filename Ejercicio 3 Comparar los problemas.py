#!/bin/python3
import math
import os
import random
import re
import sys
#
# Complete the 'compareTriplets' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
# 1. INTEGER_ARRAY a
# 2. INTEGER_ARRAY b
#
def compareTriplets(a, b):
    puntosA = 0
    puntosB = 0

    for i in range(0,3): #El tipo range es una lista inmutable de números enteros en sucesión aritmética.
        if a[i]<b[i]:
            puntosB +=1
        elif a[i]>b[i]:
            puntosA +=1
        else:
            puntosA +=1
            puntosB +=1

    puntos_totales = [puntosA,puntosB]
    return puntos_totales


if __name__ == '__main__':
    fptr = sys.stdout
    print("Escribe las notas de a (recuerda que debes introducir 3):")
    a = list(map(int, input().rstrip().split()))

    print("Escribe las notas de b (recuerda que son 3):")
    b = list(map(int, input().rstrip().split()))
    result = compareTriplets(a, b)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')
    fptr.close()