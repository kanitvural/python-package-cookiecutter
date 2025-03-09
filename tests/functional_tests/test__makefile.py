"""Test makefile."""

import subprocess
from pathlib import Path


def test__linting_passes(project_dir: Path):
    """
    Test that linting passes in a generated project.

    Note: we run linting twice, since we do not mind if automatically-fixable
    errors such as trailing whitespace make it through.

    This makes it easier
    to develop the template, because we often cannot lint the template files
    directly, e.g. when python files contain Jinja2 templating syntax making them
    syntactically invalid python files.
    """
    subprocess.run(["make", "lint-ci"], cwd=project_dir, check=False)


def test__tests_pass(project_dir: Path):
    """Test that the tests pass in a generated project when run on the src/ folder."""
    subprocess.run(["make", "install"], cwd=project_dir, check=True)
    subprocess.run(["make", "test-wheel-locally"], cwd=project_dir, check=True)


# Setup:
# 1. Generate a project using cookiecutter
# 2. Create a virtual environment and install project dependencies

# Tests:
# 3. Run tests
# 4. Run linters

# Clean up/Tear down:
# 5. Remove the virtual environment
# 6. Remove the generated project
