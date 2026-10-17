# Ejercicio 2: Operación Turno Nocturno (cuatro equipos)

Son cuatro **variantes académicas sin control físico real**. Cada equipo recibe un archivo ficticio, dibuja tres componentes y marca tres riesgos STRIDE. El archivo corregido se conserva como ejemplo seguro; la prueba negativa la generan los controles en un directorio temporal.

| Equipo | Sistema simulado | Defecto didáctico analizado | Tratamiento esperado |
|---|---|---|---|
| 1 · Agua | Lecturas de cloro | Credencial expuesta | Gitleaks y variable de entorno; rotación si fuese real |
| 2 · Energía | Estado de un interruptor | Biblioteca sin versión o vulnerable | OSV, Trivy, versión exacta y prueba funcional |
| 3 · Salud | Registros de monitor ficticio | Dato de paciente en logs | No guardar identificadores personales; usar correlación ficticia |
| 4 · Transporte | Panel de flota ficticio | Regla abierta `0.0.0.0/0` | Trivy config y acceso de red aprobado |

## Cronómetro

- **00–08:** modelar amenazas (dibujar operador → servicio/panel → dispositivo/proceso; marcar límites de confianza, categorizar STRIDE, priorizar tres riesgos).
- **08–22:** ejecutar controles (`Gitleaks`, `Semgrep`, `Trivy`, `OSV`), describir un resultado y corregir o justificar.
- **22–28:** auditar el caso de IA: paquete, entrada, protección y destino de datos.
- **28–30:** cerrar `ENTREGABLE.md` con hechos verificables.

Roles para cinco participantes: operador, desarrollador, guardián de pipeline, auditor de IA y relator. En un grupo de tres, pueden combinarse funciones, nunca eliminar la revisión humana de cambios.
