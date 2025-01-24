"""Tests for CLI entrypoint."""

import pytest
from unittest.mock import AsyncMock, MagicMock
from interpreter_assistant.entrypoints import cli

@pytest.mark.asyncio
async def test_main_flow(mocker):
    """Test main transcription flow."""
    # Mock dependencies
    mock_capture = MagicMock()
    mock_client = MagicMock()
    mock_adapter = MagicMock()
    
    # Patch imports
    mocker.patch("interpreter_assistant.entrypoints.cli.AudioCapture", return_value=mock_capture)
    mocker.patch("interpreter_assistant.entrypoints.cli.DeepgramClient", return_value=mock_client)
    mocker.patch("interpreter_assistant.entrypoints.cli.DeepgramAdapter", return_value=mock_adapter)
    
    # Configure mocks
    mock_client.connect = AsyncMock()
    mock_client.send_audio = AsyncMock()
    mock_client.receive_transcript = AsyncMock(return_value=[{"is_final": True}])
    mock_adapter.format_transcript = MagicMock(return_value="test transcript")
    
    # Run main
    await cli.main("test_key")
    
    # Verify calls
    mock_capture.start.assert_called_once()
    mock_client.connect.assert_called_once()
    mock_adapter.format_transcript.assert_called_once()