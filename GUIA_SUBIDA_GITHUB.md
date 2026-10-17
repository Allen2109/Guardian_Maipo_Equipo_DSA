# Guía simple para subir el trabajo y evitar el error anterior

**Punto esencial:** el ZIP trae la estructura preparada para que las carpetas se suban DIRECTAMENTE a la raíz del nuevo repositorio.

1. Descarga y descomprime `Guardian_Maipo_Equipo_DSA.zip`.
2. Crea un repositorio nuevo en GitHub. No agregues un README distinto.
3. En GitHub Desktop usa `File → Clone repository` para abrir el repositorio vacío.
4. Copia **el contenido dentro de la carpeta descomprimida**, no la carpeta entera, a la carpeta local del repositorio clonado.
5. GitHub Desktop: revisa cambios, escribe `Entrega inicial Guardian Maipo DSA`, pulsa `Commit to main` y `Push origin`.
6. En la página principal de GitHub comprueba que ves `.github`, `src`, `tests`, `docs`, `ENTREGABLE.md` todos al mismo nivel.
7. En `Actions` ahora deben aparecer tres nombres: `01 - Integracion del simulador`, `02 - Controles DevSecOps`, `03 - Ejercicio 1 rojo a verde`.
8. En `Settings → Secrets and variables → Actions` registra `PLC_PASSWORD` con valor EXCLUSIVAMENTE ficticio.
9. Ejecuta los workflows manualmente. Si aparecen errores, guarda captura y revisa registros; no se debe declarar aprobación anticipada.
10. Copia las URL finales en `evidencias/VALIDACION.md` y en `ENTREGABLE.md` y realiza un commit adicional con la evidencia real.

### Si prefieres subir solo con navegador

Arrastrar carpetas completas puede fallar. GitHub Desktop o Git por consola conserva la estructura, especialmente `.github/workflows/`. El archivo ZIP como una sola carga **no sirve** para que Actions reconozca sus workflows.

### El repositorio original de otro grupo

No copies el ZIP ni las capturas del grupo de referencia dentro de este proyecto: cite su trabajo como fuente en `docs/REFERENCIAS.md` y evidencia únicamente acciones del nuevo equipo.
