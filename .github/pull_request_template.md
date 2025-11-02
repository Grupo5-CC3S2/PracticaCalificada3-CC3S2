## Cambios realizados
Describe brevemente qué cambia este PR, riesgos potenciales, y si requiere bypass temporal de algún hook.

## Checklist

**Vinculación y formato**
- [ ] Commits siguen [Conventional Commits](https://www.conventionalcommits.org)
- [ ] PR vinculado al issue: `Fixes #N`
- [ ] Título claro y descriptivo

**Calidad y pruebas**
- [ ] Lint y tests verdes (`pytest -vv --cov`)
- [ ] Cobertura ≥85%
- [ ] No se introducen secretos (.env, claves, tokens)
- [ ] Patrones/DIP aplicados (facade, adapter, ports)

**Impacto en tablero**
- [ ] Tarjeta movida a `Review-QA`
- [ ] Estimate actualizado en GitHub Project


## Políticas de Seguridad

| Categoría | Política | Cumple |
|------------|-----------|--------|
| **Puertos** | Ningún puerto adicional abierto sin aprobación del equipo | [ ] |
| **Secretos** | Ningún secreto expuesto en código, PR o .env | [ ] |
| **Licencias** | Solo dependencias con licencia compatible (MIT, Apache-2.0, BSD) | [ ] |
| **Tamaño de artefactos** | No subir binarios >10 MB al repo | [ ] |
| **Revisión cruzada** | ≥1 aprobación (≥2 si módulo sensible) | [ ] |
| **IaC drift** | 0 % drift documentado entre `plan` consecutivos | [ ] |
| **Conformidad CI** | CI verde (lint, tests, cobertura, secretos, IaC) | [ ] |


