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
