import os
import subprocess
import pytest
from pathlib import Path
import shutil

# Fixture para repositorio temporal
@pytest.fixture
def temp_repo(tmp_path, monkeypatch):
    # Crear repositorio temporal
    repo = tmp_path / "repo"
    repo.mkdir()

    # Monkeypatch GIT_DIR
    git_dir = repo / ".git"
    monkeypatch.setenv("GIT_DIR", str(git_dir))

    cwd = os.getcwd()
    os.chdir(repo)
    try:
        # Configuración minima del repositorio temporal
        subprocess.run(["git", "init"], check=True)
        subprocess.run(["git", "config", "user.email", "test@example.com"], check=True)
        subprocess.run(["git", "config", "user.name", "Test User"], check=True)
        
        # Instalar el hook pre-commit en .git/hooks/pre-commit del repositorio temporal
        # para que git lo ejecute automáticamente durante 'git commit'
        hooks_dir = git_dir / "hooks"
        hooks_dir.mkdir(exist_ok=True)
        project_root = Path(__file__).resolve().parents[1]
        src_hook = project_root / "scripts" / "pre-commit"
        if src_hook.exists():
            dest_hook = hooks_dir / "pre-commit"
            shutil.copy2(src_hook, dest_hook)
            os.chmod(dest_hook, 0o755)
        
        # Instalar el hook commit-msg en .git/hooks/commit-msg del repositorio temporal
        src_commit_msg = project_root / "scripts" / "commit-msg"
        if src_commit_msg.exists():
            dest_commit_msg = hooks_dir / "commit-msg"
            shutil.copy2(src_commit_msg, dest_commit_msg)
            os.chmod(dest_commit_msg, 0o755)
    except Exception:
        # git no disponible en este entorno; continuar sin inicializar
        pass
    yield repo
    os.chdir(cwd)