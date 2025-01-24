# Utilities Module

Provides helper functions and configuration management.

## Functions

### load_config
```python
def load_config() -> Dict[str, Any]:
    """Load configuration from environment and YAML files.
    
    Returns:
        Dictionary containing configuration values
    """
```

### setup_logging
```python
def setup_logging(level: int = logging.INFO) -> None:
    """Configure logging with Rich formatting.
    
    Args:
        level: Logging level (e.g., logging.INFO)
    """
```

### get_logger
```python
def get_logger(name: Optional[str] = None) -> logging.Logger:
    """Get configured logger instance.
    
    Args:
        name: Logger name
        
    Returns:
        Configured logger instance
    """