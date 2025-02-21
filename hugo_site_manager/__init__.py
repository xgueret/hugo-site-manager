# Version du package
__version__= "1.0.0"

from .cli import main
from .core import HugoManager

print(f"hugo-site-manager version {__version__} loaded.")

__all__ = [
    "HugoManager", 
    "main"
]
