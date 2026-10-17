# Validación y evidencia: hechos, no capturas inventadas

**Fecha de construcción local:** 16-10-2026  
**Equipo:** Daniel Silva, Allen Ramirez y Antonella Mancilla

## 1. Resultados locales reproducidos en el entorno de preparación

| Control local | Resultado real observado |
|---|---|
| `python -m unittest discover -s tests -v` | **12 pruebas aprobadas (12/12)** |
| `python scripts/revisar_sectores.py` | **4 escenarios aprobados (4/4)** |
| Compilación e importación Python | **Correctas** |
| Lector simulado con variable ficticia | **Correcto**, valor `0.70` sin credencial en salida |
| Empaquetado de laboratorio | **Generado** en `dist/` local |
| SBOM académica | **Generada** en `evidencias/sbom-local.cdx.json`; no certifica vulnerabilidades |

Estas observaciones **no equivalen a un éxito de GitHub Actions**, porque el ZIP puede descargarse antes de ejecutar CI remoto.

## 2. Evidencias por completar desde GitHub

| Evidencia | Resultado/URL/fecha a completar por el equipo |
|---|---|
| Repositorio nuevo | PENDIENTE: pegar URL real |
| Integración en GitHub Actions | PENDIENTE: URL del run y captura |
| Seguridad: Gitleaks, Semgrep, Trivy, OSV | PENDIENTE: URL del run; reportes y estado de cada paso |
| SBOM completa descargada como artefacto | PENDIENTE: nombre y URL del run |
| Ejercicio 1, escaneo rojo deliberado | PENDIENTE: URL del run e identificación del hallazgo |
| Ejercicio 1, corrección verde | PENDIENTE: URL del run y prueba funcional |
| PR no fusionada para auditar propuesta IA | PENDIENTE: número, URL y captura |
| Dibujo real del grupo | PENDIENTE: foto original realizada por el grupo |
| Práctica de IA controlada (Gandalf) | PENDIENTE: indicar lo observado, no inventar resultado |

## 3. Resultado incorrecto que debe documentarse

Si los escáneres no pueden instalarse, fallan por integridad o hallan una debilidad, **no está todo aprobado**. Agregar enlace de la ejecución roja y explicar cuál fallo técnico o hallazgo debe subsanarse. No borrar reglas ni cambiar la compuerta para obtener verde.
