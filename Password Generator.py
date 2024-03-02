import random
import string

def generate_password(length, use_lowercase=True, use_uppercase=True, use_digits=True, use_special=True):
    characters = ''

    if use_lowercase:
        characters += string.ascii_lowercase
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_digits:
        characters += string.digits
    if use_special:
        characters += string.punctuation

    if not characters:
        print("Error: No character set selected.")
        return None
    password = ''
    for i in range(length):
        password += (random.choice(characters) )
    return password


length = int(input("Enter the desired password length: "))
use_lowercase = input("Include lowercase letters? (yes/no): ").lower() == 'yes'
use_uppercase = input("Include uppercase letters? (yes/no): ").lower() == 'yes'
use_digits = input("Include digits? (yes/no): ").lower() == 'yes'
use_special = input("Include special characters? (yes/no): ").lower() == 'yes'

generated_password = generate_password(length, use_lowercase, use_uppercase, use_digits, use_special)

if generated_password:
    print(f"\nGenerated Password: {generated_password}")