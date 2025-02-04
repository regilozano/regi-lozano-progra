#Variables
num1 = input('ingres un número')
num2 = input('ingresa un número')

#Suma
sum= float(num1) + float(num2) 

#Resultado 
print('La suma es:', sum)

#Resta 
res= float(num1) - float(num2)

#Resultado 
print('La resta es:', res)

#Multiplicación
mult= float(num1) * float(num2)

#Resultado 
print('La multiplicación es:', mult)

#División
div= float(num1) / float(num2)
if(num2 == 0):
        print('indefinido')
else: 
        print('La divisón es:', div)