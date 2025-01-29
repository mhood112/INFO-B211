import random
import string
import os
from datetime import datetime

def generate_password(length=12, include_punctuation=True, exclude_chars=""):
    """Generate a random password."""
    characters = string.ascii_letters + string.digits # numbers and letters
    if include_punctuation: 
        characters += string.punctuation # If there is any punctuation, add it to the character set
    
    # Remove excluded characters from the character set
    characters = ''.join(c for c in characters if c not in exclude_chars)
    
    password = ''.join(random.choice(characters) for i in range(length)) #ranmdomly select characters from the character set
    return password

def log_password(password, password_type):
    """Log the generated password with timestamp to the appropriate file."""
    timestamp = datetime.now().strftime("%A, %d %B %Y %H:%M:%S") # Get the current date and time
    directory = "Memorable" if password_type == "memorable" else "Random" # Determine the directory based on password type
    os.makedirs(directory, exist_ok=True) # Create the directory if it doesn't exist
    file_path = os.path.join(directory, "Generated_Passwords.txt") # Create the file path
    
    with open(file_path, "a") as file:
        file.write(f"{timestamp}: {password}\n") # Write the password and timestamp to the file

# Example usage
if __name__ == "__main__":
    #main script - get user input for password length, punctuation inclusion, and excluded characters
    try:
        n = int(input("Enter the desired length of the password: "))
        if n <= 0:
            raise ValueError("Password length must be a positive integer.")
    except ValueError as e:
        print(f"Invalid input for password length: {e}")
        exit(1)
    
    try:
        include_punctuation = input("Include punctuation symbols? (yes/no): ").strip().lower()
        if include_punctuation not in ['yes', 'no']:
            raise ValueError("Input must be 'yes' or 'no'.")
        include_punctuation = include_punctuation == 'yes'
    except ValueError as e:
        print(f"Invalid input for punctuation inclusion: {e}")
        exit(1)
    
    exclude_chars = input("Enter any characters to exclude (leave blank if none): ").strip()
    # the range for the loop is 1000, but it can be changed to any number
    try:
        for _ in range(1000):
            password_type = random.choice(["memorable", "random"])
            if password_type == "memorable":
                # Generate a memorable password (for simplicity, using the same function)
                password = generate_password(length=n, include_punctuation=False, exclude_chars="l1O0" + exclude_chars)
            else:
                password = generate_password(length=n, include_punctuation=include_punctuation, exclude_chars=exclude_chars)
            
            log_password(password, password_type)
    except Exception as e:
        print(f"An error occurred during password generation: {e}")
        exit(1)
