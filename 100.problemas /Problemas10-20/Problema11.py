#Problema 11
#Verificar si una cadena es un palíndromo.

#Ingresamos la palabra o número que queremos verificar
palíndromo = input("ingresa una palabra:").lower()

if palíndromo == palíndromo [::-1]:
    print ("es un palíndromo")
else: 
    print ("no es un palíndromo")