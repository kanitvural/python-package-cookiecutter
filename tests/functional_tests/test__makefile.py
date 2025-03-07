import subprocess
from pathlib import Path


def test__linting_passes(project_dir: Path):
    subprocess.run(["make", "lint-ci"], cwd=project_dir, check=True)


def test__tests_pass(project_dir: Path):
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
