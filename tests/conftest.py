"""Test configuration for Quote Generation Agent."""

import pytest


@pytest.fixture
def agent_config():
    return {"name": "quote-generation-agent", "category": "Sales"}
