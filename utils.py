# src/utils.py

"""
Utilities Module

This module contains utility functions that can be used throughout the ShieldPass project. 
These functions are designed to assist with common tasks, such as loading resources and 
validating user input.
"""

def load_resources():
    """
    Function to load educational resources for the user.

    Returns:
        list: A list of available educational resources.
    """
    # Simulating loading educational resources
    resources = [
        "Best Practices for Android Security",
        "Common Android Vulnerabilities",
        "Overview of Security Tools for Android"
    ]
    return resources

def validate_password_input(password):
    """
    Function to validate the password input from the user.

    Args:
        password (str): The password input to validate.

    Returns:
        bool: True if the password meets the criteria, False otherwise.
    """
    # Example validation: password must be at least 6 characters
    if len(password) < 6:
        print("Password must be at least 6 characters long.")
        return False
    return True

# Additional utility functions can be added here
