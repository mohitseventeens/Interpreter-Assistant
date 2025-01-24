"""Tests for Deepgram integration components."""

import pytest
from unittest.mock import AsyncMock
from interpreter_assistant.services.deepgram import DeepgramClient, DeepgramAdapter

@pytest.mark.asyncio
async def test_deepgram_client_connect():
    """Test WebSocket connection establishment."""
    client = DeepgramClient("test_key")
    client.connection = AsyncMock()
    
    await client.connect()
    client.connection.connect.assert_called_once()

@pytest.mark.asyncio
async def test_deepgram_adapter_format_transcript():
    """Test transcript formatting."""
    adapter = DeepgramAdapter()
    response = {
        "is_final": True,
        "start": 0.0,
        "duration": 1.0,
        "channel": {
            "alternatives": [{"transcript": "test"}]
        }
    }
    
    result = adapter.format_transcript(response)
    assert result == "[00:00:00 - 00:00:01] test"