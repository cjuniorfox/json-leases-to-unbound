from .core import main
from .cli import main_cli

__all__ = ["main", "main_cli"]
__version__ = "0.1.0"

def get_version():
    return __version__