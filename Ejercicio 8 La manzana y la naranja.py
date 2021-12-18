import math
import os
import random
import re
import sys

def contarmanzanasnaranjas(s, t, a, b, apples, oranges):
    manzanasdentro=0
    naranjasdentro=0
    for manzana in apples:
        if(a+manzana>=s and a+manzana<=t):
            manzanasdentro+=1
    for naranja in oranges:
        if(b+naranja>=s and b+naranja<=t):
            naranjasdentro+=1
    print(f"Han caido {manzanasdentro} manzanas dentro")
    print(f"Han caido {naranjasdentro} naranjas dentro")



if __name__ == '__main__':
    print("Establece el punto de inicio y final de la ubicación de la casa de Sam separado por un espacio")
    first_multiple_input = input().rstrip().split()
    s = int(first_multiple_input[0])
    t = int(first_multiple_input[1])
    print("Establece la ubicación del manzano y naranjo separados por un espacio")
    second_multiple_input = input().rstrip().split()
    a = int(second_multiple_input[0])
    b = int(second_multiple_input[1])
    print("Establece el número de manzanas y naranjas separado por un espacio y las distancias a las que cada manzana y naranja cae del árbol separado por un espacio")
    third_multiple_input = input().rstrip().split()
    m = int(third_multiple_input[0])
    n = int(third_multiple_input[1])
    apples = list(map(int, input().rstrip().split()))
    oranges = list(map(int, input().rstrip().split()))
    contarmanzanasnaranjas(s, t, a, b, apples, oranges)