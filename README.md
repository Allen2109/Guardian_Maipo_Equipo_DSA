# Guardian Maipo | Taller DevSecOps para infraestructura crítica

**Universidad Bernardo O'Higgins · Laboratorio académico**  
**Equipo:** **Daniel Silva**, **Allen Ramirez** y **Antonella Mancilla**  
**Fecha de preparación:** 16 de octubre de 2026  
**Caso base:** Maipo Sur, planta ficticia de agua potable.

> ⚠️ **Simulación únicamente.** No hay control real de cloro, sensores, PLC, HMI, servicios hospitalarios, energía, redes ni transportes. Los valores y las direcciones pertenecen al laboratorio; no son recomendaciones de operación sanitaria.

## ¿Qué construimos?

`Guardian Maipo` es un lector de mediciones inventadas diseñado para demostrar seguridad integrada en el desarrollo. No es una copia del código de referencia: usa un paquete Python nuevo, validación de datos, cuatro conjuntos ficticios de escenarios, doce pruebas y pipelines independientes para integración, análisis y ejercicio de Gitleaks.

El programa recibe el identificador `SENS-001`, consulta `escenarios/agua/lecturas.json`, valida la lectura y solo entrega un objeto informativo. Exige `PLC_PASSWORD` desde el entorno, sin guardar ni imprimir su valor.

## Lo principal para el profesor

| Requisito | Dónde está |
|---|---|
| Sistema, participantes y roles | [ENTREGABLE.md](ENTREGABLE.md) |
| Diagrama con fronteras de confianza | [Arquitectura](docs/arquitectura/diagrama.svg), [editable Mermaid](docs/arquitectura/diagrama.mmd) |
| Tres amenazas STRIDE priorizadas | [Modelo de amenazas](docs/amenazas/analisis.md) |
| Código, dependencias e infraestructura | `.github/workflows/seguridad.yml` |
| Ejercicio 1, rojo → verde | `.github/workflows/ejercicio-1.yml`, [guía](docs/actividad-ia/ejercicio-1.md) |
| Auditoría del parche propuesto por IA | [Veredicto](docs/auditoria-ia/veredicto.md) |
| Informe para presentar | [Informe PDF](reportes/Informe_Guardian_Maipo.pdf) |
| Criterios 100 puntos | [Rúbrica](docs/rubrica/matriz.md) |
| Evidencias reales / pendientes | [Validación](evidencias/VALIDACION.md) |
| Guion de cierre 90 s | [Exposición](docs/exposicion/guion.md) |

## Estructura sin carpetas anidadas

```text
.github/workflows/    <- Obligatorio en la raiz de GitHub
src/guardian_maipo/   <- Programa NUEVO: entrada validada, datos simulados
tests/                 <- 12 pruebas unitarias
escenarios/            <- Agua, energia, salud, transporte
infra/                 <- Modelo estatico, no desplegable
policies/              <- Regla de acceso al panel ficticio
scripts/               <- Verificacion y artefactos
herramientas (tools/)  <- Binarios de escaneo fijados por versión y SHA-256
docs/                  <- Diagramas, riesgos, auditoría y exposición
evidencias/             <- Registro honesto y SBOM local
reportes/               <- Informe PDF de evaluación
ENTREGABLE.md           <- Ficha de blindaje
```

## 1. Prueba local rápida (Python 3.12)

Ejecutar en la raíz del proyecto:

```bash
python -m pip install --require-hashes -r requirements.lock
PYTHONPATH=src python -m unittest discover -s tests -v
python scripts/revisar_sectores.py
python scripts/compilar.py
```

En Windows PowerShell, sustituir la línea de tests por:

```powershell
$env:PYTHONPATH="src"; python -m unittest discover -s tests -v
```

Para probar la lectura, usar **solo un valor ficticio de laboratorio** suministrado a través del entorno; no pegar credenciales reales en archivos ni en capturas:

```powershell
$env:PYTHONPATH="src"; $env:PLC_PASSWORD="SOLO-DEMO"; python -m guardian_maipo --sensor SENS-001
```

La lectura ficticia de 0.70 mg/L no es un umbral sanitario ni una recomendación de dosificación.

## 2. Cómo ejecutar el taller en GitHub

1. Crea un repositorio nuevo (por ejemplo, `guardian-maipo-dsa`) y sube **el contenido de este ZIP a la raíz**. El repositorio debe mostrar `.github`, `src`, `tests`, `docs` y `ENTREGABLE.md` al mismo nivel.
2. Comprueba que GitHub muestra **Actions**: `01 - Integracion del simulador`, `02 - Controles DevSecOps`, `03 - Ejercicio 1 rojo a verde`.
3. Configura en `Settings → Secrets and variables → Actions` el secreto `PLC_PASSWORD` con **un valor ficticio**. No usar la contraseña de sistemas reales.
4. Ejecuta `03 - Ejercicio 1 rojo a verde` con `escenario=fallo`: debe aparecer una ejecución roja **intencionada** que demuestra detección del secreto generado en una carpeta temporal del runner.
5. Vuelve a ejecutarlo con `escenario=corregido`: debe quedar verde si el secreto ficticio está configurado. No modifica archivos reales ni elimina reglas.
6. Comprueba las ejecuciones de `01` y `02`. Los informes de seguridad y la SBOM completa, cuando los escáneres concluyan, se descargan desde **Artifacts**.
7. Copia las URL y una captura de los resultados **reales** a [evidencias/VALIDACION.md](evidencias/VALIDACION.md), incluida la PR de auditoría de IA si la creas.

**Si una ejecución falla por permisos, herramientas o versiones, documenta el fallo y corrígelo. No afirmes que funcionó ni desactives controles para obtener verde.**

## 3. Ejercicio en equipos (30 minutos)

Cada equipo modela tres riesgos, ejecuta controles, documenta su decisión y rechaza o acepta razonadamente el parche académico de IA. Hay guías para [agua, energía, salud y transporte](escenarios/GUIA_EQUIPOS.md). Distribución por fases: 8 minutos para modelar, 14 para controles, 6 para revisar IA y 2 para cerrar la ficha.

## 4. Auditoría de la IA

La propuesta escrita en [docs/auditoria-ia/caso-propuesto.md](docs/auditoria-ia/caso-propuesto.md) es texto para analizar, **no código para instalar o ejecutar**. Se evalúan cuatro preguntas: origen del paquete, manejo de entradas, protecciones desactivadas y destino de datos. La decisión es humana.

Para presentar una PR didáctica, crea una rama `propuesta-ia-revision`, agrega un documento explicativo del cambio propuesto y abre una PR hacia `main`. **No fusiones código inseguro**. La revisión escrita está lista; el número y URL de la PR deben completarse desde GitHub.

## 5. Atribución y honestidad de evidencias

Este proyecto académico se diseñó a partir de la **presentación y guía DevSecOps del profesor** y toma como referencia temática el repositorio público de Miguel Briceño (`miguelbriceno-sys/Taller-de-infraestructura-critica`), sin atribuir al nuevo equipo actividades hechas por sus autores. La implementación, la organización y el informe fueron redactados de nuevo. Véase [fuentes](docs/REFERENCIAS.md).

Las **12 pruebas unitarias y cuatro comprobaciones de sectores** sí fueron ejecutadas en este entorno al preparar el paquete. **No se afirma** que GitHub Actions, la práctica Gandalf o una pull request hayan sido ejecutadas por Daniel, Allen y Antonella antes de aportar evidencia real.
