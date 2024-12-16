import json

# Ruta del archivo de texto
archivo_txt = 'retos/DL_all.txt'
archivo_json = 'retos/dataset.json'

# Lista para almacenar los JSON generados
json_gigante = {}

# Leer el archivo línea por línea
with open(archivo_txt, 'r') as archivo:
    for linea in archivo:
        # Quitar saltos de línea y espacios
        linea = linea.strip()

        # Separar por comas y convertir en lista
        n, p, alfa, beta, orden = linea.split(',')

        if n not in json_gigante:
            json_gigante[n] = []

        json_objeto = {
            "n": int(n),
            "p": int(p),
            "alfa": int(alfa),
            "beta": int(beta),
            "orden": int(orden)
        }

        # Añadir el JSON al gran conjunto
        json_gigante[n].append(json_objeto)

# Escribir el JSON gigante en un archivo
with open(archivo_json, 'w') as archivo_salida:
    json.dump(json_gigante, archivo_salida, indent=4)

print(f"JSON gigante creado en: {archivo_json}")
