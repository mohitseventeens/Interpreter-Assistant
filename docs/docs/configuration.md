# Configuration

The system can be configured through environment variables and YAML files.

## Environment Variables

| Variable | Description | Default |
|----------|-------------|---------|
| DEEPGRAM_API_KEY | Deepgram API key | Required |
| DEEPGRAM_HOST | Deepgram API host | wss://api.deepgram.com |
| AUDIO_SAMPLE_RATE | Audio sample rate | 16000 |
| AUDIO_CHUNK_SIZE | Audio chunk size | 8000 |

## YAML Configuration

Create `config/config.yaml` with the following structure:

```yaml
deepgram:
  api_key: your_api_key
  host: wss://api.deepgram.com
  language: en-US
  
audio:
  sample_rate: 16000
  chunk_size: 8000
  
logging:
  level: INFO
  format: "%(message)s"
```

## Loading Order

1. Environment variables
2. YAML configuration
3. Default values