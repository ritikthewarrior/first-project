import random
import string

def generate_password(length=12, use_special_chars=True, use_digits=True, use_uppercase=True):
    # Define character sets based on user preferences
    characters = string.ascii_lowercase  # Always include lowercase letters
    
    if use_uppercase:
        characters += string.ascii_uppercase  # Include uppercase letters
    
    if use_digits:
        characters += string.digits  # Include digits
    
    if use_special_chars:
        characters += string.punctuation  # Include special characters
    
    # Ensure the password has at least one character from each selected group
    password = [
        random.choice(string.ascii_lowercase),  # At least one lowercase letter
    ]
    
    if use_uppercase:
        password.append(random.choice(string.ascii_uppercase))
    
    if use_digits:
        password.append(random.choice(string.digits))
    
    if use_special_chars:
        password.append(random.choice(string.punctuation))
    
    # Fill the rest of the password length with random characters
    password += random.choices(characters, k=length - len(password))
    
    # Shuffle the password to randomize the order
    random.shuffle(password)
    
    return ''.join(password)

# Get user preferences for password generation
length = int(input("Enter password length: "))
use_special_chars = input("Include special characters? (y/n): ").lower() == 'y'
use_digits = input("Include digits? (y/n): ").lower() == 'y'
use_uppercase = input("Include uppercase letters? (y/n): ").lower() == 'y'

# Generate and display the password
password = generate_password(length, use_special_chars, use_digits, use_uppercase)
print(f"Generated Password: {password}")
