"""Audio buffer management for real-time processing."""

import numpy as np
from collections import deque
from typing import Deque, Optional

class BufferManager:
    """Manages audio buffers for real-time processing."""
    
    def __init__(self, max_seconds: float = 2.0, sample_rate: int = 16000):
        """Initialize buffer manager.
        
        Args:
            max_seconds: Maximum buffer duration in seconds (reduced for lower latency)
            sample_rate: Audio sample rate in Hz
        """
        self.sample_rate = sample_rate
        self.max_samples = int(max_seconds * sample_rate)
        self.buffer: Deque[np.ndarray] = deque(maxlen=self.max_samples)
        
    def add_frame(self, frame: np.ndarray) -> None:
        """Add new audio frame to buffer."""
        self.buffer.append(frame)
        
    def get_audio(self) -> np.ndarray:
        """Get complete audio buffer as single array."""
        return np.concatenate(list(self.buffer)) if self.buffer else np.array([])
        
    def clear(self) -> None:
        """Clear audio buffer."""
        self.buffer.clear()