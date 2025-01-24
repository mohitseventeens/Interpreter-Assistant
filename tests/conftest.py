"""Pytest configuration and fixtures."""

import pytest
from unittest.mock import AsyncMock, MagicMock
from interpreter_assistant.services.deepgram import DeepgramClient, DeepgramAdapter
from interpreter_assistant.audio_io import AudioCapture, BufferManager

@pytest.fixture
def mock_audio_capture():
    """Mock AudioCapture instance."""
    capture = MagicMock(spec=AudioCapture)
    capture.start = MagicMock()
    capture.stop = MagicMock()
    return capture

@pytest.fixture
def mock_buffer_manager():
    """Mock BufferManager instance."""
    return MagicMock(spec=BufferManager)

@pytest.fixture
def mock_deepgram_client():
    """Mock DeepgramClient instance."""
    client = MagicMock(spec=DeepgramClient)
    client.connect = AsyncMock()
    client.send_audio = AsyncMock()
    client.receive_transcript = AsyncMock()
    client.close = AsyncMock()
    return client

@pytest.fixture
def mock_deepgram_adapter():
    """Mock DeepgramAdapter instance."""
    return MagicMock(spec=DeepgramAdapter)