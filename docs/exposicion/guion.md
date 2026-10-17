# Guion de presentación | 90 segundos, equipo DSA

**Daniel Silva · Allen Ramirez · Antonella Mancilla**

### 0:00–0:30 — Contexto e impacto (Daniel)

«Nuestro trabajo se basa en Maipo Sur, una planta de agua ficticia. Diseñamos un lector local de registros para demostrar que los errores de software no se quedan solo en el computador: si algo parecido llegara a una planta real, podría afectar la supervisión y las decisiones del personal. Por eso priorizamos tres riesgos: contraseñas expuestas, datos manipulados y paneles abiertos.»

### 0:30–1:00 — Controles y decisión (Allen)

«Aplicamos DevSecOps integrando pruebas y análisis antes de cualquier despliegue. Nuestro programa supera doce pruebas locales y revisamos cuatro casos simulados. El repositorio incorpora Gitleaks para buscar secretos, Semgrep para revisar código, Trivy para dependencias y configuración, y OSV para bibliotecas. La evidencia final de las ejecuciones se comprueba en GitHub Actions.»

### 1:00–1:30 — IA y cierre (Antonella)

«Además, auditamos una propuesta generada por IA y decidimos rechazarla. No verificaba el paquete externo, usaba entradas en comandos, desactivaba una protección TLS y enviaba datos a un destino no justificado. Nuestra conclusión es que la IA puede ayudar, pero el equipo debe comprobar y autorizar cualquier cambio antes de acercarlo a un servicio esencial.»

**Al exponer:** mostrar el diagrama, las pruebas reales y la ficha. Si GitHub Actions aún falla, informar con precisión el hallazgo; nunca fingir verde ni capturas de ejecuciones.
