## Bypass de Emergencia

Solo en crisis reales (sistema caído, deadline crítico).

Pasos:
1. rm -f .git/hooks/pre-commit .git/hooks/commit-msg
2. git commit --no-verify -m "fix(critical): [qué pasó]"
3. make install-hooks

Obligatorio:
- Crear issue: bypass: emergencia [fecha]
- Explicar el motivo

Más detalles: docs/politicas.md