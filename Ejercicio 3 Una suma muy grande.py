#!/bin/python3
import math
import os
import random
import re
import sys
#
# Complete the 'aVeryBigSum' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts LONG_INTEGER_ARRAY ar as parameter.
#
def aVeryBigSum(ar):
# Write your code here


if __name__ == '__main__':
    fptr = sys.stdout #código perteneciente a satckoverflow
    print('Escribe un número:')
    ar_count = int(input().strip())
    print('Escriba una sucesión de números separados por espacios:')
    ar = list(map(int, input().rstrip().split()))
    result = aVeryBigSum(ar)
    fptr.write(str(result) + '\n')
    fptr.close()