.PHONY: install-deps install-hooks setup test

install-deps:
	@echo "Instalando black (Python formatter)..."
	pip install --user black || pip install black

	@echo "Descargando gitleaks v8.18.4 para Windows"
	curl -L -o gitleaks.exe \
		https://github.com/gitleaks/gitleaks/releases/download/v8.18.4/gitleaks_8.18.4_windows_x64.exe
	chmod +x gitleaks.exe
	@echo "gitleaks instalado como './gitleaks.exe'"

install-hooks:
	@echo "Instalando hooks..."
	mkdir -p .git/hooks
	cp scripts/pre-commit .git/hooks/pre-commit
	cp scripts/commit-msg .git/hooks/commit-msg
	chmod +x .git/hooks/pre-commit .git/hooks/commit-msg
	@echo "Hooks instalados: pre-commit y commit-msg"


setup: install-deps install-hooks
	@echo "Setup completo. ya puede usar git commit"

test:
	pytest