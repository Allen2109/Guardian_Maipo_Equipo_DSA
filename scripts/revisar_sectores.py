"""Pruebas estáticas de cuatro escenarios de simulación, sin redes externas."""
from pathlib import Path
import json
import sys

CASES = {
    'agua': Path('escenarios/agua/lecturas.json'),
    'energia': Path('escenarios/energia/control.json'),
    'salud': Path('escenarios/salud/registro_ejemplo.json'),
    'transporte': Path('escenarios/transporte/panel.json'),
}


def comprobar():
    for sector, path in CASES.items():
        data = json.loads(path.read_text(encoding='utf-8'))
        if sector == 'agua':
            assert all(c.startswith('SENS-') for c in data)
        elif sector == 'energia':
            assert data['estado'] == 'SIMULADO'
        elif sector == 'salud':
            assert not any(k in data for k in ('rut', 'nombre', 'diagnostico', 'paciente'))
        elif sector == 'transporte':
            assert '0.0.0.0/0' not in data['origenes_permitidos']
        print(f'OK {sector}: comprobación estática satisfactoria')


if __name__ == '__main__':
    try:
        comprobar()
    except (OSError, ValueError, AssertionError, KeyError) as ex:
        print(f'ERROR: {ex}', file=sys.stderr)
        raise SystemExit(1)
