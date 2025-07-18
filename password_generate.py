import string
import random

def gen_password(len, uppercase=True, digits=True, special=True):
    char = list(string.ascii_lowercase)

    #add characters based on user choice
    if uppercase:
        char += list(string.ascii_uppercase)
    if digits:
        char += list(string.digits)
    if special:
        char += list(string.punctuation) 

    if len < 1:
        raise ValueError("Password should not be less than 1.")
    if not char:
        raise ValueError("No character selected.") 
    
    password = ''.join(random.choice(char) for _ in range (len))
    return password

def main():
    print("Password Generator")
    try:
        len = int(input("Length of the password:"))
        uppercase = input("Include uppercase? (yes/no):").lower() == 'yes'
        digits = input("Include digits? (yes/no)").lower() == 'yes'
        special = input("Include special characters? (yes/no)").lower() == 'yes'

        password = gen_password(len, uppercase, digits, special)
        print("\nGenerate password:", password)
    except ValueError as valerr:
        print("Error:", valerr)

if __name__ == "__main__":
    main()    
