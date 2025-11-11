Daren:
- Los tests se implementaron medianamente de acuerdo a lo que se pidió. No se pudo hacer uso de stubs de comandos de git debido a que no encontré forma de hacerlo que involucrara usar los hooks.
- Hubieron algunos errores con los hooks que ya se habían implementado por mi compañero, lo solucionaré en el srpint 2
- No hubo ningun bloqueo
- Probablemente los tests no sean lo más eficientes posibles debido a que el repositorio se crea en cada test, pero fue la forma más simple de no tener dependencias entre los diferentes tests.

Jhon:
- Detecté que las políticas de los hooks tienen huecos y es sorprendentemente fácil hacerles bypass sin intención. Eso dejó claro que hay que reforzar varias validaciones.
- La ejecución de los hooks no es estable: en ciertos casos bloquean cambios que deberían permitir y, en otros, dejan pasar commits que deberían detener. Ahí hay lógica que ajustar.
- No tuve bloqueos reales