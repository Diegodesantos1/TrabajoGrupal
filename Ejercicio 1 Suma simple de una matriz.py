import math
import os
import random
import re
import sys
def SumaSimple(numeros):
    suma = 0 #Comienza en 0 la suma
    for i in ar:
        suma = suma + i
    return suma






if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    print("¿De qué tamaño quieres la matriz?")
    tamaño_matriz = int(input().strip())
    print("Introduzca los números a sumar separados por un espacio")
    numeros= list(map(int, input().rstrip().split()))
    
    result = SumaSimple(ar)
    fptr.write(str(result) + '\n')
    
    fptr.close()