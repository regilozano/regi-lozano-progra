#Problema 12
#Encontrar el mayor entre tres números dados.

#Ingresamos los números a verificar
a = float(input("Ingresa un número"))
b = float(input("Ingresa un número"))
c = float(input("Ingresa un número"))

if a != b and a !=c and b != c: 
    if a > b:
        if a >c:
            print ("El número mayor es:", a ) 
        else:
            print("El número mayor es: ",c)
    else: 
        if b > c: 
            print("El número mayro es:" ,b)
        else: 
            print("El número mayor es:", c)
else: 
    print ("Ingrsea 3 números diferentes")