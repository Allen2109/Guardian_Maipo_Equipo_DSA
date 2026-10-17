# Propuesta hipotética de IA para auditar · NO EJECUTAR

Una IA propone sustituir la lectura local por un módulo más rápido. Presenta las siguientes **características descritas**, no código ejecutable en este repositorio:

- incorpora un paquete de nombre `plc_helper_utils` sin demostrar su origen;
- arma una cadena de comandos a partir del identificador de dispositivo recibido;
- intenta ejecutarla con `subprocess.run(..., shell=True)`;
- transmite la respuesta con `requests.post(..., verify=False)`;
- menciona un destino `TELEMETRIA` sin documentación ni autorización.

El objetivo de este documento es **revisar** la propuesta, no instalarla ni fusionarla. Estas prácticas son deliberadamente rechazadas en el proyecto final.

Preguntas: ¿Se verificó el paquete? ¿Qué hace con entradas externas? ¿Desactiva protecciones? ¿Qué datos salen y a qué destino?
