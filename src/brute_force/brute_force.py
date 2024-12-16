import json
import os
import time
from collections import Counter

import matplotlib.pyplot as plt

from src.const import MAGIA, DATASET_PATH
from src.logger import configurar_logger

ruta_actual = os.path.abspath(__file__)
directorio_actual = os.path.dirname(ruta_actual)

logger = configurar_logger(directorio_actual)

def test():
    logger.info(f"\n{MAGIA} FUERZA BRUTA {MAGIA}")
    logger.info(f"Data: n;alfa;beta;p;x;duracion")

    with open(DATASET_PATH, 'r') as j:
        d = json.load(j)

    for talla, objetos in d.items():
        for obj in objetos:
            n = obj["n"]
            p = obj["p"]
            alfa = obj["alfa"]
            beta = obj["beta"]
            orden = obj["orden"]
            logaritmo_discreto_fuerza_bruta(n, alfa, beta, p)


# Problema del logaritmo discreto: Encontrar x tal que g^x ≡ y (mod p)
def logaritmo_discreto_fuerza_bruta(n ,alfa, beta, p):
    """
    Encontrar x tal que alfa^x ≡ beta (mod p)

    :param alfa: base
    :param beta: resultado conocido
    :param p: número primo
    :return: exponente que buscamos
    """

    inicio = time.time()
    for x in range(p):  # Probar todos los valores posibles de x (de 0 a p-1)
        if pow(alfa, x, p) == beta:  # Verificar si g^x mod p == y
            fin = time.time()  # Registrar el tiempo final
            duracion = fin - inicio

            logger.info(f"{n};{alfa};{beta};{p};{x};{duracion:.6f}")
            return x

    fin = time.time()
    duracion = fin - inicio
    x = None
    logger.info(f"{n};{alfa};{beta};{p};{x};{duracion:.6f}")
    return None  # Si no se encuentra una solución (teóricamente improbable si g es una base válida)


def demostrar_modulo_uniforme(primo, rango_a):
    # Calcular los restos
    restos = [a % primo for a in range(rango_a)]

    # Contar la frecuencia de cada resto
    frecuencia_restos = Counter(restos)

    # Mostrar resultados
    print(f"Primo: {primo}")
    print(f"Frecuencia de restos (módulo {primo}): {dict(frecuencia_restos)}")

    # Verificar que los restos son uniformes
    esperados = rango_a // primo
    print(f"Frecuencia esperada (si es uniforme): {esperados}")
