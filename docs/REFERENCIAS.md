# Fuentes y procedencia

## Documentación base proporcionada por el curso

- *Taller DevSecOps sobre Infraestructura Crítica*, presentación del profesor, Universidad Bernardo O'Higgins, octubre de 2026.
- *Guía del facilitador: Taller DevSecOps sobre Infraestructura Crítica, v2*, documento de apoyo, 7 de octubre de 2026.

## Proyecto de referencia consultado

- Miguel Briceño y equipo, repositorio académico `https://github.com/miguelbriceno-sys/Taller-de-infraestructura-critica` y material de apoyo compartido por el usuario. Se utilizó para comprender los tipos de entregables y técnicas aplicables; **no se declaran sus ejecuciones de CI, fotografías, capturas, fechas ni autoría como propias**.

## Herramientas técnicas

- GitHub Actions: https://docs.github.com/en/actions
- Gitleaks: https://github.com/gitleaks/gitleaks
- Semgrep OSS: https://semgrep.dev/docs/
- Trivy: https://trivy.dev/
- OSV-Scanner: https://google.github.io/osv-scanner/
- CycloneDX: https://cyclonedx.org/
- OWASP Threat Modeling: https://owasp.org/www-community/Threat_Modeling
- NIST SP 800-82 Rev. 3: guía de seguridad de tecnología operativa.
- NIST SP 800-218 (SSDF): marco de desarrollo seguro.
- IEC 62443-4-1: ciclo de vida seguro industrial.
- Ley chilena 21.663: Ley Marco de Ciberseguridad.

## Precaución de versiones

El laboratorio bloquea versiones de las herramientas binarias y registra un SHA-256 de descarga. Esas huellas se tomaron del manifiesto de referencia del taller y deberán contrastarse con los artefactos oficiales cuando se actualicen. No se usa la versión de Trivy marcada como comprometida en la guía. El instalador comprueba las huellas y falla si no coinciden.
