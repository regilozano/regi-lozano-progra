#Generar la secuencia de Fibonacci hasta un número dado de términos.
       
def fib(n):
    if n < 2: 
        return n 
    return fib(n-1) + fib (n-2)

for x in range(20): 
    print(fib(x))
    