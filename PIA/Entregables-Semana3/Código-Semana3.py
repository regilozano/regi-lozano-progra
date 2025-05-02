import csv
import re
import numpy as np
import statistics as stats

#Lectura y validación de datos del archivo CSV
def leer_y_validar_csv(nombre_archivo):
    """
    Lee un archivo CSV de países, valida los campos y devuelve los datos listos para graficar.
    Cada país será representado como un diccionario con datos limpios y tipos adecuados.
    """
    datos_procesados = [] #Lista para guardar los datos limpios
    errores = 0 

    #Expresiones regulares para validar 
    regex_texto = r"^[\wÁÉÍÓÚÑáéíóúñ\s\(\)\-\,\.'’]+$"
    regex_divisa = r"^[\wÁÉÍÓÚÑáéíóúñ\s\(\)\-\,\.\$€¥£’ʻöđ]*$"  
    regex_poblacion = r'^\d{1,3}(\.\d{3})*$'

    try:
        with open(nombre_archivo, mode='r', encoding='utf-8') as archivo:
            lector = csv.DictReader(archivo)
            encabezados_esperados = {"nombre", "capital", "poblacion", "idioma", "divisa"}

            #Verificación de encabezados
            if set(lector.fieldnames) != encabezados_esperados:
                print(f"Error: Encabezados incorrectos. Se esperaban: {encabezados_esperados}")
                return []

            for i, fila in enumerate(lector, 1):
                nombre = fila['nombre'].strip()
                capital = fila['capital'].strip()
                poblacion_str = fila['poblacion'].strip()
                idioma = fila['idioma'].strip()
                divisa = fila['divisa'].strip()

                #Validaciones
                if not re.match(regex_texto, nombre):
                    print(f"Fila {i}: nombre inválido → '{nombre}'")
                    errores += 1
                if not re.match(regex_texto, capital):
                    print(f"Fila {i}: capital inválida → '{capital}'")
                    errores += 1
                if not re.match(regex_poblacion, poblacion_str):
                    print(f"Fila {i}: población inválida → '{poblacion_str}'")
                    errores += 1
                if not re.match(regex_texto, idioma):
                    print(f"Fila {i}: idioma inválido → '{idioma}'")
                    errores += 1
                if not re.match(regex_divisa, divisa):
                    print(f"Fila {i}: divisa inválida → '{divisa}'")
                    errores += 1
                #Solo agregar si todo está válido hasta el momento 
                if errores == 0:
                    poblacion_num = int(poblacion_str.replace('.', ''))
                    datos_procesados.append({
                        "nombre": nombre,
                        "capital": capital,
                        "poblacion": poblacion_num,
                        "idioma": idioma,
                        "divisa": divisa
                    })

        #Indica que no se devuelvan los datos si es que hay errores 
        if errores > 0:
            print(f"\nSe encontraron {errores} errores. Corrige el archivo antes de continuar.")
            return []
        else:
            return datos_procesados

    except FileNotFoundError:
        print(f"Error: El archivo '{nombre_archivo}' no fue encontrado.")
        return []
    except Exception as e:
        print(f"Ocurrió un error al leer el archivo: {e}")
        return []

#Análisis estadístico a la población
def analizar_datos_poblacion(datos):
    poblaciones = [pais["poblacion"] for pais in datos]
    array = np.array(poblaciones)

    print("\nAnálisis Estadístico de la Población:\n")
    print(f"Cantidad de países: {len(poblaciones)}")

    #Cálculo de medias de tendencia central 
    print(f"Media: {np.mean(array):,.0f}")
    print(f"Mediana: {np.median(array):,.0f}")
    
    #Cálculo de moda 
    try:
        moda = stats.mode(poblaciones)
        print(f"Moda: {moda:,}")
    except:
        print("Moda: No se pudo calcular (posiblemente no hay valores repetidos)")

    #Medidas de dispersión 
    print(f"Desviación estándar: {np.std(array):,.2f}")
    print(f"Varianza: {np.var(array):,.2f}")

    #Valores extremos 
    print(f"Valor mínimo: {np.min(array):,}")
    print(f"Valor máximo: {np.max(array):,}")
    print(f"Rango: {np.max(array) - np.min(array):,}")

    #Cuartiles para ver la distribución
    print(f"Percentil 25: {np.percentile(array, 25):,.0f}")
    print(f"Percentil 75: {np.percentile(array, 75):,.0f}")

    #Detección de outliers con método IQR
    Q1 = np.percentile(array, 25)
    Q3 = np.percentile(array, 75)
    IQR = Q3 - Q1
    outliers = array[(array < Q1 - 1.5 * IQR) | (array > Q3 + 1.5 * IQR)]

    print(f"Outliers detectados (poblaciones extremas): {outliers if len(outliers) > 0 else 'Ninguno'}")


#Ejemplo de ejecución directa 
if __name__ == "__main__":
    archivo = input("Ingresa el nombre del archivo CSV a procesar (ej. europa_paises.csv): ").strip()
    datos = leer_y_validar_csv(archivo)

    if datos:
        print("\nDatos preparados correctamente.")
        print("Ejemplo de los primeros 3 países:\n")
        for pais in datos[:3]:
            print(pais)

        analizar_datos_poblacion(datos)
    else:
        print("\nNo se pudieron procesar los datos.")