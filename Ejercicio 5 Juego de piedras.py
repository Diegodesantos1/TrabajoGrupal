import math
import os
import random
import re
import sys

def JuegoPiedras(n):
    ganador=""
    if(jugada(n)!=0):
        ganador="El jugador 1 es el ganador de el juego de las piedras"
    else:
        ganador ="El jugador 2 es el ganador del juego de las piedras"
    return ganador

def jugada(n):
    buenajugada=0
    modulo=n%7
    if(modulo>=2 and modulo<=3):
        buenajugada=2
    elif(modulo==4):
        buenajugada=3
    elif(modulo>=5 and modulo<=6):
        buenajugada=5
    return


if __name__ == '__main__':
    fptr = (sys.stdout)  # Arreglado el error que no dejaba funcionar el código, de stackoverflow
    t = int(input().strip())
    for t_itr in range(t):
    n = int(input().strip())
    result = JuegoPiedras(n)
    fptr.write(result + '\n')
    fptr.close()