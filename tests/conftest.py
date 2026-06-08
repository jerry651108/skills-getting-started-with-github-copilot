import copy

import pytest
from fastapi.testclient import TestClient

from src import app as app_module

_BASE_ACTIVITIES = copy.deepcopy(app_module.activities)


@pytest.fixture(autouse=True)
def reset_activities():
    """Reset in-memory activities before each test for isolation."""
    app_module.activities.clear()
    app_module.activities.update(copy.deepcopy(_BASE_ACTIVITIES))
    yield


@pytest.fixture
def client():
    return TestClient(app_module.app)
