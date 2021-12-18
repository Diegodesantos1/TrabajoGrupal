import math
import os
import random
import re
import sys

def JuegoPiedras(n):
    ganador=""
    if(jugadaperfecta(n)!=0):
        ganador="P1 is the winner"
    else:
        ganador ="P2 is the winner"
    return ganador

def jugadaperfecta(n):
    buenajugada=0
    modulo=n%7
    if(modulo>=2 and modulo<=3):
        buenajugada=2
    elif(modulo==4):
        buenajugada=3
    elif(modulo>=5 and modulo<=6):
        buenajugada=5
    return buenajugada

def Ejecutarjuego(n):
    intentos=0
    ganador=""
    while(ganador!="P1 is the winner" and ganador!="P2 is the winner"):
        jugada=jugadaperfecta(n)
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
    fptr = sys.stdout
    print("Cuántas partidas quieres jugar?")
    t = int(input().strip())

    for t_itr in range(t):
        print("¿Cuántas piedras tienes?")
        n = int(input().strip())
        result = JuegoPiedras(n)
        Ejecutarjuego(n)
        fptr.write(result + '\n')

    fptr.close()