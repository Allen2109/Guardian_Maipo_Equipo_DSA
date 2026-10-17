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
| Repositorio nuevo | [Guardian_Maipo_Equipo_DSA](https://github.com/Allen2109/Guardian_Maipo_Equipo_DSA); rama `main` |
| Integración en GitHub Actions | **Aprobada** para commit `4a47309` según captura del equipo. **Pendiente:** URL específica y captura anexada en `evidencias/`. |
| Seguridad: Gitleaks, Semgrep, Trivy, OSV | **Workflow aprobado** para commit `4a47309` según captura del equipo. **Pendiente:** URL específica y comprobación detallada de cada paso mediante los reportes publicados. |
| SBOM completa descargada como artefacto | Se observó artefacto de reportes en una ejecución anterior. **Pendiente:** confirmar SBOM descargada de la ejecución final y enlazarla. |
| Ejercicio 1, escaneo rojo deliberado | **Confirmado por captura:** Gitleaks mostró `leaks found: 1` y `exit code 1` para el caso ficticio. **Pendiente:** URL del run y captura guardada. |
| Ejercicio 1, corrección verde | **Aprobado:** [ejecución #3, 16-10-2026, commit `4a47309`](https://github.com/Allen2109/Guardian_Maipo_Equipo_DSA/actions/runs/38987814463). Captura recibida muestra `Success`, 11 segundos. La ejecución corregida requiere `PLC_PASSWORD` configurado como secreto del repositorio; no publicar su valor. |
| PR no fusionada para auditar propuesta IA | PENDIENTE: número, URL, captura y veredicto documentado |
| Dibujo real del grupo | PENDIENTE: foto original realizada por el grupo |
| Práctica de IA controlada (Gandalf) | PENDIENTE: indicar lo observado, no inventar resultado |

## 3. Resultado incorrecto que debe documentarse

Si los escáneres no pueden instalarse, fallan por integridad o hallan una debilidad, **no está todo aprobado**. Agregar enlace de la ejecución roja y explicar cuál fallo técnico o hallazgo debe subsanarse. No borrar reglas ni cambiar la compuerta para obtener verde.

## 4. Cronología del ejercicio de detección y corrección

- **Rojo previsto:** el escáner Gitleaks detectó un secreto *ficticio* en un archivo temporal de laboratorio. El análisis se detuvo deliberadamente; esto es una detección correcta, no un defecto sin resolver. **URL pendiente.**
- **Primer intento de corrección:** Gitleaks pasó, pero la prueba funcional se detuvo porque faltaba `PLC_PASSWORD` en el entorno. Se solucionó configurando el secreto de GitHub; este fallo intermedio no debe confundirse con una vulnerabilidad. **URL pendiente.**
- **Verde comprobado:** ejecución [38987814463](https://github.com/Allen2109/Guardian_Maipo_Equipo_DSA/actions/runs/38987814463), commit `4a47309`, escenario corregido, `Success` (según captura del equipo).

**Importante:** los estados se basan en las capturas compartidas y en la URL facilitada por el equipo. Los otros enlaces y descargas no han sido verificados externamente desde esta sesión.
