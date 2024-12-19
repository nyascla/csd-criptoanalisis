import logging
from datetime import datetime
import os

# Configuración del logger
def configurar_logger(file, name):
    """Configura el logger para escribir en la salida estándar y en un archivo."""
    ruta_actual = os.path.abspath(file)
    base_path = os.path.dirname(ruta_actual)
    log_path = os.path.join(base_path, "logs")
    os.makedirs(log_path, exist_ok=True)

    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)

    # Formato del log
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

    # Handler para la salida estándar
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)
    console_handler.setFormatter(formatter)

    # Handler para el archivo de log
    fecha_hoy = datetime.now().replace(microsecond=0)
    file_handler = logging.FileHandler(f"{log_path}/log_{fecha_hoy}.log")
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(formatter)

    # Añadir los handlers al logger
    logger.addHandler(console_handler)
    logger.addHandler(file_handler)

    return logger
