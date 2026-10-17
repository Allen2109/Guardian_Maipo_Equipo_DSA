"""Auditoría local de que el ZIP se prepara con workflows en la raíz."""
from pathlib import Path
import sys

REQUERIDOS = [
    '.github/workflows/integracion.yml',
    '.github/workflows/seguridad.yml',
    '.github/workflows/ejercicio-1.yml',
    '.gitleaks.toml', '.semgrep.yml',
    'ENTREGABLE.md', 'README.md', 'requirements.txt',
    'config.yaml','infra/plc.tf','infra/panel.yaml','policies/panel.rego',
    'src/guardian_maipo/core.py','tests/test_core.py',
    'docs/amenazas/analisis.md','docs/arquitectura/diagrama.svg',
    'docs/auditoria-ia/veredicto.md','docs/exposicion/guion.md',
    'evidencias/VALIDACION.md', 'evidencias/sbom-local.cdx.json',
    'reportes/Informe_Guardian_Maipo.pdf',
    'reportes/Presentacion_Guardian_Maipo.pptx',
]


def main():
    fallas = [item for item in REQUERIDOS if not Path(item).is_file()]
    txt = Path('ENTREGABLE.md').read_text(encoding='utf-8')
    for nombre in ('Daniel Silva','Allen Ramirez','Antonella Mancilla'):
        if nombre not in txt:
            fallas.append(f'Integrante ausente: {nombre}')
    for archivo in Path('.github/workflows').glob('*.yml'):
        contenido = archivo.read_text(encoding='utf-8')
        if 'runs-on:' not in contenido or 'jobs:' not in contenido:
            fallas.append(f'Workflow incompleto: {archivo}')
    if fallas:
        for item in fallas:print('FALTA:',item,file=sys.stderr)
        raise SystemExit(1)
    print('Estructura correcta: tres workflows en la raiz y tres integrantes acreditados.')
    print(f'Archivos obligatorios revisados: {len(REQUERIDOS)}')


if __name__ == '__main__':
    main()
