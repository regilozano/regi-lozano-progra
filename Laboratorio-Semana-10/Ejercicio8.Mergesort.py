#Ejercicio 8: Implementación de Mergesort

def mergesort(arr):
    """Ordena una lista usando el algoritmo de Mergesort."""
    if len(arr) <= 1:
        return arr

    # Dividir la lista en dos mitades
    medio = len(arr) // 2
    izquierda = mergesort(arr[:medio])
    derecha = mergesort(arr[medio:])

    # Mezclar las dos mitades ordenadas
    return mezclar(izquierda, derecha)

def mezclar(izquierda, derecha):
    """Mezcla dos listas ordenadas en una sola lista ordenada."""
    resultado = []
    i = j = 0

    # Comparar elementos de ambas listas y añadir el menor a la lista resultado
    while i < len(izquierda) and j < len(derecha):
        if izquierda[i] < derecha[j]:
            resultado.append(izquierda[i])
            i += 1
        else:
            resultado.append(derecha[j])
            j += 1

    # Añadir los elementos restantes de la lista izquierda
    while i < len(izquierda):
        resultado.append(izquierda[i])
        i += 1

    # Añadir los elementos restantes de la lista derecha
    while j < len(derecha):
        resultado.append(derecha[j])
        j += 1

    return resultado

def main():
    # Solicitar al usuario que ingrese una lista de números
    numeros = input("Ingrese una lista de números separados por espacios: ")
    lista_numeros = list(map(int, numeros.split()))

    print("Lista original:")
    print(lista_numeros)

    # Ordenar la lista usando Mergesort
    lista_ordenada = mergesort(lista_numeros)

    print("Lista ordenada:")
    print(lista_ordenada)

if __name__ == "__main__":
    main()