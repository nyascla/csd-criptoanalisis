"""
seleccionar una serie de numeros primos
generar equaciones
while not todos los primos en las ecuaciones:
    1. numero random
    2. foctorizacion de primmos
    3. if S-smooth
    4. aplicamos el logaritmos para obtener una relacion lineal
        - una ecuacion de suma de logaritmos
        - ahora en modulo del orden
resolver el sistema
obtener los logaritmos de los elementos en S

while no solucion
    1. generar mas r
    2. if beta x alfa^r mod n es s-smooth
        - generamos la relacion lineal
        - ahora es facil de resolver
            - porque todos los logaritmos sabemos su resultado
            - log_alfa beta + r = relacion lineal
            - return = log_alfa beta
"""
import json
import random
import time

import sympy
from collections import defaultdict

from src.const import MAGIA, DATASET_PATH
from src.logger import configurar_logger
# 2 3 5 7 11 13 17
S = [2, 3, 5, 7, 11, 13, 17]

def single_test():
    n = 32
    p = 2703258601
    alfa = 87
    beta = 1218285964
    orden = 1351629300

    x = index_calculus(alfa, beta, p, orden)

    if pow(alfa, int(x), p) == beta:
        print("GOOD")


def test(max_talla, n_talla):
    logger = configurar_logger(__file__, __name__)
    logger.info(f"\n{MAGIA} index calculus | talla:{max_talla} {MAGIA}")
    logger.info(f"Data: n;alfa;beta;p;x;duracion")

    with open(DATASET_PATH, 'r') as j:
        d = json.load(j)

    for talla, objetos in d.items():
        if int(talla) < max_talla: continue
        if int(talla) > max_talla: return
        c = 1
        for obj in objetos:
            if c > n_talla:
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

            x = index_calculus(alfa, beta, p, orden)

            fin = time.time()  # Registrar el tiempo final
            duracion = fin - inicio

            logger.info(f"{n};{alfa};{beta};{p};{x};{duracion:.6f}")
            
            c += 1


def exp_mod(base, exponente, mod):
    result = 1
    base = base % mod  # Asegurarse de que la base esté en el rango del módulo
    while exponente > 0:
        if exponente % 2 == 1:
            result = (result * base) % mod
        base = (base * base) % mod
        exponente = exponente // 2
    return result





def is_s_smooth(n, max_p):
    factores = sympy.factorint(n)  # Factoriza el número n
    for factor in factores:
        if factor > max_p:
            return None
    return factores

def sigue(primos_count):
    if len(S) > len(primos_count.keys()):
        return True
    
    if not all(value >= 1


               for value in primos_count.values()):
        return True
    
    return False
    

def build_smooths(alfa, p, orden):
    primos_count = defaultdict(int)
    primos_count[2] = 0 
    s_smooths = {}
    c = 0
    while sigue(primos_count):
        r = random.randint(1, orden)
        # print(r)
        if r not in s_smooths:
            x = pow(alfa, r, p)
            f = is_s_smooth(x, S[-1])
            if f :
                s_smooths[r] = f
                for key in f.keys():
                    primos_count[key] += 1
                print(f"\r{c}/1000 {s_smooths}", end="")
        c += 1
    print(f"S: {S}")
    print(f"s_smooths: {s_smooths}")
    print(f"primos_count: {primos_count}")
    return s_smooths


def build_equations(s_smooths, orden):
    # Variables y ecuaciones dinámicas
    variable_names = [f"log{s}" for s in S]

    ecuaciones_data = []
    for r, factorizacion_primos in s_smooths.items():
        s = ""
        for base, exponente in factorizacion_primos.items():
            if exponente == 1:
                s += f"log{base}+"
            else:
                s += f"{exponente}*log{base}+"
        s = s[:-1]
        ecuaciones_data.append((r, s))

    # Crear las variables simbólicas dinámicamente
    variables = sympy.symbols(" ".join(variable_names))
    variables_dict = {name: var for name, var in zip(variable_names, variables)}

    # Construir ecuaciones dinámicamente con sympy.sympify
    ecuaciones = [
        sympy.Eq(lhs, sympy.sympify(rhs, locals=variables_dict)) for lhs, rhs in ecuaciones_data
    ]

    # Depuración: imprime ecuaciones y variables

    # Resolver el sistema de ecuaciones
    solucion = sympy.solve(ecuaciones, list(variables_dict.values()))

    if not solucion:
        return
    s = {}
    print(f"solucion types: {type(solucion)}")
    print(f"solucion: {solucion}")

    for key, value in solucion.items():
        s[str(key)] = value % orden

    print(f"ecuaciones: {ecuaciones}")
    print(f"solucion: {solucion}")
    print(f"s: {s}")

    return s


