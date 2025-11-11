import subprocess
import pytest
from pathlib import Path
import os

@pytest.fixture(autouse=True)
def remove_pre_commit_hook(temp_repo):
    """
    Fxiture para borrar el hook pre-commit antes de cada test (depende temp_repo para GIT_DIR)
    """
    git_dir = Path(os.getenv("GIT_DIR"))
    pre_commit_hook = git_dir / "hooks" / "pre-commit"
    
    # Borrar el hook si existe
    if pre_commit_hook.exists():
        pre_commit_hook.unlink()
    
    yield

@pytest.mark.parametrize("message", [
    "feat(ejemplo): mensaje correcto",
    "fix(ejemplo): good msg",
    "test(ejemplo): buen mensaje"
])
def test_commit_msg_valid(temp_repo, message):
    # Crear un archivo para commitear
    (temp_repo / "README.md").write_text("Contenido válido")

    subprocess.run(["git", "add", "."])
    result = subprocess.run(["git", "commit", "-m", message], capture_output=True, text=True)

    assert result.returncode == 0
    assert "correcto" in result.stdout.lower() or "correcto" in result.stderr.lower()

@pytest.mark.parametrize("message", [
    "mal mensaje",
    "BaD meSsage",
    "hola(ejemplo): no es buen mensaje"
])
def test_commit_msg_invalid(temp_repo, message):
    # Crear un archivo para commitear
    (temp_repo / "README.md").write_text("Contenido válido")

    subprocess.run(["git", "add", "."])
    result = subprocess.run(["git", "commit", "-m", message], capture_output=True, text=True)

    assert result.returncode == 1
    assert "error" in result.stdout.lower() or "error" in result.stderr.lower()