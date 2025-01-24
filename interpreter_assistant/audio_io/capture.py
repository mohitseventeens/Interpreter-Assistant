"""Audio capture implementation using PyAudio."""

import asyncio
import pyaudio
import numpy as np
from typing import Optional, Callable

class AudioCapture:
    """Handles audio stream capture and processing."""
    
    def __init__(self, sample_rate: int = 16000, chunk_size: int = 8000):
        self.sample_rate = sample_rate
        self.chunk_size = chunk_size
        self.audio = pyaudio.PyAudio()
        self.stream = None
        
    async def start(self, callback: Callable[[np.ndarray], None]) -> None:
        """Start audio capture with processing callback."""
        loop = asyncio.get_event_loop()
        
        def sync_callback(in_data, frame_count, time_info, status_flags):
            audio_data = np.frombuffer(in_data, dtype=np.int16)
            loop.call_soon_threadsafe(lambda: callback(audio_data))
            return (in_data, pyaudio.paContinue)
            
        self.stream = self.audio.open(
            format=pyaudio.paInt16,
            channels=1,
            rate=self.sample_rate,
            input=True,
            frames_per_buffer=self.chunk_size,
            stream_callback=sync_callback
        )
    
    def stop(self) -> None:
        """Stop audio capture."""
        if self.stream:
            self.stream.stop_stream()
            self.stream.close()
        self.audio.terminate()