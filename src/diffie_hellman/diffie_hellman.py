import base64
import json
import os
import time

from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

from src.const import MAGIA, DATASET_PATH
from src.logger import configurar_logger

ruta_actual = os.path.abspath(__file__)
directorio_actual = os.path.dirname(ruta_actual)




def test():
    logger = configurar_logger(__file__, __name__)

    logger.info(f"\n{MAGIA} DIFFIE HELLMAN {MAGIA}")
    logger.info(f"Data: n;alfa;beta;p;x;duracion")

    with open(DATASET_PATH, 'r') as j:
        d = json.load(j)

    for talla, objetos in d.items():
        for obj in objetos:
            inicio = time.time()

            n = obj["n"]
            p = obj["p"]
            alfa = obj["alfa"]
            beta = obj["beta"]
            orden = obj["orden"]

            x = diffie_hellman(p, alfa)

            fin = time.time()  # Registrar el tiempo final
            duracion = fin - inicio

            logger.info(f"{n};{alfa};{beta};{p};{x};{duracion:.6f}")


def entero_a_bytes_32(entero):
    """
    Convierte un entero en bytes de 32 bytes, rellenando con ceros si es necesario.
    """
    return int.to_bytes(entero, 32, byteorder='big')


def encriptar(texto, clave):
    """
    Encripta un texto utilizando el algoritmo AES en modo ECB con la clave proporcionada.
    El texto debe ser una cadena de texto, y la clave un número entero.
    """
    clave_bytes = entero_a_bytes_32(clave)

    # Convertir texto a bytes
    datos = texto.encode('utf-8')

    # Crear un cifrador AES en modo ECB
    cipher = AES.new(clave_bytes, AES.MODE_ECB)

    # Rellenar el texto hasta el tamaño múltiplo de 32 bytes
    datos_rellenados = pad(datos, AES.block_size)

    # Encriptar el texto
    ciphertext = cipher.encrypt(datos_rellenados)

    # Codificar el resultado en base64 para una representación legible
    return base64.b64encode(ciphertext).decode('utf-8')


def desencriptar(texto_encriptado, clave):
    """
    Desencripta un texto previamente encriptado utilizando AES en modo ECB y la clave proporcionada.
    """
    clave_bytes = entero_a_bytes_32(clave)

    # Decodificar el texto encriptado de base64
    ciphertext = base64.b64decode(texto_encriptado)

    # Crear un cifrador AES
    cipher = AES.new(clave_bytes, AES.MODE_ECB)

    # Desencriptar el texto
    datos_desencriptados = unpad(cipher.decrypt(ciphertext), AES.block_size)

    # Convertir los bytes de vuelta a texto
    return datos_desencriptados.decode('utf-8')


class Persona:
    def __init__(self, nombre, secreto, primo, base):
        """
        Inicializa una persona con su nombre, secreto, número primo y base para Diffie-Hellman.
        """
        self.nombre = nombre
        self.secreto = secreto  # Secreto de la persona
        self.primo = primo  # Número primo para Diffie-Hellman
        self.base = base  # Base para Diffie-Hellman
        self.clave_publica = self.calcular_clave_publica()  # Clave pública calculada

    def calcular_clave_publica(self):
        """
        Calcula la clave pública de la persona utilizando su secreto y los parámetros de Diffie-Hellman.
        """
        return (self.base ** self.secreto) % self.primo

    def generar_clave_compartida(self, clave_publica_otro):
        """
        Calcula la clave compartida utilizando la clave pública del otro participante.
        """
        return (clave_publica_otro ** self.secreto) % self.primo

    def encriptar_mensaje(self, clave_publica_otro, mensaje):
        """
        Encripta un mensaje utilizando la clave pública del otro participante.
        """
        clave_compartida = self.generar_clave_compartida(clave_publica_otro)
        return encriptar(mensaje, clave_compartida)

    def desencriptar_mensaje(self, clave_publica_otro, mensaje_encriptado):
        """
        Desencripta un mensaje utilizando la clave pública del otro participante.
        """
        clave_compartida = self.generar_clave_compartida(clave_publica_otro)
        return desencriptar(mensaje_encriptado, clave_compartida)


def diffie_hellman(primo, base):
    """
    Función principal para ejecutar el intercambio de mensajes utilizando Diffie-Hellman y AES.
    """
    # Inicializar a Alice y Bob
    alice = Persona(nombre="Alice", secreto=6, primo=primo, base=base)
    bob = Persona(nombre="Bob", secreto=15, primo=primo, base=base)

    # Mensaje a intercambiar
    mensaje_original = "En un lugar de la Mancha, de cuyo nombre no quiero acordarme..."

    # Alice encripta el mensaje para Bob
    mensaje_encriptado = alice.encriptar_mensaje(bob.clave_publica, mensaje_original)
    # print(f"Mensaje encriptado: {mensaje_encriptado}")

    # Bob desencripta el mensaje de Alice
    mensaje_desencriptado = bob.desencriptar_mensaje(alice.clave_publica, mensaje_encriptado)
    # print(f"Mensaje desencriptado por Bob: {mensaje_desencriptado}")

    return mensaje_original == mensaje_desencriptado


def check():
    a = 6
    b = 15
    p = 23
    base = 5
    x = ((base ** a) ** b) % p
    y = ((base ** b) ** a) % p
    print(f"PK: {x} PK: {y} OK: {x == y}")
    assert x == y, "Error Garrafal"


if __name__ == "__main__":
    # Ejecutar el intercambio de mensajes con los parámetros de Diffie-Hellman
    # check()
    diffie_hellman(primo=23, base=5)

