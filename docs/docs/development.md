# Development Guide

## Setup

1. Clone the repository:
```bash
git clone https://github.com/mohitseventeens/interpreter-assistant.git
cd interpreter-assistant
```

2. Install dependencies:
```bash
poetry install
```

3. Set up pre-commit hooks:
```bash
poetry run pre-commit install
```

## Testing

Run all tests:
```bash
poetry run pytest
```

Run specific test file:
```bash
poetry run pytest tests/test_audio_io.py
```

## Documentation

Build documentation:
```bash
poetry run mkdocs build
```

Serve documentation locally:
```bash
poetry run mkdocs serve
```

## Code Style

- Follow PEP 8 guidelines
- Use type hints
- Write docstrings for all public methods
- Keep line length under 88 characters