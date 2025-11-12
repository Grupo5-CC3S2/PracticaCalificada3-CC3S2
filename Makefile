.PHONY: install-deps install-hooks setup test

SHELL := /bin/bash

install-deps:
	python -m pip install --upgrade pip &&\
	python -m venv .venv && \
	echo "Instalando dependencias de python (black, pytest, pytest-cov)..." && \
	source .venv/bin/activate && \
	pip install -r requirements.txt
	@echo "Descargando gitleaks v8.18.4 para Linux"
	curl -L -o gitleaks_8.18.4_linux_x64.tar.gz \
		https://github.com/gitleaks/gitleaks/releases/download/v8.18.4/gitleaks_8.18.4_linux_x64.tar.gz
	tar -xzf gitleaks_8.18.4_linux_x64.tar.gz
	rm gitleaks_8.18.4_linux_x64.tar.gz
	chmod +x gitleaks
	@echo "gitleaks instalado como './gitleaks'"
	@sudo mv gitleaks /usr/local/bin/

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
	@echo "Ejecutando tests con cobertura..."
	pytest

cov-xml-report:
	@echo "Generando reporte XML de cobertura..."
	pytest --cov-report=xml

cov-html-report:
	@echo "Generando reporte HTML de cobertura..."
	pytest --cov-report=html

format:
	@echo "Formateando código python con black..."
	@black tests

format-check:
	@echo "Verificando formato (sin modificar archivos)..."
	@black --check tests --diff