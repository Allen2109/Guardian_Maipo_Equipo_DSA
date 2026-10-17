"""Consulta local de registros ficticios de una estación de tratamiento de agua.

No se admiten direcciones de red, comandos del sistema ni control de PLC.
Los límites son parámetros del ejercicio, NO valores sanitarios certificados.
"""
from dataclasses import dataclass
from decimal import Decimal, InvalidOperation
from pathlib import Path
import json
import os
import re

CODIGO_SENSOR = re.compile(r'\ASENS-[0-9]{3}\Z')
MIN_DEMO = Decimal('0.00')
MAX_DEMO = Decimal('2.00')

class ErrorLectura(ValueError):
    """Entrada fuera del contrato académico."""

@dataclass(frozen=True)
class Registro:
    sensor: str
    valor: Decimal
    unidad: str = 'mg/L'
    fuente: str = 'SIMULADA'

    def a_diccionario(self):
        return {
            'sensor': self.sensor,
            'valor': str(self.valor),
            'unidad': self.unidad,
            'fuente': self.fuente,
        }


def validar_sensor(codigo: str) -> str:
    if not isinstance(codigo, str) or not CODIGO_SENSOR.fullmatch(codigo):
        raise ErrorLectura('Código de sensor inválido; formato esperado SENS-000')
    return codigo


def validar_valor(valor) -> Decimal:
    if isinstance(valor, bool) or not isinstance(valor, (str, int, float, Decimal)):
        raise ErrorLectura('El valor debe ser numérico')
    try:
        numero = Decimal(str(valor))
    except InvalidOperation as exc:
        raise ErrorLectura('El valor debe ser numérico') from exc
    if not numero.is_finite() or not MIN_DEMO <= numero <= MAX_DEMO:
        raise ErrorLectura('La lectura está fuera del intervalo didáctico')
    return numero


def obtener_registro(codigo: str, archivo: Path, *, credencial: str | None = None) -> Registro:
    validar_sensor(codigo)
    valor_secreto = credencial if credencial is not None else os.environ.get('PLC_PASSWORD')
    if not valor_secreto:
        raise ErrorLectura('Falta PLC_PASSWORD en el entorno')
    try:
        registros = json.loads(Path(archivo).read_text(encoding='utf-8'))
    except (OSError, ValueError) as exc:
        raise ErrorLectura('No es posible leer el conjunto ficticio de datos') from exc
    if not isinstance(registros, dict) or codigo not in registros:
        raise ErrorLectura('El sensor indicado no existe en el laboratorio')
    return Registro(sensor=codigo, valor=validar_valor(registros[codigo]))