def solve(alfa, beta, p, orden, valores_log):
    # # Resolver
    # trial = 102
    # betaalfa = (beta * alfa ** trial) % p
    # betaalfa_smooth = {2: 2, 5: 1}
    # # beta * alfa**trial = betaalfa_smooth
    # # log_alfa(beta) + trial * log_alfa(alfa) = 2 * log_alfa(2) + log_alfa(5) mod(orden)
    # # x = valor - trial
    #
    # print(280 % orden)
    # print(280 - 102)

    # trial = 102

    for _ in range(1000000):
        trial = random.randrange(0, p)

        exp_mod = pow(alfa, trial, p)
        betaalfa = (beta * exp_mod) % p
        betaalfa_smooth = is_s_smooth(betaalfa, S[-1])

        if betaalfa_smooth:
            s = ""
            for base, exponente in betaalfa_smooth.items():
                if exponente == 1:
                    s += f"log{base}+"
                else:
                    s += f"{exponente}*log{base}+"
            s = s[:-1]
            expresion = s

            resultado = eval(expresion, {}, valores_log)
            r = resultado - trial

            return int(r)



def index_calculus(alfa, beta, p, orden):
    for intentos in range(1000):
        try:
            print(f"--- buscando los s_smooths")
            s_smooths = build_smooths(alfa, p, orden)
            print(f"--- construimos las ecuaciones")
            v = build_equations(s_smooths, orden)
            print(f"--- resolvemos las ecuaciones")
            result = solve(alfa, beta, p, orden, v)
        except Exception as e:
            print(f"index_calculus Exception {e}")
            result = None
        print(f"result: {result}")
        if result:
            if pow(alfa, int(result), p) == beta:
                print(f"GOOD: {result}")
                return result
            else:
                print(f"BAD: {result}")
    return 0

# trial = 102
# p = 421
# alfa = 2
# beta = 412
# orden = 420

if __name__ == "__main__":
    # n = 16
    # p = 48947
    # alfa = 2
    # beta = 30855
    # orden = 48946

    n = 32
    p = 2703258601
    alfa = 87
    beta = 1218285964
    orden = 1351629300

    x = index_calculus(alfa, beta, p, orden)

    if pow(alfa, int(x), p) == beta:
        print("GOOD")

"""
El último algoritmo analizado es el de Index Calculus, actualmente el más potente para resolver problemas de logaritmos discretos de mayor tamaño y el que se utiliza en escenarios prácticos para romper instancias más desafiantes. En este tipo de problemas, la mayor dificultad radica en la construcción de un sistema de ecuaciones lineales que será utilizado para despejar valores y calcular la solución final.
Proceso General del Algoritmo
El algoritmo se divide en dos etapas principales:
Construcción del Sistema de Ecuaciones
Para generar un conjunto de ecuaciones que luego resolveremos, seguimos estos pasos:
Selección de una base de números primos: Elegimos un conjunto S de números primos, llamado la base de factorización.
Generación de ecuaciones: Utilizamos un proceso iterativo para encontrar números que se puedan factorizar completamente en términos de los primos de S:
while not todos los primos en las ecuaciones:
    1. Generar un número aleatorio.
    2. Factorizar el número.
    3. Si es \( S \)-smooth (factorizable usando únicamente los primos en \( S \)):
        - Aplicar logaritmos para obtener una relación lineal.
        - Añadir una ecuación en términos de suma de logaritmos módulo el orden del grupo.
Una vez que hemos generado suficientes ecuaciones, resolvemos el sistema lineal para obtener los logaritmos de todos los elementos en S.

Resolución del Logaritmo Discreto
Con el sistema de ecuaciones resuelto y los logaritmos de la base calculados, buscamos resolver el problema de logaritmo discreto:

while no solucion:
    1. Generar un valor \( r \) aleatorio.
    2. if beta x alfa^random mod p es s-smooth
- Generar la relación lineal correspondiente. 
- Como ya conocemos los logaritmos de todos los primos en \( S \), resolver es directo:

"""