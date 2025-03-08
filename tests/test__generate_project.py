import shutil
from pathlib import Path
from typing import (
    Dict,
    Generator,
)

import pytest

from tests.utils.project import generate_project


@pytest.fixture(scope="function")
def project_dir() -> Generator[Path, None, None]:
    template_values: Dict[str, str] = {"repo_name": "test-repo"}
    generated_repo_dir: Path = generate_project(template_values=template_values)
    yield generated_repo_dir
    shutil.rmtree(path=generated_repo_dir)


def test__can_generate_project(project_dir: Path):
    """
    execute: `cookiecutter <template directory> ...`
    """
    assert project_dir.exists()
    assert project_dir.exists()
