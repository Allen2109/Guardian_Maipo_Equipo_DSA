# Ejercicio 1 | El secreto que no debe quedar en el código

## Objetivo (15 minutos)

Comprobar que un escáner detecta una credencial **ficticia** incluida en un archivo temporal y que la corrección deja de activar la alarma sin desactivar reglas.

1. Copiar el proyecto a un repositorio propio (o emplear la copia del taller).
2. Activar `Actions` y localizar `03 - Ejercicio 1 rojo a verde`.
3. Ejecutar con `escenario = fallo`. La acción crea **solo en el runner** un archivo de laboratorio inseguro, lo revisa y debe terminar **roja**. No se publica ninguna contraseña en commits.
4. En `Settings → Secrets and variables → Actions`, crear `PLC_PASSWORD` usando un **valor ficticio** exclusivo para el taller. El nombre del secreto queda visible, no su contenido.
5. Ejecutar el mismo workflow con `escenario = corregido`: se crea un archivo con `password_env: PLC_PASSWORD`. El análisis debe terminar **verde** y el lector debe funcionar sin revelar el valor.
6. Abrir los registros y anotar el nombre del archivo, la regla, la decisión y el enlace real en `evidencias/VALIDACION.md`.

## Por qué es equivalente al ejercicio en el PPT

La demostración enseña la misma transición **fallo detectado → secreto separado del código → análisis correcto**. La diferencia metodológica es que no guardamos deliberadamente una contraseña, aunque sea ficticia, en `main`; el caso se crea temporalmente en GitHub Actions para mantener la rama principal apta para controles continuos.

## Extensión para enseñar cambios de Git

Si el facilitador necesita mostrar un commit antes y otro después, puede ejecutar el ejercicio en una **copia de práctica**, con un valor ficticio, revisar el fallo, corregir `config.yaml` y rotar el valor simulado. El análisis de historia completa se explica como actividad avanzada: borrar la línea del estado actual NO borra los commits anteriores.

## Práctica adicional sobre IA

La presentación propone Gandalf de Lakera como juego de inyección de instrucciones. **Actividad por realizar:** visitar el laboratorio autorizado, intentar comprender los límites de sus defensas y registrar una captura o un comentario sobre lo observado. **No se atribuye ningún nivel completado** a este equipo sin evidencia de su propia práctica.
