"""
Algoritmo para aracar el problema del logaritmo discreto
Algoritmo Montecarlo: no determinista

Procedure:

"""

import json
import random
import time
from math import gcd
from sympy import mod_inverse

# from src.const import MAGIA, DATASET_PATH
# from src.logger import configurar_logger

ITERACIOENS = 5000000


def test(max_talla, n_talla):
    logger = configurar_logger(__file__, __name__)
    logger.info(f"\n{MAGIA} pollard_rho_log | talla:{max_talla} {MAGIA}")
    logger.info(f"Data: n;alfa;beta;p;orden;x;duracion")

    ok = 0
    err = 0
    with open(DATASET_PATH, "r") as j:
        d = json.load(j)
    c = {
            "colision": 0,
            "no_inv": 0,
            "no_sol": 0,
            "sol": 0    
        } 
    for talla, objetos in d.items():
        if int(talla) < max_talla:
            continue
        if int(talla) > max_talla:
            # logger.info(f"iteraciones: {ITERACIOENS} | ok: {ok} | err: {err}")
            logger.info(f"iteraciones: {ITERACIOENS} | colisiones: {c["colision"]} | no_inv: {c["no_inv"]} | no_sol: {c["no_sol"]} | sol: {c["sol"]}")

            return
        count = 1
        for obj in objetos:
            if count > n_talla:
                break

            inicio = time.time()

            n = obj["n"]
            p = obj["p"]
            alfa = obj["alfa"]
            beta = obj["beta"]
            orden = obj["orden"]

            # if beta == 146970801:
            #     print("pass")
            #     continue

            x, c = pollard_rho_log(alfa, beta, p, orden, c)

            fin = time.time()  # Registrar el tiempo final
            duracion = fin - inicio

            if not x:
                err += 1
                x = 0
            else:
                ok += 1
            logger.info(f"{n};{alfa};{beta};{p};{orden};{x};{duracion:.6f}")

            # assert (((alfa ** x) % p) == beta), "error garrafal"

            count += 1
    
    
    logger.info(f"problemas: {ok + err} | iteraciones: {ITERACIOENS} | ok: {ok} | err: {err}")

def pollard_rho_log(alpha, beta, p, orden, c):
    # Paso 1: Definir la función pseudoaleatoria
    # 0 % 3 = 0
    # 1 % 3 = 1
    # 2 % 3 = 2
    # 3 % 3 = 0
    
    def f(x, a, b):
        # Definir la función pseudoaleatoria basada en el valor de x
        if x % 3 == 1:
            return (a, (b + 1) % (p - 1))
        elif x % 3 == 0:
            return ((2 * a) % (p - 1), (2 * b) % (p - 1))
        elif x % 3 == 2:
            return ((a + 1) % (p - 1), b)
        else:
            raise Exception("f")

    def nx(x):
        # Definir la función pseudoaleatoria basada en el valor de x
        if x % 3 == 1:
            return (beta * x) % p
        elif x % 3 == 0:
            return (x**2) % p
        elif x % 3 == 2:
            return (alpha * x) % p
        else:
            raise Exception("f")

    # Paso 2: Inicialización
    a1, b1 = 0, 0  # Inicializamos los valores de a y b
    a2, b2 = 0, 0  # Inicializamos otros dos pares
    x1, x2 = 1, 1  # Inicializamos x1 y x2

    # Empezamos con el algoritmo de Pollard-Rho
    for i in range(ITERACIOENS):  # Número máximo de iteraciones
    # while(1):
        a1, b1 = f(x1, a1, b1)
        x1 = nx(x1)

        a2, b2 = f(x2, a2, b2)
        x2 = nx(x2)

        a2, b2 = f(x2, a2, b2)
        x2 = nx(x2)

        # Paso 3: Verificar si hay colisión
        if x1 == x2:
            c["colision"] += 1
            v = b1 - b2 + orden
            try:
                m = mod_inverse(v, orden)
                # esto se garantiza solo para ordenes primos
     
                v = ((a2 - a1) * m) % orden
                if pow(alpha, v, p) == beta:
                    c["sol"] += 1
                    return v, c
                
                c["no_sol"] += 1
            
            except Exception as e:
                c["no_inv"] += 1
    return None, c


# Función para calcular el inverso modular
def mod_inv(a, m):
    # Usamos el algoritmo de Euclides extendido para encontrar el inverso modular
    t, new_t = 0, 1
    r, new_r = m, a
    while new_r != 0:
        quotient = r // new_r
        t, new_t = new_t, t - quotient * new_t
        r, new_r = new_r, r - quotient * new_r
    if r > 1:
        return None  # No tiene inverso modular
    if t < 0:
        t = t + m

    return t


if __name__ == "__main__":
    # Ejemplo de uso
    # p = 853
    # alfa = 9
    # beta = 804
    # orden = 71

    # p = 971
    # alfa = 4
    # beta = 364
    # orden = 97

    err8 = {
            "n": 8,
            "p": 229,
            "alfa": 100,
            "beta": 81,
            "orden": 114
        }
    
    err16 = {
            "n": 16,
            "p": 48947,
            "alfa": 2,
            "beta": 46122,
            "orden": 48946
        }
    
    ok = {
            "n": 16,
            "p": 48947,
            "alfa": 100,
            "beta": 35391,
            "orden": 24473
        }
    
    tt = {
            "n": 8,
            "p": 229,
            "alfa": 100,
            "beta": 81,
            "orden": 114
        }
    
    d=tt
    c = {
        "colision": 0,
        "no_inv": 0,
        "no_sol": 0,
        "sol": 0    
    } 
    
    inicio = time.time()
    print("inicio:", inicio)

    # Llamamos a Pollard-Rho para encontrar el logaritmo discreto
    result = pollard_rho_log(d["alfa"], d["beta"], d["p"], d["orden"],c)
   
    fin = time.time()  # Registrar el tiempo final
    duracion = fin - inicio
    print("duracion:", duracion)
    print("El logaritmo discreto de beta con base alpha es:", result)

    print("alfa**result % p = b")
    print(f"{d["alfa"] ** result % d["p"]} = {d["beta"]}")
