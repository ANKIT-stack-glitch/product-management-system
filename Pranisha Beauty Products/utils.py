import os

def clear_screen():
    """Clear the console screen."""
    os.system('cls' if os.name == 'nt' else 'clear')

def validate_input(prompt, condition):
    """Prompt the user for input and validate it based on a given condition."""
    while True:
        user_input = input(prompt).strip()
        if condition(user_input):
            return user_input
        print("Invalid input. Please try again.")
