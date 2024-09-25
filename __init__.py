# src/__init__.py

"""
ShieldPass Package

This package contains modules for demonstrating Android password security vulnerabilities,
including methods for bypassing and cracking passwords.
"""

# Import relevant classes or functions from the modules
from .shieldpass import main  # Assuming main() is your entry point function in shieldpass.py
from .android_cracker import crack_password  # Example function to crack passwords
from .bypass import bypass_lock  # Example function to bypass Android locks
from .utils import load_resources  # Utility function to load educational resources
from .educational_resources import get_best_practices, get_common_vulnerabilities  # Functions to get educational content

__all__ = [
    'main',
    'crack_password',
    'bypass_lock',
    'load_resources',
    'get_best_practices',
    'get_common_vulnerabilities'
]
