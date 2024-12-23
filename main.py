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
    x, y = verificar_generador(2,48947,48946)
    graficar_distribucion(y, 24473)


if __name__ == "__main__":
    indexcalculus.single_test()
    # t()


