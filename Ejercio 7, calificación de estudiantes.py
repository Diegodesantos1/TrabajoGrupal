import math
import os
import random
import re
import sys

#
# Complete the 'gradingStudents' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY grades as parameter.
#

def gradingStudents(grades):



#Según esta tarea si la calificación obtenida es menor que 40 no se redondeará,
#puesto que menor de 40 ya es supenso y aunque se redondee será suspenso.

#Por otro lado, si hay una diferencia menor que 3 entre el siguiente número de la nota  obtenida y la nota obtenida se resondeará
#hasta el siguiente múltiplo de 5

def notas_finales(grades): 
    nota_redondeada = 0
    if grades < 40:
        nota_redondeada = grades
    else:
    



if __name__ == '__main__':
    fptr = sys.stdoubt

    grades_count = int(input().strip()) 

    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    result = gradingStudents(grades)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()