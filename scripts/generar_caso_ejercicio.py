"""Crea un error SOLO en un directorio temporal controlado (no en main)."""
import argparse
from pathlib import Path


def crear(destino: Path, modo: str) -> Path:
    destino.mkdir(parents=True, exist_ok=True)
    ruta = destino / 'config.yaml'
    if modo == 'fallo':
        # No guardamos un valor con el patrón completo en el código fuente.
        clave_de_laboratorio = 'LAB-' + 'CLORO-' + '2026-' + 'DEMO'
        ruta.write_text(f'sistema: laboratorio\npassword: {clave_de_laboratorio}\n',encoding='utf-8')
    elif modo == 'corregido':
        ruta.write_text('sistema: laboratorio\npassword_env: PLC_PASSWORD\n',encoding='utf-8')
    else:
        raise ValueError('Modo no reconocido')
    return ruta


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--destino', type=Path, required=True)
    parser.add_argument('--modo', choices=['fallo','corregido'], required=True)
    args = parser.parse_args()
    archivo = crear(args.destino,args.modo)
    print(f'Caso de prueba creado: {archivo} (sin mostrar su contenido)')
