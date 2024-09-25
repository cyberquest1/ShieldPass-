"""
ShieldPass: Password Bypass & Cracking Tool

This package contains modules and functionalities for 
analyzing and exploiting password vulnerabilities.
"""

# Import necessary modules for ease of access
from .shieldpass import main
from .bypass import PasswordBypass
from .cracking import PasswordCracker
from .hash_cracker import HashCracker
from .utils import Logger

__all__ = [
    "main",
    "PasswordBypass",
    "PasswordCracker",
    "HashCracker",
    "Logger"
]
