# Modelo de amenazas STRIDE | Maipo Sur

**Alcance:** operador, panel HMI representado, lector local, controlador ficticio y un asistente de IA representado, no desplegado. **Activos:** integridad de la lectura, credencial del servicio, trazabilidad, continuidad de supervisión.

## Flujo y fronteras de confianza

```text
[Operador] ─F1─> [HMI simulado] ─F2─> [Servicio local] ─F3─> [PLC solo modelo]
                                                  ^
                                                  | F4 (consulta de IA sin credenciales)
                                           [Asistente conceptual]
```

La separación representada evita que una modificación de código o instrucción de IA se convierta automáticamente en una orden al proceso. **La única pieza funcional del laboratorio es el servicio local que lee JSON.**

## Tres prioridades (escala ilustrativa de 1 a 3)

`riesgo = probabilidad x impacto`, escala orientativa académica; no es evaluación real de planta.

| ID | Flujo | STRIDE | Amenaza | P x I | Impacto físico si existiera conexión real | Control |
|---|---|---|---|---:|---|---|
| A1 | F1/F3 | S, I | Secreto expuesto permite suplantar al operador | 3×3 = 9 | Orden no autorizada, pérdida de supervisión | Secretos fuera del código, Gitleaks, mínimo privilegio |
| A2 | F2 | T, E | Dato manipulado utilizado como comando | 3×3 = 9 | Lectura alterada y respuesta operativa inadecuada | Semgrep y validación estricta, sin shell |
| A3 | F1/F3 | I, D, E | Acceso abierto al panel | 2×3 = 6 | Disponibilidad afectada, pérdida de supervisión | Trivy config y control de red MAIPO-NET-001 |

## Riesgos adicionales identificados

| ID | STRIDE | Posible riesgo | Respuesta |
|---|---|---|---|
| A4 | T | Archivo de lecturas modificado | Integridad de archivos y control de versiones; falta firma de origen |
| A5 | R | Falta de registro sobre quién modificó el sistema | Auditoría y revisión de PR; control de identidad pendiente |
| A6 | T, E | Dependencias modificadas y vulnerables | OSV, Trivy, lock y lista de componentes |
| A7 | I | Extracción de datos por prompt injection | IA conceptual sin secretos, sin permisos de actuación |
| A8 | D | Indisponibilidad por consultas excesivas | Límites y pruebas de carga futuras |
| A9 | T | Cambios directos en main sin revisión | Pull requests, checks y protección de rama |
| A10 | D | Despliegue sin plan de reversión | Ventana de mantención y rollback antes de usar equipos reales |

## Método y decisiones

Se siguieron las cuatro preguntas: qué construimos, qué puede fallar, cómo lo prevenimos y cómo verificamos. Priorizamos las **consecuencias sobre la continuidad del servicio** antes que la facilidad técnica de un arreglo. Se evaluaron las seis categorías STRIDE: suplantación, manipulación, repudio, divulgación, denegación y elevación de privilegios.
