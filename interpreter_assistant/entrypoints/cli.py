"""Command-line interface entrypoint."""

import asyncio
import logging
from typing import Optional
from ..audio_io import AudioCapture, BufferManager
from ..services.deepgram import DeepgramClient, DeepgramAdapter

logger = logging.getLogger(__name__)

async def main(api_key: str) -> None:
    """Main transcription loop."""
    # Initialize components
    capture = AudioCapture()
    buffer = BufferManager()
    client = DeepgramClient(api_key)
    adapter = DeepgramAdapter()
    
    try:
        await client.connect()
        
        def process_frame(frame):
            buffer.add_frame(frame)
            asyncio.create_task(client.send_audio(frame.tobytes()))
            
        await capture.start(process_frame)
        
        async for response in client.receive_transcript():
            transcript = adapter.format_transcript(response)
            if transcript:
                print(transcript)
                
    except Exception as e:
        logger.error(f"Error during transcription: {e}")
    finally:
        capture.stop()
        await client.close()

if __name__ == "__main__":
    import os
    from dotenv import load_dotenv
    
    load_dotenv()
    api_key = os.getenv("DEEPGRAM_API_KEY")
    
    if not api_key:
        raise ValueError("DEEPGRAM_API_KEY not found in environment")
        
    asyncio.run(main(api_key))