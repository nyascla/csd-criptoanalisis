"""
Algoritmo para aracar el problema del logaritmo discreto
Algoritmo Montecarlo: no determinista

Procedure:

"""
import random
from math import gcd


def pollard_rho_log(alpha, beta, p, orden):
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

    def nx(x, a, b):
        # Definir la función pseudoaleatoria basada en el valor de x
        if x % 3 == 1:
            return ((beta * x) % p)
        elif x % 3 == 0:
            return ((x**2) % p)
        elif x % 3 == 2:
            return ((alpha * x) % p)
        else:
            raise Exception("f")

    # Paso 2: Inicialización
    a1, b1 = 0, 0  # Inicializamos los valores de a y b
    a2, b2 = 0, 0  # Inicializamos otros dos pares
    x1, x2 = 1, 1  # Inicializamos x1 y x2


    # Empezamos con el algoritmo de Pollard-Rho
    for _ in range(10000):  # Número máximo de iteraciones
        a1, b1 = f(x1, a1, b1)
        x1 = nx(x1, a1, b1)

        a2, b2 = f(x2, a2, b2)
        x2 = nx(x2, a2, b2)

        a2, b2 = f(x2, a2, b2)
        x2 = nx(x2, a2, b2)

        # Paso 3: Verificar si hay colisión
        if x1 == x2:
            v = (b1 - b2) + orden
            m = mod_inv(v, orden)
            v = (a2 - a1) * m % orden
            return v

    return None


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
    p = 971
    alfa = 4
    beta = 364
    orden = 97

    # Llamamos a Pollard-Rho para encontrar el logaritmo discreto
    result = pollard_rho_log(alfa, beta, p, orden)
    print("El logaritmo discreto de beta con base alpha es:", result)

    print("alfa**result % p = b" )
    print(f"{alfa ** result % p} = {beta}")