import pytest


@pytest.fixture
def server_info() -> dict:
    return {
        "status": 200,
        "message": "Welcome to the Evolution API, it is working!",
        "version": "1.7.4",
        "swagger": "http://example.evolution-api.com/docs",
        "manager": "http://example.evolution-api.com/manager",
        "documentation": "https://doc.evolution-api.com",
    }
