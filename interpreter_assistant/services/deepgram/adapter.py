"""Deepgram response adapter and formatting."""

from typing import Dict, Optional
from datetime import datetime

class DeepgramAdapter:
    """Adapts and formats Deepgram API responses."""
    
    def __init__(self, language_code: str = "en-US"):
        self.language_code = language_code
        
    def format_transcript(self, response: Dict) -> Optional[str]:
        """Format transcript from Deepgram response."""
        if not response.get("is_final"):
            return None
            
        transcript = response.get("channel", {}).get("alternatives", [{}])[0].get("transcript", "")
        if not transcript:
            return None
            
        return self._add_timestamps(transcript, response)
        
    def _add_timestamps(self, transcript: str, response: Dict) -> str:
        """Add timestamps to transcript."""
        start = response.get("start", 0)
        duration = response.get("duration", 0)
        end = start + duration
        
        start_time = datetime.fromtimestamp(start).strftime("%H:%M:%S")
        end_time = datetime.fromtimestamp(end).strftime("%H:%M:%S")
        
        return f"[{start_time} - {end_time}] {transcript}"