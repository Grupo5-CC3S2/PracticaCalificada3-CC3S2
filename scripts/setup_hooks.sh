#!/bin/bash
# setup_hooks.sh: copia hooks a .git/hooks
cp scripts/pre-commit .git/hooks/pre-commit
chmod +x .git/hooks/pre-commit
cp scripts/commit-msg .git/hooks/commit-msg
chmod +x .git/hooks/commit-msg
echo "Hooks instalados"