import logging
from datetime import datetime


# Configuración del logger
def configurar_logger():
    """Configura el logger para escribir en la salida estándar y en un archivo."""
    logger = logging.getLogger("cli_logger")
    logger.setLevel(logging.DEBUG)

    # Formato del log
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

    # Handler para la salida estándar
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)
    console_handler.setFormatter(formatter)

    # Handler para el archivo de log
    fecha_hoy = datetime.now().strftime("%Y-%m-%d")
    file_handler = logging.FileHandler(f"./logs/log_{fecha_hoy}.log")
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(formatter)

    # Añadir los handlers al logger
    logger.addHandler(console_handler)
    logger.addHandler(file_handler)

    return logger
