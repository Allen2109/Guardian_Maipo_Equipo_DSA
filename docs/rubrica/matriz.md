# Matriz de trazabilidad de la rúbrica de 100 puntos

Esta tabla indica **dónde está preparado cada criterio** y **qué no puede darse por aprobado hasta ver GitHub**.

| Criterio del PPT | Máximo | Archivos | Evidencia que falta comprobar |
|---|---:|---|---|
| Modelado de amenazas y efecto físico | 25 | `ENTREGABLE.md`, `docs/amenazas/analisis.md`, diagrama | Foto del dibujo realizada por el equipo |
| Controles automáticos reales | 25 | `.github/workflows/{integracion,seguridad,ejercicio-1}.yml`, `.gitleaks.toml`, `.semgrep.yml`, `policies/` | URL de runs reales: una falla intencional y otra corrección, reporte de escáneres |
| Gestión de hallazgos justificada | 20 | Tabla de `ENTREGABLE.md`, `docs/amenazas/analisis.md` | Nombre definitivo de responsables y fechas reales |
| Auditoría de parche IA | 20 | `docs/auditoria-ia/caso-propuesto.md` y `veredicto.md` | URL de PR de revisión no fusionada y constatación de cuatro preguntas |
| Claridad de exposición | 10 | `docs/exposicion/guion.md` | Exposición presencial del relator |

**Bonificaciones del PPT:** fijación por SHA (las acciones usadas están fijadas por commit), SBOM (local creada, remota por verificar), ayuda a otros equipos (no documentada). No se anuncian puntos adicionales automáticos.

**Penalización:** obtener verde silenciando o eliminando reglas es incorrecto. La compuerta de `seguridad.yml` recopila fallos, genera informes y falla si cualquier análisis obligatorio falla.
