# Políticas de Seguridad

## 1. Secretos
- Usamos gitleaks v8.18.4
- Se ejecuta en cada commit
- Si encuentra algo, avisa (no bloquea en S1)
- Nunca subas claves, tokens o contraseñas

## 2. Commits
- Deben seguir Conventional Commits
- Ejemplo: feat(setup): agregar hooks
- Validado por scripts/commit-msg

## 3. Archivos grandes
- Máximo 10 MB
- Se avisa si hay archivos grandes

## 4. Bypass de Emergencia (solo en crisis)

Solo si el sistema está caído o hay deadline urgente.

Pasos:
1. Borrar hooks:
   rm -f .git/hooks/pre-commit .git/hooks/commit-msg

2. Commit rápido:
   git commit --no-verify -m "fix(critical): arreglar error grave"

3. Restaurar hooks:
   make install-hooks

4. Crear issue:
   Título: bypass: emergencia 2025-11-11
   Explicar por qué fue necesario

Solo el dueño del repo puede hacerlo.
Todos los bypass quedan en el historial.