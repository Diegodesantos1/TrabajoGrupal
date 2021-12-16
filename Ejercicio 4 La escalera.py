import math
import os
import random
import re
import sys
def escalera(tamaño):
    for i in range(0,tamaño): #Bucle para crear las líneas
        linea=""
    for j in range(0,tamaño-1-i): #Bucle para dejar espacios
        linea=linea + " "
    for k in range(0,i+1):
        linea = linea + "# " #Bucle para printear la escalera
    print(linea)



if __name__ == '__main__':
    print("Introduzca el tamaño de la escalera")
    tamaño = int(input().strip())

    escalera(tamaño)