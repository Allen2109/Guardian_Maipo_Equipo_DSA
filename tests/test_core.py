import io
import json
import os
from pathlib import Path
import tempfile
import unittest
from contextlib import redirect_stdout
from unittest.mock import patch

from guardian_maipo.core import ErrorLectura, obtener_registro, validar_sensor, validar_valor

DATA = Path('escenarios/agua/lecturas.json')


class SeguridadDelLector(unittest.TestCase):
    def test_01_lectura_ficticia(self):
        r = obtener_registro('SENS-001', DATA, credencial='TOKEN-SOLO-TEST')
        self.assertEqual(str(r.valor), '0.70')
        self.assertEqual(r.fuente, 'SIMULADA')

    def test_02_ausencia_de_credencial(self):
        with patch.dict(os.environ, {}, clear=True):
            with self.assertRaisesRegex(ErrorLectura, 'PLC_PASSWORD'):
                obtener_registro('SENS-001', DATA)

    def test_03_credencial_vacia(self):
        with self.assertRaises(ErrorLectura):
            obtener_registro('SENS-001', DATA, credencial='')

    def test_04_ningun_secreto_sale_por_stdout(self):
        output = io.StringIO()
        with redirect_stdout(output):
            obtener_registro('SENS-001', DATA, credencial='TOKEN-PRIVADO-TEST')
        self.assertNotIn('TOKEN-PRIVADO-TEST', output.getvalue())

    def test_05_codigo_potencialmente_peligroso_se_rechaza(self):
        for entrada in ('SENS-001;whoami', '../secreto', 'localhost', 'SENS-1'):
            with self.subTest(entrada=entrada):
                with self.assertRaises(ErrorLectura):
                    validar_sensor(entrada)

    def test_06_limites_didacticos(self):
        self.assertEqual(str(validar_valor('0.00')), '0.00')
        self.assertEqual(str(validar_valor('2.00')), '2.00')

    def test_07_valores_invalidos(self):
        for dato in ('-1', '2.01', 'NaN', 'InFiNiTy', 'nada', True):
            with self.subTest(dato=dato):
                with self.assertRaises(ErrorLectura):
                    validar_valor(dato)

    def test_08_sensor_desconocido(self):
        with self.assertRaisesRegex(ErrorLectura, 'no existe'):
            obtener_registro('SENS-999', DATA, credencial='DEMO')

    def test_09_archivo_ilegible(self):
        with self.assertRaises(ErrorLectura):
            obtener_registro('SENS-001', Path('archivo-no-existe.json'), credencial='DEMO')

    def test_10_json_invalido(self):
        with tempfile.TemporaryDirectory() as d:
            p = Path(d) / 's.json'
            p.write_text('{mal json', encoding='utf-8')
            with self.assertRaises(ErrorLectura):
                obtener_registro('SENS-001', p, credencial='DEMO')

    def test_11_configuracion_no_contiene_credencial(self):
        config = Path('config.yaml').read_text(encoding='utf-8')
        self.assertIn('password_env: PLC_PASSWORD', config)
        self.assertNotIn('password: LAB-CLORO-', config)

    def test_12_sin_equipos_reales(self):
        cfg = Path('infra/plc.tf').read_text(encoding='utf-8')
        self.assertNotIn('resource "', cfg)

if __name__ == '__main__':
    unittest.main()
