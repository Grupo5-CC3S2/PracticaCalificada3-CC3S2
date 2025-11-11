#!/bin/bash
# setup_hooks.sh - Instalador 1-click para hooks
mkdir -p .git/hooks
cp scripts/pre-commit .git/hooks/pre-commit
cp scripts/commit-msg .git/hooks/commit-msg
chmod +x .git/hooks/pre-commit .git/hooks/commit-msg
echo "Hooks instalados: pre-commit y commit-msg"
echo "Listo! Usa: git commit"
