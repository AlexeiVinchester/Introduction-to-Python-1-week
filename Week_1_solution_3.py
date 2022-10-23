import sys
import math

#найти корни квадратного уравнения
#Ответ привести к целочисленному типу

a = int(sys.argv[1])
b = int(sys.argv[2])
c = int(sys.argv[3])

D = (b * b) - (4 * a * c)
x1 = int((- b - math.sqrt(D)) / (2 * a))
x2 = int((- b + math.sqrt(D)) / (2 * a))
print(x1, x2)
