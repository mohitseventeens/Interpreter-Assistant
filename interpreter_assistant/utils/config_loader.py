"""Configuration loading utilities."""

import os
from typing import Dict, Any
from dotenv import load_dotenv
import yaml

def load_config() -> Dict[str, Any]:
    """Load configuration from environment and YAML files."""
    load_dotenv()
    
    config = {
        "deepgram": {
            "api_key": os.getenv("DEEPGRAM_API_KEY"),
            "host": os.getenv("DEEPGRAM_HOST", "wss://api.deepgram.com"),
            "language": os.getenv("DEEPGRAM_LANGUAGE", "en-US")
        },
        "audio": {
            "sample_rate": int(os.getenv("AUDIO_SAMPLE_RATE", "16000")),
            "chunk_size": int(os.getenv("AUDIO_CHUNK_SIZE", "8000"))
        }
    }
    
    # Load additional config from YAML if present
    config_path = os.getenv("CONFIG_PATH", "config/config.yaml")
    if os.path.exists(config_path):
        with open(config_path) as f:
            yaml_config = yaml.safe_load(f)
            config.update(yaml_config)
            
    return config