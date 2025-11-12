## Registrar deuda técnica y lecciones aprendidas

### Deuda técnica

| ID | Descripción | Impacto | Prioridad |
|----|-------------|---------|-----------|
| DT-01 | El parseo de etiquetas `size:*` en el job **Actualizar Estimate por label size** asume que solo existen `size:S`, `size:M` y `size:L`. Cualquier otra etiqueta (p.ej. `size:XL` o errores tipográficos) es ignorada sin feedback. | Estimaciones incorrectas en el tablero de proyecto. | Alta |
| DT-02 | El job **Registrar Blocked time** concatena fechas sin validar que el campo “Blocked time” ya contenga entradas duplicadas o sin orden cronológico. | Registro ilegible y cálculo manual de tiempo bloqueado. | Media |
| DT-03 | Los nombres de los estados del proyecto son sensibles a mayúsculas/minúsculas (`In progress` vs `In Progress`). El script usa valores hard-codeados, lo que genera fallos cuando el nombre real difiere. | Tarjetas no se mueven al estado esperado. | Alta |
| DT-04 | El workflow depende de un **secret** `PROJECT_TOKEN` con permisos amplios (`organization.projects: write`, `issues: write`, `pull-requests: write`). No se implementa rotación ni alcance mínimo. | Riesgo de exposición de permisos excesivos. | Media |
| DT-05 | Búsqueda de ítems en el proyecto limitada a `first: 100`. Repositorios con >100 ítems abiertos no serán procesados completamente. | Automatización parcial en proyectos grandes. | Baja |

### Lecciones aprendidas

1. **Nomenclatura consistente** – Los nombres de columnas/estados deben definirse en una única fuente de verdad (p.ej. variable de entorno o constante en el script) para evitar errores por diferencias de capitalización o espacios.
2. **Manejo robusto de etiquetas** – Validar la existencia de la etiqueta esperada y devolver un mensaje de error claro en el log del Action cuando no coincida.
3. **Paginación en GraphQL** – Implementar `after` cursor para consultas que puedan superar los 100 ítems.
4. **Alcance mínimo de tokens** – Usar permisos granulares (`repo`, `project`) y rotar el token periódicamente.
5. **Feedback explícito** – Incluir `core.setFailed` o comentarios en el PR cuando una acción falla por configuración, facilitando la depuración rápida del equipo.