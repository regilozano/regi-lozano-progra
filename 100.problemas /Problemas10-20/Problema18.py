#Problema 18 
#Resolver ecuaciones cuadráticas.

from math import sqrt
import cmath

def resolver_ecuaciones(a,b,c):
    determinante = b**2 - 4*a*c

    if determinante > 0: 
        x_1 = (-b + sqrt(b**2 - 4*a*c)) / (2*a)
        x_2 = (-b - sqrt(b**2 - 4*a*c)) / (2*a)
        return x_1, x_2 
    elif determinante == 0: 
        x_1 = -b / (2*a)
        return (x_1,)
    else: 
        x_1 = (-b + cmath.sqrt(determinante)) / (2*a)
        x_2 = (-b - cmath.sqrt(determinante)) / (2*a)
        return x_1, x_2 
    
a = float(input("Ingrese un valor para el coeficiente a:"))
b = float(input("Ingrese un valor para el coeficiente b:"))
c = float(input("Ingrese un valor para el coeficiente c:"))

print ("Las soluciones son:", resolver_ecuaciones(a,b,c))
