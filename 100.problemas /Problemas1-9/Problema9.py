#Lista de números pares e impares hasta un límite dado

Lista_1 = list([1,2,3,4,5,6,7,8,9,10])

for num in Lista_1: 
    if (num % 2) == 0: 
        print('{0} es par'.format(num))
    else: 
        print('{0} es impar'.format(num))

