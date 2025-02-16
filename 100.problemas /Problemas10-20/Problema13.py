#Problema 13
#Convertir una temperatura entre distintas escalas.

def conversor (): 
    temp = input("Ingrese la temperatura con la respectiva unidad, sin el signo de grado")
    unidad = temp[-1].upper()
    grados = float(temp[:-1])

    if unidad == "C": 
        temp_conv = (grados * (9/5) +32)
        print (f"{grados}°{unidad} es equivalente a {temp_conv}°F")

    else:
        temp_conv = ((grados - 32) * (5/9))
        print(f"{grados}°{unidad} es equivalente a {temp_conv}°C")

conversor ()