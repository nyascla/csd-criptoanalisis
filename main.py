import argparse
import sys

from src.logger import configurar_logger

# Logger global
logger = configurar_logger()


# Funciones principales del programa
def comando_principal(argumento1, argumento2):
    """Ejemplo de función principal para un comando."""
    logger.info(f"Ejecutando el comando principal con argumento1={argumento1} y argumento2={argumento2}")


def otro_comando(opcion):
    """Ejemplo de otra función para un comando."""
    logger.info(f"Ejecutando otro comando con la opción={opcion}")


# Configuración del CLI
def main():
    parser = argparse.ArgumentParser(
        description="Plantilla de programa con interfaz CLI en Python",
        epilog="Gracias por usar este programa!"
    )

    # Subcomandos
    subparsers = parser.add_subparsers(title="Comandos", dest="comando", required=True)

    # Subcomando: baby-giant-step
    parser_otro = subparsers.add_parser("baby-giant-step", help="Ejecuta baby-giant-step")
    parser_otro.add_argument("--opcion", type=str, default="valor_por_defecto", help="Una opción para este comando")
    parser_otro.set_defaults(func=lambda args: otro_comando(args.opcion))

    # Subcomando: pollards-rho
    parser_otro = subparsers.add_parser("pollards-rho", help="Ejecuta pollards-rho")
    parser_otro.add_argument("--opcion", type=str, default="valor_por_defecto", help="Una opción para este comando")
    parser_otro.set_defaults(func=lambda args: otro_comando(args.opcion))

    # Subcomando: index-calculus
    parser_principal = subparsers.add_parser("index-calculus", help="Ejecuta index-calculus")
    parser_principal.add_argument("argumento1", type=str, help="El primer argumento obligatorio")
    parser_principal.add_argument("argumento2", type=int, help="El segundo argumento obligatorio, debe ser un entero")
    parser_principal.set_defaults(func=lambda args: comando_principal(args.argumento1, args.argumento2))

    # Si no se pasan argumentos, mostrar la ayuda
    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit(0)

    # Parseo de argumentos
    args = parser.parse_args()

    # Ejecutar la función asociada al comando
    try:
        args.func(args)
    except Exception as e:
        logger.error(f"Error: {e}", exc_info=True)
        sys.exit(1)


if __name__ == "__main__":
    main()
