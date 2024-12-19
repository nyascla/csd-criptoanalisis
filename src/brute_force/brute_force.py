import json
import time

from src.const import MAGIA, DATASET_PATH
from src.logger import configurar_logger


def test(max_talla, n_talla):
    logger = configurar_logger(__file__, __name__)
    logger.info(f"\n{MAGIA} FUERZA BRUTA talla:{max_talla} {MAGIA}")
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

            x = logaritmo_discreto_fuerza_bruta(alfa, beta, p)

            fin = time.time()  # Registrar el tiempo final
            duracion = fin - inicio

            logger.info(f"{n};{alfa};{beta};{p};{x};{duracion:.6f}")

            c += 1


# Problema del logaritmo discreto: Encontrar x tal que g^x ≡ y (mod p)
def logaritmo_discreto_fuerza_bruta(alfa, beta, p):
    """
    Encontrar x tal que alfa^x ≡ beta (mod p)
    """
    for x in range(p):  # Probar todos los valores posibles de x (de 0 a p-1)
        if pow(alfa, x, p) == beta:  # Verificar si g^x mod p == y
            return x
    return None  # Si no se encuentra una solución (teóricamente improbable si alfga es una base válida)


def es_grupo_uniforme(primo, base):
    """
    Comprueba si la base genera un grupo cíclico uniforme módulo un número primo.
    """
    elementos_generados = set()
    for exponente in range(primo - 1):  # El orden de un grupo multiplicativo mod primo es primo-1
        valor = pow(base, exponente, primo)  # base^exponente mod primo
        elementos_generados.add(valor)

    # Si la cantidad de elementos generados es igual a primo-1, es un grupo cíclico uniforme
    if len(elementos_generados) == primo - 1:
        print(f"La base {base} forma un grupo cíclico uniforme módulo {primo}.")
        return True
    else:
        print(f"La base {base} NO forma un grupo cíclico uniforme módulo {primo}.")
        return False


def basic_test():
    base = 5
    congruente = 8
    primo = 23

    print(f"t tal que {base}^t ≡ {congruente} (mod {primo})")
    print(f"Calculando...")
    t = logaritmo_discreto_fuerza_bruta(alfa=base, beta=congruente, p=primo)

    assert (base ** t) % primo == congruente, "Error Garrafal"
    print(f"t: {t}")
    print("(base ** t) % primo, congruente")
    print(f"({base} ** {t}) % {primo} = {congruente}")


if __name__ == "__main__":
    pass
