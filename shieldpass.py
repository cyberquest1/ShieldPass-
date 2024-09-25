# src/shieldpass.py

"""
ShieldPass: Main Application Logic

This module serves as the entry point for the ShieldPass project. It provides functionalities 
for demonstrating Android password security vulnerabilities, including methods for bypassing 
and cracking passwords.
"""

from src.android_cracker import crack_password
from src.bypass import bypass_lock
from src.utils import load_resources

def main():
    """
    Main function to run the ShieldPass application.
    Provides a menu-driven interface for users to choose an action.
    """
    while True:
        print("Welcome to ShieldPass!")
        print("1. Crack Android Password")
        print("2. Bypass Android Lock")
        print("3. Load Educational Resources")
        print("4. Exit")
        
        choice = input("Enter your choice (1-4): ")
        
        if choice == '1':
            password = input("Enter the password to crack: ")
            result = crack_password(password)
            print(f"Cracking Result: {result}")
        
        elif choice == '2':
            print("Bypassing Android Lock...")
            bypass_lock()
        
        elif choice == '3':
            resources = load_resources()
            print("Educational Resources:")
            for resource in resources:
                print(f"- {resource}")
        
        elif choice == '4':
            print("Exiting the application. Goodbye!")
            break
        
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
