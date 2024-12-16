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

import random

import sympy


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


def build_smooths(p):
    p_count = set()
    s_smooths = {}
    while len(p_count) < len(S):
        r = random.randint(1, 10000)

        x = (alfa ** r) % p
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
    print(p_count)
    print(s_smooths)
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
    print("Ecuaciones:", ecuaciones)
    print("Variables dict:", variables_dict)

    # Resolver el sistema de ecuaciones
    solucion = sympy.solve(ecuaciones, list(variables_dict.values()))
    s = {}
    print(solucion)
    for key, value in solucion.items():
        s[str(key)] = value % orden
    print(s)
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

    trial = 102
    betaalfa = (beta * (alfa ** trial)) % p
    print(betaalfa)
    betaalfa_smooth = is_s_smooth(betaalfa)
    print(betaalfa_smooth)
    if betaalfa_smooth:
        s = ""
        for base, exponente in betaalfa_smooth.items():
            if exponente == 1:
                s += f"log{base}+"
            else:
                s += f"{exponente}*log{base}+"
        s = s[:-1]
        expresion = s
        print(expresion)
        print(valores_log)
        resultado = eval(expresion, {}, valores_log)
        print(resultado)

        return resultado - trial

        # beta * alfa**trial = betaalfa_smooth

    # log_alfa(beta) + trial * log_alfa(alfa) = 2*log2+log5
    # x = valor - trial


def index_calculus(n, alfa, beta, p, orden):
    s_smooths = build_smooths(p)
    v = build_equations(s_smooths, orden)
    result = solve(alfa, beta, p, orden, v)
    print("@@@ SOLUTION @@@")
    print(result)


if __name__ == "__main__":
    # Datos proporcionados
    p = 421
    alfa = 2
    beta = 412
    orden = 420

    # Elegimos S
    S = [2, 3, 5, 7]

    index_calculus(0, alfa, beta, p, orden)