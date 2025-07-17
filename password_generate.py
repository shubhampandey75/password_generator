import string
import random

def generate_password(length, use_uppercase=True, use_digits=True, use_specialchar=True):
    # Starts with lowercase
    characters = list(string.ascii_lowercase)

    # Add characters based on user choices
    if use_uppercase:
        characters += list(string.ascii_uppercase)
    if use_digits:
        characters += list(string.digits)
    if use_specialchar:
        characters += list(string.punctuation)

    if length < 1:
        raise ValueError("Length of password must be at least 1.")
    if not characters:
        raise ValueError("No character sets selected.")

    # Generate password
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("Password Generator")
    try:
        length = int(input("Enter the desired password length: "))
        use_upper = input("Include uppercase letters(yes/no) ?: ").lower() == 'yes'
        use_digits = input("Include digits(yes/no) ?: ").lower() == 'yes'
        use_special = input("Include special characters(yes/no) ?: ").lower() == 'yes'

        password = generate_password(length, use_upper, use_digits, use_special)
        print("\nGenerated Password:", password)
    except ValueError as valerr:
        print("Error:", valerr)

if __name__ == "__main__":
    main()
