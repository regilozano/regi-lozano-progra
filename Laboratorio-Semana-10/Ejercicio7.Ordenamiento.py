#Ejercicio 7: Ordenamiento y Búsqueda

import random

def quicksort(arr):
    """Ordena una lista usando el algoritmo de Quicksort."""
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[len(arr) // 2]
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        return quicksort(left) + middle + quicksort(right)

def busqueda_binaria(arr, objetivo):
    """Realiza una búsqueda binaria en una lista ordenada."""
    izquierda, derecha = 0, len(arr) - 1
    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        if arr[medio] == objetivo:
            return medio  # Retorna el índice del objetivo
        elif arr[medio] < objetivo:
            izquierda = medio + 1
        else:
            derecha = medio - 1
    return -1  # Retorna -1 si no se encuentra el objetivo

def generar_lista_aleatoria(cantidad, rango_inferior, rango_superior):
    """Genera una lista de números aleatorios sin usar librerías."""
    lista = []
    for _ in range(cantidad):
        numero = rango_inferior + int((rango_superior - rango_inferior + 1) * (hash(str(_)) % 100) / 100)
        lista.append(numero)
    return lista

def main():
    # Solicitar al usuario la cantidad de números aleatorios a generar
    cantidad_numeros = int(input("Ingrese la cantidad de números aleatorios a generar: "))
    
    # Generar una lista de números aleatorios
    lista_numeros = generar_lista_aleatoria(cantidad_numeros, 1, 100)

    print("Lista original:")
    print(lista_numeros)

    # Ordenar la lista usando Quicksort
    lista_ordenada = quicksort(lista_numeros)

    print("Lista ordenada:")
    print(lista_ordenada)

    # Permitir al usuario buscar un número
    numero_buscar = int(input("Ingrese un número a buscar en la lista: "))
    resultado = busqueda_binaria(lista_ordenada, numero_buscar)

    if resultado != -1:
        print(f"Número {numero_buscar} encontrado en el índice {resultado}.")
    else:
        print(f"Número {numero_buscar} no encontrado en la lista.")

if __name__ == "__main__":
    main()