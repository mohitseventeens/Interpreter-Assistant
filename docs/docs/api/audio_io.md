# Audio IO Module

Handles audio input/output operations.

## Classes

### AudioCapture
```python
class AudioCapture:
    """Handles audio stream capture and processing."""
    
    def __init__(self, sample_rate: int = 16000, chunk_size: int = 8000):
        """Initialize audio capture.
        
        Args:
            sample_rate: Audio sample rate in Hz
            chunk_size: Number of samples per chunk
        """
        
    async def start(self, callback: Callable[[np.ndarray], None]) -> None:
        """Start audio capture with processing callback.
        
        Args:
            callback: Function to process audio frames
        """
        
    def stop(self) -> None:
        """Stop audio capture."""
```

### BufferManager
```python
class BufferManager:
    """Manages audio buffers for real-time processing."""
    
    def __init__(self, max_seconds: float = 5.0, sample_rate: int = 16000):
        """Initialize buffer manager.
        
        Args:
            max_seconds: Maximum buffer duration in seconds
            sample_rate: Audio sample rate in Hz
        """
        
    def add_frame(self, frame: np.ndarray) -> None:
        """Add new audio frame to buffer."""
        
    def get_audio(self) -> np.ndarray:
        """Get complete audio buffer as single array."""
        
    def clear(self) -> None:
        """Clear audio buffer."""