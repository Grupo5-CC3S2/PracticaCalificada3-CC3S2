Daren:
- Pensé en hacer dos workflows al inicio, pero me pareción más importante el de testing, linting y cobertura. Así que lo implementé
- Habían algunos errores provenientes del sprint 1, los corregí para poder usarlo en el workflow

Jhon:
- La automatización ya cumple con mover las tarjetas entre estados y asignar estimates según las etiquetas, aunque el parsing de tamaños (S/M/L) aún necesita refinarse.
- Fue necesario crear un token para que las Actions funcionaran correctamente, algunos errores se debieron a diferencias mínimas en los nombres de columnas (por ejemplo, In Progress vs In progress)
- El flujo ya está operativo y reduce bastante la intervención manual
- Aún no se cumplen los cambios en los labels reflejados en los campos en el tablero, pero se intentará para el sprint 3