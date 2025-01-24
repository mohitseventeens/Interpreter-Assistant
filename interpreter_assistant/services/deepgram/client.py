"""Deepgram WebSocket client implementation."""

import asyncio
import websockets
import json
from typing import AsyncGenerator, Optional

class DeepgramClient:
    """Manages WebSocket connection to Deepgram API."""
    
    def __init__(self, api_key: str, host: str = "wss://api.deepgram.com"):
        self.api_key = api_key
        self.host = host
        self.connection = None
        
    async def connect(self) -> None:
        """Establish WebSocket connection."""
        self.connection = await websockets.connect(
            f"{self.host}/v1/listen",
            extra_headers={"Authorization": f"Token {self.api_key}"}
        )
        
    async def send_audio(self, audio_data: bytes) -> None:
        """Send audio data through WebSocket."""
        if self.connection:
            await self.connection.send(audio_data)
            
    async def receive_transcript(self) -> AsyncGenerator[dict, None]:
        """Receive transcription results."""
        if self.connection:
            async for message in self.connection:
                yield json.loads(message)
                
    async def close(self) -> None:
        """Close WebSocket connection."""
        if self.connection:
            await self.connection.close()