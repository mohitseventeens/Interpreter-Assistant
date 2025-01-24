"""Logging configuration and utilities."""

import logging
from typing import Optional
from rich.logging import RichHandler

def setup_logging(level: int = logging.INFO) -> None:
    """Configure logging with Rich formatting."""
    logging.basicConfig(
        level=level,
        format="%(message)s",
        datefmt="[%X]",
        handlers=[RichHandler(rich_tracebacks=True)]
    )

def get_logger(name: Optional[str] = None) -> logging.Logger:
    """Get configured logger instance."""
    return logging.getLogger(name)