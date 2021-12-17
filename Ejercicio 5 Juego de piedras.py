import math
import os
import random
import re
import sys

def gameOfStones(n):





if __name__ == '__main__':
    fptr = (sys.stdout)  # Arreglado el error que no dejaba funcionar el código, de stackoverflow
    t = int(input().strip())
    for t_itr in range(t):
    n = int(input().strip())
    result = gameOfStones(n)
    fptr.write(result + '\n')
    fptr.close()