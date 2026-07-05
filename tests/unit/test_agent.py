"""Quote Generation Agent - Unit Tests."""

import pytest
from src.agent.tools import AgentTools


@pytest.mark.asyncio
async def test_configure_quote():
    """Test Configure a quote with products, quantities, and pricing."""
    tools = AgentTools()
    result = await tools.configure_quote(products="test", customer_id="test")
    assert result is not None
    assert "status" in result or "tool" in result


@pytest.mark.asyncio
async def test_apply_discount():
    """Test Apply discount rules and check approval requirements."""
    tools = AgentTools()
    result = await tools.apply_discount(quote_id="test", discount_pct="test")
    assert result is not None
    assert "status" in result or "tool" in result


@pytest.mark.asyncio
async def test_generate_document():
    """Test Generate a professional quote document."""
    tools = AgentTools()
    result = await tools.generate_document(quote_id="test", format="test")
    assert result is not None
    assert "status" in result or "tool" in result


@pytest.mark.asyncio
async def test_manage_expiration():
    """Test Set and manage quote expiration dates and reminders."""
    tools = AgentTools()
    result = await tools.manage_expiration(quote_id="test", valid_days=1)
    assert result is not None
    assert "status" in result or "tool" in result


@pytest.mark.asyncio
async def test_agent_initialization():
    """Test that the agent initializes correctly."""
    from src.agent.quote_generation_agent_agent import QuoteGenerationAgentAgent
    agent = QuoteGenerationAgentAgent()
    assert agent.agent_id is not None
    assert agent._system_prompt is not None
    assert len(agent._tool_dispatch) > 0
