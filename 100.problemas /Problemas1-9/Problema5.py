#Números Primos 

def primo(num): 
    for n in range(2,num): 
        if num%n == 0:
            return False 
    return True 

print(primo(3))
print(primo(21))
