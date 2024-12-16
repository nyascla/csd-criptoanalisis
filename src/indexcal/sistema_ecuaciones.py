import sympy

if __name__ == "__main__":
    # Datos proporcionados
    p = 421
    alfa = 2
    beta = 412
    orden = 420

    # Elegimos S
    S = [2, 3, 5, 7]

    # Construimos los S smooth
    smooth = {
        7: {2: 7},
        170: {5: 1, 7: 2},
        351: {2: 1, 3: 1, 7: 1},
        406: {2: 2, 3: 1},
        408: {2: 4, 3: 1}
    }
    # 7 = 7 * math.log(2, alfa)(mod orden)
    # 170 = math.log(5, alfa) + 2 * math.log(7, alfa)(mod orden)
    # 351 = math.log(2, alfa) + math.log(3, alfa) + math.log(7, alfa)(mod orden)
    # 406 = 2 * math.log(2, alfa) + math.log(3, alfa)(mod orden)
    # 408 = 4 * math.log(2, alfa) + math.log(3, alfa)(mod orden)

    # Definir las incógnitas simbólicas
    log2, log3, log5, log7 = sympy.symbols("log2 log3 log5 log7")

    # Definir las ecuaciones
    ecuaciones = [
        sympy.Eq(7, 7 * log2),  # Primera ecuación
        sympy.Eq(170, log5 + 2 * log7),  # Segunda ecuación
        sympy.Eq(351, log2 + log3 + log7),  # Tercera ecuación
        sympy.Eq(406, 2 * log2 + log3),  # Cuarta ecuación
        sympy.Eq(408, 4 * log2 + log3)  # Quinta ecuación
    ]

    # Resolver el sistema
    solucion = sympy.solve(ecuaciones, [log2, log3, log5, log7])

    # Mostrar la solución
    for key, value in solucion.items():
        print(key, value % orden)

    # Resolver
    trial = 102
    betaalfa = (beta * alfa**trial) % p
    betaalfa_smooth = {2: 2, 5: 1}
    # beta * alfa**trial = betaalfa_smooth
    # log_alfa(beta) + trial * log_alfa(alfa) = 2 * log_alfa(2) + log_alfa(5) mod(orden)
    # x = valor - trial


    print(280 % orden)
    print(280 - 102)