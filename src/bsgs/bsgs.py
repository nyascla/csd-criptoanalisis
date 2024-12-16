import json
import math
import os
import time

from src.const import MAGIA, DATASET_PATH
from src.logger import configurar_logger

ruta_actual = os.path.abspath(__file__)
directorio_actual = os.path.dirname(ruta_actual)

logger = configurar_logger(directorio_actual)


def test():
    logger.info(f"\n{MAGIA} BABY STEP GIANT STEP {MAGIA}")
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
            baby_step_giant_step(n, alfa, beta, p)


def modinv(a, p):
    """Calcula el inverso modular de a módulo p usando el algoritmo extendido de Euclides."""
    t, new_t = 0, 1
    r, new_r = p, a
    while new_r != 0:
        quotient = r // new_r
        t, new_t = new_t, t - quotient * new_t
        r, new_r = new_r, r - quotient * new_r
    if r > 1:
        raise ValueError(f"{a} no tiene inverso modular")
    if t < 0:
        t = t + p
    return t


def baby_step_giant_step(n, alfa, beta, p):
    """Algoritmo Baby-step Giant-step para resolver el logaritmo discreto: g^x = h (mod p)."""
    inicio = time.time()

    # Paso 1: Preparar m = ceil(sqrt(p))
    m = math.isqrt(p) + 1

    # Paso 2: Crear la tabla de Baby Steps: g^j mod p para j = 0, 1, ..., m-1
    baby_steps = {}
    current = 1
    for j in range(m):
        baby_steps[current] = j
        current = (current * alfa) % p

    # Paso 3: Calcular g^(-m) mod p (inverso de g^m mod p)
    g_m = modinv(pow(alfa, m, p), p)

    # Paso 4: Buscar en los Giant Steps
    current = beta
    for i in range(m):
        if current in baby_steps:
            # Si encontramos un match, calculamos x = i * m + j
            fin = time.time()  # Registrar el tiempo final
            duracion = fin - inicio
            x = i * m + baby_steps[current]
            logger.info(f"{n};{alfa};{beta};{p};{x};{duracion:.6f}")
            return x
        current = (current * g_m) % p

    # Si no se encontró una solución
    fin = time.time()  # Registrar el tiempo final
    duracion = fin - inicio
    x = None
    logger.info(f"{n};{alfa};{beta};{p};{x};{duracion:.6f}")
    return None
