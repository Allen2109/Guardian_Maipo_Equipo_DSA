# METADATA
# title: Prohibir panel simulado expuesto globalmente
# description: Solo se permiten origenes de laboratorio, nunca origen global.
# custom:
#   id: MAIPO-NET-001
#   severity: CRITICAL
#   recommended_actions: Restringir acceso a una red aprobada.
#   input:
#     selector:
#     - type: yaml
package user.maipo.MAIPONET001

deny[msg] {
  input.sistema == "panel-operacional-laboratorio"
  input.origenes_permitidos[_] == "0.0.0.0/0"
  msg := "El panel ficticio no puede quedar disponible desde cualquier origen"
}
