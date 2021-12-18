<h1 align="center">Trabajo Grupal</h1>


<h2>Repositorio</h2>

Este es el link del [Repositorio](https://github.com/Diegodesantos1/TrabajoGrupal)

***

<h2>Participantes</h2>

***

1. [Alba](https://github.com/albabernal03)
2. [Diego](https://github.com/Diegodesantos1)

***
## Índice
1. [Ejercicio1](#id1)
3. [Ejercicio2](#id2)
3. [Ejercicio3](#id3)
4. [Ejercicio4](#id4)
5. [Ejercicio5](#id5)
6. [Ejercicio6](#id6)
7. [Ejercicio7](#id7)
8. [Ejercicio8](#id8)
***
## Ejercicio 1: Suma simple de una matriz<a name="id1"></a>

*En el primer ejercicio teníamos que realizar una suma de los elementos de una matriz, según el tamaño introducido y sus respectivos elementos*

Aquí su [Milestone](https://github.com/Diegodesantos1/TrabajoGrupal/milestone/1?closed=1)

**El digrama de flujo es el siguiente:**

![tarea 1](https://user-images.githubusercontent.com/91721875/146649386-c84d6143-f95e-40f1-ada0-2c1d356fc4b2.jpg)

**El código empleado para resolverlo es el siguiente:**

```python
import sys


def Suma(numeros):
    suma = 0
    for i in numeros:
        suma = suma + i
    return suma


if __name__ == "__main__":
    fptr = sys.stdout  # Arreglado el error que no dejaba funcionar el código, de stackoverflow
    print("¿De qué tamaño quieres la matriz?")
    ar_count = int(input().strip())
    print("Introduzca los elementos de la matriz a sumar separados por un espacio")
    numeros = list(map(int, input().rstrip().split()))

    resultado = Suma(numeros)

    fptr.write(str(f"El resultado de la suma de los elementos de la matriz es {resultado}") + "\n")

    fptr.close()
```
***

## Ejercicio 2: Compara los problemas<a name="id2"></a>

*En el segundo ejercicio teníamos que realizar un programa al cual das un valor a la nota final de tanto Lucía como carlos, asignandoles unos criterios, y después compararlas*

Aquí su [Milestone](https://github.com/Diegodesantos1/TrabajoGrupal/milestone/2?closed=1)

**El diagrama de flujo es el siguiente:**
![EJERCIO 3 ](https://user-images.githubusercontent.com/91721875/146654195-e1018a42-aee2-4ba7-b248-af053d79c4f4.jpg)

**El código empleado para resolverlo es el siguiente:**

```python
import math
import os
import random
import re
import sys


def compareTriplets(a, b):
    puntosA = 0
    puntosB = 0

    for i in range(0, 3):  # El tipo range es una lista inmutable de números enteros en sucesión aritmética.
        if a[i] < b[i]:
            puntosB += 1
        elif a[i] > b[i]:
            puntosA += 1
        else:
            puntosA += 1
            puntosB += 1
    puntos_totales = [puntosA, puntosB]
    print("Los puntos de Lucía y Carlos son los siguientes:", puntos_totales)
    return puntos_totales


if __name__ == "__main__":
    fptr = sys.stdout
    print("Escribe las notas de Lucía (recuerda que debes introducir 3):")
    a = list(map(int, input().rstrip().split()))

    print("Escribe las notas de Carlos (recuerda que son 3):")
    b = list(map(int, input().rstrip().split()))
    result = compareTriplets(a, b)
    fptr.close()
```
***


## Ejercicio 3: Una suma muy grande<a name="id3"></a>

*En el tercer ejercicio teníamos que realizar un programa que dada una sucesión de números, sea capaz de hallar el valor total de la suma*

Aquí su [Milestone](https://github.com/Diegodesantos1/TrabajoGrupal/milestone/3?closed=1)

**El diagrama de flujo es el siguiente:**

![EJERCIO 3 0](https://user-images.githubusercontent.com/91721875/146655081-40f6de69-c68d-43ae-a45b-e5ab36774c35.jpg)

**El código empleado para resolverlo es el siguiente:**

```python
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
    selección = print(ar_count)

    print('Escriba una sucesión de números separados por espacios:')
    ar = list(map(int, input().rstrip().split()))
    seleccion_2 = print(ar)

    
    result = print('La resultado de la suma es igual a:', aVeryBigSum(ar))
    fptr.write(str(result) + '\n')
    
    fptr.close()
```
***


## Ejercicio 4: La escalera<a name="id4"></a>

*En el cuarto ejercicio teníamos que realizar un programa capaz de printear una escalera creada con lineas y # en función de la dimensión seleccionada*

Aquí su [Milestone](https://github.com/Diegodesantos1/TrabajoGrupal/milestone/4?closed=1)

**El diagrama de flujo es el siguiente:**
![tarea 2](https://user-images.githubusercontent.com/91721875/146649604-bad62170-e37a-4039-9ecd-dd1618f34327.jpg)


**El código empleado para resolverlo es el siguiente:**

```python
def escalera(tamaño):
    for i in range(0, tamaño):  # Bucle para crear las líneas
        linea = ""
        for j in range(
            0, tamaño - 1 - i
        ):  # Bucle para dejar los espacios en las líneas
            linea = linea + " "
        for k in range(0, i + 1):
            linea = linea + "# "  # Bucle para printear los # de la escalera
        print(linea)


if __name__ == "__main__":
    print("Introduzca el tamaño de la escalera")
    tamaño = int(input().strip())

    escalera(tamaño)
```
***

## Ejercicio 5: Juego de piedras<a name="id5"></a>

*En el quinto ejercicio teníamos que realizar un programa capaz de ejecutar un juego de unas piedras en las cuales los 2 jugadores van quitando un númrro de piedras concreto que tiene que ser 2, 3 o 5 y el jugador que se quede sin movimientos pierde, siempre empieza el P1 y se van alternando*

Aquí su [Milestone](https://github.com/Diegodesantos1/TrabajoGrupal/milestone/5?closed=1)

**El diagrama de flujo es el siguiente:**

![JUEGO 5](https://user-images.githubusercontent.com/91721875/146653078-35d0602c-65ee-4fdf-89d9-102753a33967.jpg)

**El código empleado para resolverlo es el siguiente:**

```python
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
```
***

## Ejercicio 6: Laberinto<a name="id6"></a>



**El código empleado para resolverlo es el siguiente:**

```python
from io import DEFAULT_BUFFER_SIZE
import math
import os
import random
import re
import sys

class Coordenadas:
    def __init__(self, x, y):
        self.x=x
        self.y=y
    def comparate(self, x, y):
        if (self.x==x and self.y==y):
            return True
        else:
            return False

class Tunel:
    def __init__(self, x1, y1, x2, y2):
        self.extremo1 = Coordenadas(x1,y1)
        self.extremo2 = Coordenadas(x2,y2)

def buscaTunel (Casillax, Casillay, tuneles):
    coordenadas = Coordenadas (Casillax, Casillay)
    for t in tuneles:
        if(t.extremo1.comporate(Casillax,Casillay)):
            coordenadas.x=t.extremo2.x
            coordenadas.y=t.extremo2.y
            break
        elif(t.extremo2.comporate(Casillax,Casillay)):
            coordenadas.x=t.extremo1.x
            coordenadas.y=t.extremo1.y
            break
        return coordenadas

def exploracion(Casillax, Casillay, laberinto, n, m, tuneles):
    num = 0
    den = 0
    probabilidad= 0.0
    if(Casillax>0 and laberinto[Casillax-1][Casillay]!="#"):
        den +=1
        if(laberinto[Casillax-1][Casillay]=="%"):
            num+=1
    if(Casillax<n-1 and laberinto[Casillax+1][Casillay]!="#"):
        den +=1
        if(laberinto[Casillax+1][Casillay]=="%"):
            num+=1
    if(Casillay<m-1 and laberinto[Casillax][Casillay+1]!="#"):
        den +=1
        if(laberinto[Casillax][Casillay+1]=="%"):
            num+=1
    if(Casillay>0 and laberinto[Casillax][Casillay-1]!="#"):
        den +=1
        if(laberinto[Casillax][Casillay-1]=="%"):
            num+=1
    if(den==0):
        return probabilidad
    probabilidad=num/den
    if(Casillax>0 and laberinto[Casillax-1][Casillay]=="$"):
        laberintocopia=laberinto
        coordenadas= buscaTunel(Casillax-1,Casillay,tuneles)
        laberintocopia[Casillax][Casillay]="#"
        probabilidad+=exploracion(coordenadas.x,coordenadas.y, laberintocopia, n , m, tuneles)/den
    if(Casillax<n-1 and laberinto[Casillax+1][Casillay]=="$"):
        laberintocopia=laberinto
        coordenadas= buscaTunel(Casillax+1,Casillay,tuneles)
        laberintocopia[Casillax][Casillay]="#"
        probabilidad+=exploracion(coordenadas.x,coordenadas.y, laberintocopia, n , m, tuneles)/den
    if(Casillay<m-1 and laberinto[Casillax][Casillay+1]=="$"):
        laberintocopia=laberinto
        coordenadas= buscaTunel(Casillax,Casillay+1,tuneles)
        laberintocopia[Casillax][Casillay]="#"
        probabilidad+=exploracion(coordenadas.x,coordenadas.y, laberintocopia, n , m, tuneles)/den
    if(Casillay>0 and laberinto[Casillax][Casillay-1]=="$"):
        laberintocopia=laberinto
        coordenadas= buscaTunel(Casillax,Casillay-1,tuneles)
        laberintocopia[Casillax][Casillay]="#"
        probabilidad+=(exploracion(coordenadas.x,coordenadas.y, laberintocopia, n , m, tuneles)/den)
    return probabilidad

    
if __name__ == '__main__':
    first_multiple_input = input("Introduzca las coordenadas del laberinto:").rstrip().split()

    n = int(first_multiple_input[0])
    m = int(first_multiple_input[1])
    k = int(first_multiple_input[2])
    laberinto = []

    
    for n_itr in range(n):
        row = input("Fila" + str(n_itr) + "del laberinto:(#--> muro, %--> salida, *-->bomba, $--> vacía, o--> tunel")
        laberinto.append(list(row))
    tuneles = []

for k_itr in range(k):
    second_multiple_input = input("Coordenadas(i1 j1 i2 j2) del túnel"+ str(k_itr)).rstrip().split()

    i1 = int(second_multiple_input[0])
    j1 = int(second_multiple_input[1])
    i2 = int(second_multiple_input[2])
    j2 = int(second_multiple_input[3])

third_multiple_input = input("Coordenadas(i1 j1 i2 j2) de la rana").rstrip().split()
pos1= int(third_multiple_input[0])
pos2 = int(third_multiple_input[0])

probabilidad = exploracion(pos1,pos2,laberinto,n,m,tuneles)
print(probabilidad)
```

***

## Ejercicio 7: Estudiantes de calificación<a name="id7"></a>

*En el séptimo ejercicio teníamos que realizar un programa capaz de redondear notas asignadas a los estudiantes según los criterios establecidos*

Aquí su [Milestone](https://github.com/Diegodesantos1/TrabajoGrupal/milestone/7?closed=1)

**El diagrama de flujo es el siguiente:**
![EJERCICIO 7](https://user-images.githubusercontent.com/91721875/146656045-950c5403-6987-4627-b76d-00380b90331d.jpg)

**El código empleado para resolverlo es el siguiente:**

```python
import math
import os
import random
import re
import sys


def gradingStudents(grades):
    list=[]
    for grade in (grades):
        list.append(notas_finales(grade)) #El punto append sirve para añadir 
    return list

#Según esta tarea si la calificación obtenida es menor que 40 no se redondeará,
#puesto que menor de 40 ya es supenso y aunque se redondee será suspenso.

#Por otro lado, si hay una diferencia menor que 3 entre el siguiente número de la nota  obtenida y la nota obtenida se resondeará
#hasta el siguiente múltiplo de 5

def notas_finales(grades):
    nota_redondeada=0
    if(grades<40):
        nota_redondeada=grades
    else:
        cociente=int(grades/5 + 1)
        multiplo=cociente*5
        if(multiplo-grades<3):
            nota_redondeada=multiplo
        else:
            nota_redondeada=grades
    return nota_redondeada

if __name__ == '__main__':
    fptr = sys.stdout
    print("Número de estudiantes")
    grades_count = int(input().strip())

    grades = []

    for _ in range(grades_count):
        print("Nota de cada estudiante")
        grades_item = int(input().strip())
        grades.append(grades_item)

    result = gradingStudents(grades)
    fptr.write(f"Las notas finales son:{result}")
    fptr.write('\n')

    fptr.close()



```
***

## Ejercicio 8: La manzana y naranja<a name="id8"></a>

*En el octavo y último ejercicio teníamos que realizar un programa capaz de calcular el número de manzanas y naranjas que caen dentro de la casa de Sam, esta está denotada por dos números enteros, además hay que establecer la ubicación del manzano y del naranjo, el número de manzanas y naranjas que caían y su posición respecto del árbol de origen*

Aquí su [Milestone](https://github.com/Diegodesantos1/TrabajoGrupal/milestone/8?closed=1)

**El código empleado para resolverlo es el siguiente:**

```python
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
 ```
