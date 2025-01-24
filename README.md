# Interpreter Assistant

Real-time bilingual transcription system using Deepgram API.

## Features

- Real-time microphone audio transcription
- Support for multiple languages
- Configurable audio processing
- WebSocket-based Deepgram integration
- Rich logging and monitoring

## Installation

1. Install Poetry:
```bash
pip install poetry
```

2. Install dependencies:
```bash
poetry install
```

3. Create .env file:
```bash
cp .env.example .env
```

4. Add your Deepgram API key to .env:
```bash
DEEPGRAM_API_KEY=your_api_key_here
```

## Usage

Run the transcription system:
```bash
poetry run python -m interpreter_assistant.entrypoints.cli
```

## Configuration

Edit `config/config.yaml` to customize:
- Audio settings (sample rate, chunk size)
- Deepgram settings (language, model)
- Logging configuration

## Development

1. Install pre-commit hooks:
```bash
poetry run pre-commit install
```

2. Run tests:
```bash
poetry run pytest
```

3. Build documentation:
```bash
poetry run mkdocs serve
```

## Documentation

Full API documentation available at: [docs/](docs/index.md)