"""Tests for audio input/output components."""

import numpy as np
from interpreter_assistant.audio_io import AudioCapture, BufferManager

def test_buffer_manager_add_frame():
    """Test adding frames to buffer."""
    buffer = BufferManager(max_seconds=1.0, sample_rate=16000)
    frame = np.zeros(1600, dtype=np.int16)
    
    buffer.add_frame(frame)
    assert len(buffer.buffer) == 1
    assert buffer.get_audio().size == 1600
    
def test_buffer_manager_clear():
    """Test clearing buffer."""
    buffer = BufferManager()
    frame = np.zeros(1600, dtype=np.int16)
    
    buffer.add_frame(frame)
    buffer.clear()
    assert len(buffer.buffer) == 0
    assert buffer.get_audio().size == 0