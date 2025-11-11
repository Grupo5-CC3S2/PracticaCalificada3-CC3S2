import subprocess
import pytest
from pathlib import Path
import os
import shutil

def _command_exists(cmd):
    """Helper para verificar si un comando está disponible."""
    return shutil.which(cmd) is not None

@pytest.fixture(autouse=True)
def remove_commit_msg_hook(temp_repo):
    """Borra el hook pre-commit antes de cada test (depende de temp_repo para GIT_DIR)."""
    git_dir = Path(os.getenv("GIT_DIR"))
    pre_commit_hook = git_dir / "hooks" / "commit-msg"
    
    # Borrar el hook si existe
    if pre_commit_hook.exists():
        pre_commit_hook.unlink()
    
    yield

@pytest.mark.skipif(not _command_exists("black"), reason="black no está instalado")
def test_pre_commit_invalid_format (temp_repo):
    # Crear script de python con error de formato (indentacion invalida)
    (temp_repo / "example.py").write_text("  import os")

    subprocess.run(["git", "add", "."])
    result = subprocess.run(["git", "commit", "-m", "ejemplo"], capture_output=True, text=True)
    
    print (result)

    assert result.returncode == 1
    assert "formato incorrecto" in result.stdout.lower() or result.stderr.lower()

@pytest.mark.skipif(not _command_exists("black"), reason="black no está instalado")
def test_pre_commit_valid_format (temp_repo):
    # Crear script de python con formato valido
    (temp_repo / "example.py").write_text(
        'def suma(a, b):\n'
        '    return a + b\n'
        '\n'
        '\n'
        'print(suma(1, 2))\n'
    )

    subprocess.run(["git", "add", "."])
    result = subprocess.run(["git", "commit", "-m", "ejemplo"], capture_output=True, text=True)
    
    print (result)

    assert result.returncode == 0
    assert "All done!" in result.stdout.lower() or result.stderr.lower()

@pytest.mark.skipif(not _command_exists("gitleaks"), reason="gitleaks no está instalado")
def test_pre_commit_pass_no_secrets(temp_repo):
    # Crear un archivo sin secretos
    (temp_repo / "safe_file.txt").write_text("Este es un contenido seguro.")
    
    subprocess.run(["git", "add", "."])
    result = subprocess.run(["git", "commit", "-m", "ejemplo"], capture_output=True, text=True)
    
    print (result)

    assert result.returncode == 0
    assert "no leaks found" in result.stdout.lower() or result.stderr.lower()

@pytest.mark.skipif(not _command_exists("gitleaks"), reason="gitleaks no está instalado")
def test_pre_commit_fail_with_secrets(temp_repo):
    # Crear un archivo con un secreto que gitleaks pueda detectar
    # Usamos un formato comun para claves de AWS
    (temp_repo / "credentials.env").write_text("AWS_ACCESS_KEY_ID = AKIAJVWFRSSWQP3A7EXA")
    
    subprocess.run(["git", "add", "."])
    result = subprocess.run(["git", "commit", "-m", "ejemplo"], capture_output=True, text=True)
    
    print (result)

    assert result.returncode == 1
    assert "leaks found: " in result.stdout.lower() or result.stderr.lower()

def test_pre_commit_detects_large_file(temp_repo):
    # Crear archivo lo suficientemente grande para que el hook detecte
    large_file = temp_repo / "large_file"
    with open(large_file, "wb") as f:
        f.seek(11 * 1024 * 1024)  # 11MB
        f.write(b'\0')

    subprocess.run(["git", "add", "."])
    result = subprocess.run(["git", "commit", "-m", "ejemplo"], capture_output=True, text=True)

    print (result)
    
    assert result.returncode == 1
    assert "archivos >10mb" in result.stdout.lower() or result.stderr.lower()
    assert "large_file" in result.stdout.lower () or result.stderr.lower()