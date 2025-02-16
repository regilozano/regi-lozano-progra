#Calcular el  área y la circunferencia de un círculo.

import math 

radio = float(input('Ingrese el radio del círculo'))

área= math.pi * (radio ** 2)
perímetro= 2 * math.pi * radio 

print ('El área del círculo es', área)
print ('Él perímetro del círculo es', perímetro)

