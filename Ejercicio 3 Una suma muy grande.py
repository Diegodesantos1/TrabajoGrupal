
import math
import os
import random
import re
import sys

def aVeryBigSum(ar):
    suma = 0
    for i in ar:
        suma += i
    return suma



if __name__ == '__main__':
    fptr = sys.stdout #código perteneciente a satckoverflow
    print('Escribe un número:')
    ar_count = int(input().strip())
    print('Escriba una sucesión de números separados por espacios:')
    ar = list(map(int, input().rstrip().split()))
    result = aVeryBigSum(ar)
    fptr.write(str(result) + '\n')
    fptr.close()