from src.brute_force import brute_force
from src.bsgs import bsgs
from src.diffie_hellman import diffie_hellman
from src.indexcal import indexcalculus
from src.pollard_rho import pollard_rho

import matplotlib.pyplot as plt
from sympy import mod_inverse

"""
    brute_force.test()
    bsgs.test()
    pollard_rho.test()
    indexcalculus.test()
    diffie_hellman.test()
"""


def verificar_generador(alpha, p, orden):
    """
    Verifica si alpha es un generador primitivo del grupo cíclico módulo p.
    """
    # Calcula los valores generados
    valores = set()
    for x in range(orden):
        valores.add(pow(alpha, x, p))

    # Verificar la cardinalidad del conjunto
    es_generador = len(valores) == orden
    print(f"alpha: {alpha} | p: {p} | orden: {orden}")
    print(f"orden: {orden} | valores generados: {len(valores)}")

    # Retornar resultados
    return es_generador, valores


def graficar_distribucion(valores, p):
    """
    Grafica la distribución de los valores generados en el grupo cíclico.
    """
    valores_lista = sorted(valores)
    plt.scatter(range(len(valores_lista)), valores_lista, alpha=0.7, color='blue', s=10)
    plt.xlabel('Índice')
    plt.ylabel('Valores Generados (mod p)')
    plt.title('Distribución de Valores Generados')
    plt.grid(True)
    plt.savefig("./distribucion.png")


def t():
    # x, y = verificar_generador(100,48947,24473)
    x, y = verificar_generador(2, 48947, 48946)
    graficar_distribucion(y, 24473)


if __name__ == "__main__":
    # 192, 50
    # 32, 10
    # brute_force.single_test()
    # pollard_rho.test(32, 10)

    import numpy as np
    import pandas as pd

    # Datos de la tabla proporcionada (tamaño en bits y tiempo en segundos)
    bit_sizes = np.array([8, 10, 16, 24, 32, 36])
    times_seconds = np.array([0.00000514, 0.0000227, 0.00347334, 2.42397878, 370.211726, 3733.688423])

    # Calcular los valores de p y sus logaritmos
    p_values = 2 ** bit_sizes
    log_p_values = np.log(p_values)

    # Ajuste de coeficiente k en el modelo O(p * log(p)) usando los datos existentes
    # Utilizamos un ajuste lineal entre p * log(p) y los tiempos en segundos
    # Revisamos valores que puedan ser problemáticos en los cálculos
    try:
        model_coefficient, _ = np.polyfit(p_values * log_p_values, times_seconds, 1)
    except np.linalg.LinAlgError:
        print("Error en la creación del modelo, quizás los valores sean demasiado grandes.")

    # Generar tamaños p más grandes para estimación (nuevo conjunto de bits)
    target_bit_sizes = np.array([40, 44, 48, 52, 56, 60, 64, 80, 96, 112, 128, 144, 160, 192])
    target_p_values = 2 ** target_bit_sizes
    target_log_p_values = np.log(target_p_values)

    # Evitar valores excesivamente grandes usando un manejo más conservador del logaritmo
    safe_log_p_values = np.log(target_p_values)
    safe_target_times = model_coefficient * target_p_values * safe_log_p_values

    # Reemplazar tiempos imposibles (en caso de que no se genere un resultado válido)
    safe_target_times[safe_target_times > 1e+10] = np.nan

    # Crear un DataFrame con los resultados
    results = pd.DataFrame({
        "Bits": target_bit_sizes,
        "Estimated Time (Seconds)": safe_target_times
    })

    # Mostrar los resultados
    print(results)
