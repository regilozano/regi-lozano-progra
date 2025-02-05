#Problema 6

#Ingresar el capital, tasa y tiempo 

capital = float(input("Ingrese el capital inicial"))
tasa = float(input('Ingrese el procentaje de tasa en decimales'))
tiempo = float(input('Ingrese el timepo en años'))

def intereses_compuesto (capital, tasa, tiempo):
    return capital*(1 + tasa)**tiempo

print ('El capital final es:', intereses_compuesto)