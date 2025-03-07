import pytest


@pytest.fixture(scope="session")
def project():
    print("Setup")
    yield 1
    print("Teardown")


def test__linting_passes(project):
    print(project)
    assert False


def test__tests_pass(): ...


def test__install_succeeds(): ...


# Setup:
# 1. Generate a project using cookiecutter
# 2. Create a virtual environment and install project dependencies

# Tests:
# 3. Run tests
# 4. Run linters

# Clean up/Tear down:
# 5. Remove the virtual environment
# 6. Remove the generated project
# 6. Remove the generated project
