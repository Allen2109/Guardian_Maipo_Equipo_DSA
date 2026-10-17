"""Verifica SHA-256 antes de instalar tres binarios de escaneo en .tools/.

Las huellas provienen de un manifiesto de referencia académico y deben
contrastarse con las publicaciones oficiales si se actualiza la versión.
No instala herramientas en el sistema operativo.
"""
import hashlib
import io
import json
from pathlib import Path
import tarfile
from urllib.request import urlopen


DESTINO = Path('.tools')


def instalar():
    DESTINO.mkdir(exist_ok=True)
    especificacion = json.loads(Path('tools/binaries.json').read_text(encoding='utf-8'))
    for nombre, meta in especificacion.items():
        url = meta['url']
        if not url.startswith('https://github.com/'):
            raise ValueError('Origen del instalador no autorizado')
        with urlopen(url, timeout=120) as conexion:  # nosec: B310 - HTTPS y hash obligatorio
            contenido = conexion.read()
        digest = hashlib.sha256(contenido).hexdigest()
        if digest != meta['sha256']:
            raise RuntimeError(f'No coincide la huella SHA-256 de {nombre}')
        if url.endswith('.tar.gz'):
            with tarfile.open(fileobj=io.BytesIO(contenido), mode='r:gz') as archivo:
                miembro = next((x for x in archivo if x.isfile() and x.name == nombre), None)
                if miembro is None:
                    raise RuntimeError(f'Binario {nombre} no encontrado en el archivo')
                contenido_binario = archivo.extractfile(miembro).read()
        else:
            contenido_binario = contenido
        ejecutable = DESTINO / nombre
        ejecutable.write_bytes(contenido_binario)
        ejecutable.chmod(0o755)
        print(f'{nombre}: {meta["version"]}, descarga íntegra (SHA-256)')


if __name__ == '__main__':
    instalar()
