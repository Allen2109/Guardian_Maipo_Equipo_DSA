# Infraestructura didáctica no desplegable: NO define providers ni resources.
variable "red_operacional_de_laboratorio" {
  type        = string
  description = "Red de documentación RFC 5737, no una red de planta"
  default     = "192.0.2.0/24"
}

variable "comunicacion_con_plc_real" {
  type    = bool
  default = false
}
