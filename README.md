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
## Ejercicio 1<a name="id1"></a>


*En el primer ejercicio teníamos que realizar una suma de los elementos de una matriz, según el tamaño introducido y sus respectivos elementos*

Aquí su [Milestone](https://github.com/Diegodesantos1/TrabajoGrupal/milestone/1?closed=1)

**El código empleado para resolverlo es el siguiente:**

```python
import sys


def Suma(numeros):
    suma = 0
    for i in numeros:
        suma = suma + i
    return suma


if __name__ == "__main__":
    fptr = (
        sys.stdout
    )  # Arreglado el error que no dejaba funcionar el código, de stackoverflow
    print("¿De qué tamaño quieres la matriz?")
    ar_count = int(input().strip())
    print("Introduzca los elementos de la matriz a sumar separados por un espacio")
    numeros = list(map(int, input().rstrip().split()))

    resultado = Suma(numeros)

    fptr.write(str(f"El resultado de la suma de los elementos de la matriz es {resultado}") + "\n")

    fptr.close()
```
***

## Ejercicio 2<a name="id2"></a>


***


## Ejercicio 3<a name="id3"></a>


***

## Ejercicio 4: La escalera<a name="id4"></a>

*En el cuarto ejercicio teníamos que realizar un programa capaz de printear una escalera creada con lineas y # en función de la dimensión seleccionada*

Aquí su [Milestone](https://github.com/Diegodesantos1/TrabajoGrupal/milestone/4?closed=1)

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

## Ejercicio 4<a name="id4"></a>

***

## Ejercicio 5<a name="id5"></a>

***

## Ejercicio 6<a name="id6"></a>

***

## Ejercicio 7<a name="id7"></a>

***

## Ejercicio 8<a name="id8"></a>

