#Ejercicio 4: Calculadora de Estadísticas

def calcular_estadisticas(*args):
    if not args:
        return None, None, None  # Retorna None si no hay argumentos

    # Calcular promedio
    promedio = sum(args) / len(args)

    # Calcular mediana
    lista_ordenada = sorted(args)
    n = len(lista_ordenada)
    if n % 2 == 0:
        mediana = (lista_ordenada[n // 2 - 1] + lista_ordenada[n // 2]) / 2
    else:
        mediana = lista_ordenada[n // 2]

    # Calcular desviación estándar
    varianza = sum((x - promedio) ** 2 for x in args) / len(args)
    desviacion_estandar = varianza ** 0.5

    return promedio, mediana, desviacion_estandar

def main():
    # Solicitar al usuario una lista de números
    numeros = input("Ingrese una lista de números separados por espacios: ")
    lista_numeros = list(map(float, numeros.split()))

    # Calcular estadísticas
    promedio, mediana, desviacion_estandar = calcular_estadisticas(*lista_numeros)

    # Mostrar resultados
    print(f"Promedio: {promedio}")
    print(f"Mediana: {mediana}")
    print(f"Desviación estándar: {desviacion_estandar}")

if __name__ == "__main__":
    main()

    