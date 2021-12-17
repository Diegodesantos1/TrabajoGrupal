import math
import os
import random
import re
import sys

def JuegoPiedras(n):
    ganador=""
    if(jugadabuena(n)!=0):
        ganador="El jugador 1 es el ganador del juego de las piedras"
    else:
        ganador ="El jugador 2 es el ganador del juego de las piedras"
    return ganador

def jugadabuena(n):
    buenajugada=0
    modulo=n%7
    if(modulo>=2 and modulo<=3):
        buenajugada=2
    elif(modulo==4):
        buenajugada=3
    elif(modulo>=5 and modulo<=6):
        buenajugada=5
    return buenajugada


def ejecutarjuego(n):
    intentos=0
    ganador=""
    while(ganador!="El jugador 1 es el ganador del juego de las piedras" and ganador!="El jugador 2 es el ganador del juego de las piedras"):
        jugada=jugadabuena(n)
        if(jugada==0):
            if(n>5):
                jugada=5
            elif(n>3):
                jugada=3
            else:
                jugada=2
        print("Juega P"+str((intentos%2)+1) +" quitando "+ str(jugada)+" piedras")
        n=n-jugada
        if(n==1 or n==0):
            ganador=("P"+str((intentos%2)+1)+" is the winner")
        intentos+=1
    print(ganador)


if __name__ == '__main__':
    fptr = (sys.stdout)  # Arreglado el error que no dejaba funcionar el código, de stackoverflow
    print("Cuántas partidas quieres jugar?")
    t = int(input().strip())
    
    for t_itr in range(t):
        print("¿Cuántas piedras tienes?")
        n = int(input().strip())
        result = JuegoPiedras(n)
        ejecutarjuego(n)
        fptr.write(result + '\n')
    fptr.close()