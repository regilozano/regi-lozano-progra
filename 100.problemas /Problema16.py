#Problema 16
#Contar el número de vocales y consonantes en una cadena.

def contar_vocales_consonantes (cadena): 
    vocales = "aeiouAEIOU"
    consonantes = "bcdfghjklmnñpqrstvwxyzBCDFGHJKLMNÑPQRSTVWXYZ"

    num_vocales = sum(1 for letra in cadena if letra in vocales)
    num_consonantes = sum(1 for letra in cadena if letra in consonantes)
    
    return num_vocales, num_consonantes 

cadena = input("Ingrese una cadena:")
vocales, consonantes = contar_vocales_consonantes (cadena)
print(f"Número de vocales: {vocales}")
print(f"Número de consonantes: {consonantes}")

