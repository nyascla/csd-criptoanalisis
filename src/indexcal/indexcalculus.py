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

from src.const import MAGIA, DATASET_PATH
from src.logger import configurar_logger

S = [2, 3, 5, 7]

def test(max_talla, n_talla):
    logger = configurar_logger(__file__, __name__)
    logger.info(f"\n{MAGIA} index calculus | talla:{max_talla} {MAGIA}")
    logger.info(f"Data: n;alfa;beta;p;x;duracion")

    with open(DATASET_PATH, 'r') as j:
        d = json.load(j)

    for talla, objetos in d.items():
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


def relacion_lineal():
    pass


def is_s_smooth(n, max_p=7):
    factores = sympy.factorint(n)  # Factoriza el número n
    for factor in factores:
        if factor > max_p:
            return None
    return factores


def build_smooths(alfa, p):
    p_count = set()
    s_smooths = {}
    while len(p_count) < len(S):
        r = random.randint(1, 1000000)

        x = pow(alfa, r, p)
        f = is_s_smooth(x)
        if f:
            s_smooths[r] = f
            p_count.update(list(f.keys()))
    # s_smooths = {}
    # for t in [7, 170, 351, 406, 408]:
    #     x = (alfa ** t) % p
    #     f = is_s_smooth(x)
    #     if f:
    #         s_smooths[t] = f
    #         p_count.update(list(f.keys()))
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
    s = {}
    for key, value in solucion.items():
        s[str(key)] = value % orden
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

    for _ in range(1000):
        trial = random.randrange(0, p)
        # betaalfa = (beta * (alfa ** trial)) % p
        # Exponentiación modular para calcular (alfa ** trial) % p
        exp_mod = pow(alfa, trial, p)
        # Calcular el resultado final: (beta * (alfa ** trial)) % p
        betaalfa = (beta * exp_mod) % p

        betaalfa_smooth = is_s_smooth(betaalfa)
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
            try:
                return int(r)
            except Exception as e:
                return None
        else:
            pass


def index_calculus(alfa, beta, p, orden):
    print(alfa)
    for intentos in range(1000):
        try:
            print(1)
            s_smooths = build_smooths(alfa, p)
            print(2)
            v = build_equations(s_smooths, orden)
            print(3)
            result = solve(alfa, beta, p, orden, v)
            print(4)
        except Exception as e:
            # print(f"bbb: {e}")
            result = None

        if result:
            if pow(alfa, int(result), p) == beta:
                return result
        else:
            pass

    return -777


if __name__ == "__main__":
    pass
    # Datos proporcionados

    trial = 102
    p = 421
    alfa = 2
    beta = 412
    orden = 420

    # n = 16
    # p = 48947
    # alfa = 100
    # beta = 44488
    # orden = 24473

    # n = 16
    # p = 48947
    # alfa = 100
    # beta = 35391
    # orden = 24473

    # n = 8
    # p = 229
    # alfa = 100
    # beta = 81
    # orden = 114
    # x = nnn()
    # x = index_calculus(alfa, beta, p, orden)

    # if pow(alfa, int(x), p) == beta:
    #     print("good")