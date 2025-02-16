#Problema 15 
#Determinar si un año es bisiesto.

def bisiesto(): 

    num = int(input("Ingrese el año que quiere verificar"))

    if num % 4 !=0: 
        print("no es bisiesto")
    elif num % 4 == 0 and num % 100 !=0: 
        print ("es bisiesto")
    elif num % 4 == 0 and num % 100 == 0 and num % 400 !=0: 
        print ("no es bisiesto")
    elif num % 4 == 0 and num % 100 == 0 and num % 400 == 0: 
        print ("es bisiesto")

bisiesto ()