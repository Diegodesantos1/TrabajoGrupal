import math
import os
import random
import re
import sys
def escalera(tamaño):
    for i in range(0,tamaño): #Bucle para crear las líneas
        linea=" "
    for j in range(0,tamaño-1-i):
            linea=linea + " "



if __name__ == '__main__':
    print("Introduzca el tamaño de la escalera")
    tamaño = int(input().strip())

    escalera(tamaño)