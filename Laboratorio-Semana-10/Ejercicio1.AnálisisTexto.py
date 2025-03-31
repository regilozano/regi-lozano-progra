#Ejercicio 1: Análisis de Texto con Diccionarios y Conjuntos

def analizar_texto(texto):
    # Convertir el texto a minúsculas y dividirlo en palabras
    palabras = texto.lower().split()
    
    # Número total de palabras
    total_palabras = len(palabras)
    
    # Conjunto para palabras únicas
    palabras_unicas = set(palabras)
    cantidad_palabras_unicas = len(palabras_unicas)
    
    # Diccionario para la frecuencia de cada palabra
    frecuencia_palabras = {}
    for palabra in palabras:
        if palabra in frecuencia_palabras:
            frecuencia_palabras[palabra] += 1
        else:
            frecuencia_palabras[palabra] = 1
    
    # Encontrar la palabra más frecuente
    palabra_mas_frecuente = max(frecuencia_palabras, key=frecuencia_palabras.get)
    frecuencia_palabra_mas_frecuente = frecuencia_palabras[palabra_mas_frecuente]
    
    # Resumen de resultados
    print("Resumen del análisis del texto:")
    print(f"Número total de palabras: {total_palabras}")
    print(f"Cantidad de palabras únicas: {cantidad_palabras_unicas}")
    print("Frecuencia de cada palabra:")
    for palabra, frecuencia in frecuencia_palabras.items():
        print(f"{palabra}: {frecuencia}")
    print(f"La palabra más frecuente es '{palabra_mas_frecuente}' con {frecuencia_palabra_mas_frecuente} apariciones.")

# Solicitar al usuario que ingrese un texto
texto_usuario = input("Por favor, ingresa un texto: ")
analizar_texto(texto_usuario)