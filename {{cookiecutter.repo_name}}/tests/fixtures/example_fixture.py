"""Example fixture."""

from uuid import uuid4

import pytest

from tests.constants import PROJECT_DIR


@pytest.fixture(scope="session")
def test_session_id() -> str:
    """It generates test session id."""
    test_session_id = str(PROJECT_DIR) + str(uuid4())[:6]
    return test_session_id
