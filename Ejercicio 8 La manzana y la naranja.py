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


if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()
    s = int(first_multiple_input[0])
    t = int(first_multiple_input[1])
    second_multiple_input = input().rstrip().split()
    a = int(second_multiple_input[0])
    b = int(second_multiple_input[1])
    third_multiple_input = input().rstrip().split()
    m = int(third_multiple_input[0])
    n = int(third_multiple_input[1])
    apples = list(map(int, input().rstrip().split()))
    oranges = list(map(int, input().rstrip().split()))
    contarmanzanasnaranjas(s, t, a, b, apples, oranges)