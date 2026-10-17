"""Inventario CycloneDX LOCAL mínimo, sin afirmar escaneo de vulnerabilidades."""
from pathlib import Path
from datetime import datetime, timezone
import json

OUT = Path('evidencias/sbom-local.cdx.json')

def main():
    datos = {
        'bomFormat': 'CycloneDX', 'specVersion': '1.5', 'version': 1,
        'metadata': {'timestamp': datetime.now(timezone.utc).isoformat(),
                     'component': {'type':'application','name':'guardian-maipo','version':'1.0.0'}},
        'components': [
            {'type':'library','name':'PyYAML','version':'6.0.3','purl':'pkg:pypi/pyyaml@6.0.3'},
        ],
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(datos,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
    print(f'SBOM académica escrita en {OUT}; generar SBOM completa con Trivy en Actions')

if __name__ == '__main__':
    main()
