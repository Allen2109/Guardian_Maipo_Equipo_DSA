"""Interfaz de consola del laboratorio; no abre sockets."""
import argparse
import json
from pathlib import Path
from .core import ErrorLectura, obtener_registro


def main() -> int:
    parser = argparse.ArgumentParser(description='Lector ficticio de Maipo Sur')
    parser.add_argument('--sensor', default='SENS-001')
    parser.add_argument('--datos', type=Path, default=Path('escenarios/agua/lecturas.json'))
    args = parser.parse_args()
    try:
        resultado = obtener_registro(args.sensor, args.datos)
    except ErrorLectura as exc:
        parser.exit(2, f'Error controlado: {exc}\n')
    print(json.dumps(resultado.a_diccionario(), ensure_ascii=False))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
