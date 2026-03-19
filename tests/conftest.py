"""Shared pytest fixtures for backend API tests."""

from copy import deepcopy

import pytest
from fastapi.testclient import TestClient

from src.app import activities, app


@pytest.fixture
def client() -> TestClient:
    """Create a FastAPI test client."""
    return TestClient(app)


@pytest.fixture(autouse=True)
def reset_activities_state():
    """Keep tests isolated by restoring activity state after each test."""
    original_state = deepcopy(activities)

    yield

    activities.clear()
    activities.update(deepcopy(original_state))
