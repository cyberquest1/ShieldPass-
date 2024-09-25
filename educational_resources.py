# src/educational_resources.py

"""
Educational Resources Module

This module provides functions to access educational resources related to Android 
security, including best practices, common vulnerabilities, and tools for protection.
"""

def get_best_practices():
    """
    Function to get best practices for Android security.

    Returns:
        list: A list of recommended best practices.
    """
    best_practices = [
        "Keep your device updated with the latest security patches.",
        "Use strong, unique passwords for each application.",
        "Enable two-factor authentication wherever possible.",
        "Be cautious when downloading apps; use official stores.",
        "Regularly back up your data.",
        "Use a reputable security app to monitor your device."
    ]
    return best_practices

def get_common_vulnerabilities():
    """
    Function to get a list of common Android vulnerabilities.

    Returns:
        list: A list of common vulnerabilities found in Android devices.
    """
    vulnerabilities = [
        "Weak or easily guessable passwords.",
        "Outdated software and unpatched vulnerabilities.",
        "Malicious applications from untrusted sources.",
        "Lack of encryption on sensitive data.",
        "Unsecured Wi-Fi networks."
    ]
    return vulnerabilities

# Additional educational resource functions can be added here
