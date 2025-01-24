# Deepgram Module

Handles Deepgram API integration.

## Classes

### DeepgramClient
```python
class DeepgramClient:
    """Manages WebSocket connection to Deepgram API."""
    
    def __init__(self, api_key: str, host: str = "wss://api.deepgram.com"):
        """Initialize Deepgram client.
        
        Args:
            api_key: Deepgram API key
            host: Deepgram API host URL
        """
        
    async def connect(self) -> None:
        """Establish WebSocket connection."""
        
    async def send_audio(self, audio_data: bytes) -> None:
        """Send audio data through WebSocket."""
        
    async def receive_transcript(self) -> AsyncGenerator[dict, None]:
        """Receive transcription results."""
        
    async def close(self) -> None:
        """Close WebSocket connection."""
```

### DeepgramAdapter
```python
class DeepgramAdapter:
    """Adapts and formats Deepgram API responses."""
    
    def __init__(self, language_code: str = "en-US"):
        """Initialize adapter.
        
        Args:
            language_code: Language code for transcription
        """
        
    def format_transcript(self, response: Dict) -> Optional[str]:
        """Format transcript from Deepgram response."""