"""Genera artefacto local: código propio sin referencias a entornos secretos."""
from pathlib import Path
import zipfile

if __name__ == '__main__':
    Path('dist').mkdir(exist_ok=True)
    destino = Path('dist/guardian-maipo-lab.zip')
    archivos = sorted(Path('src').rglob('*.py')) + [Path('config.yaml'),Path('escenarios/agua/lecturas.json')]
    with zipfile.ZipFile(destino, 'w', compression=zipfile.ZIP_DEFLATED) as z:
        for archivo in archivos:
            z.write(archivo)
    print(f'Empaquetado de laboratorio: {destino} ({len(archivos)} archivos)')
