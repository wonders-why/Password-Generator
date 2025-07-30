import random  # Import the random module for generating random choices
import secrets
import string  # Import the string module to access letters, digits, and punctuation

# Combine letters, digits, and punctuation to form the pool of password characters
chars = string.ascii_letters + string.digits + string.punctuation

def get_password_length():
    """
    Prompt the user to enter a valid password length (minimum 6).
    Repeats until valid input is received.
    """
    try:
        x = int(input("Enter the length of the password: "))
        if x < 6:
            print("Password must be at least 6 characters.")
            return get_password_length()
        else:
            return x
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        return get_password_length()

def password_value(length):
    """
    Generate a password of the given length using random characters from the pool.
    """
    return ''.join(secrets.choice(chars) for x in range(1, length))
5
# Get user input and generate the password
length = get_password_length()
password = password_value(length)
print("Generated Password:", password)
