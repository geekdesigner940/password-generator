import string
import random

def generate_password(length, uppercase=True, lowercase=True, numbers=True, special_chars=True):
    """
    Generate a random password based on user preferences.

    Parameters:
    - length (int): The length of the password.
    - uppercase (bool): Include uppercase letters in the password (default=True).
    - lowercase (bool): Include lowercase letters in the password (default=True).
    - numbers (bool): Include numbers in the password (default=True).
    - special_chars (bool): Include special characters in the password (default=True).

    Returns:
    - str: The randomly generated password.
    """
    chars = ""
    if uppercase:
        chars += string.ascii_uppercase
    if lowercase:
        chars += string.ascii_lowercase
    if numbers:
        chars += string.digits
    if special_chars:
        chars += string.punctuation

    if not chars:
        raise ValueError("At least one character type should be selected.")

    return ''.join(random.choice(chars) for _ in range(length))

def main():
    """
    Main function to interact with the user and generate passwords.
    """
    try:
        num_passwords = int(input("How many passwords do you want to generate? "))
        password_length = int(input("Enter password length: "))

        include_uppercase = input("Include uppercase letters? (y/n): ").lower() == 'y'
        include_lowercase = input("Include lowercase letters? (y/n): ").lower() == 'y'
        include_numbers = input("Include numbers? (y/n): ").lower() == 'y'
        include_special_chars = input("Include special characters? (y/n): ").lower() == 'y'

        passwords = []
        for _ in range(num_passwords):
            password = generate_password(password_length, include_uppercase, include_lowercase, include_numbers, include_special_chars)
            passwords.append(password)

        print("\nGenerated Passwords:")
        for password in passwords:
            print(password)

    except ValueError as e:
        print("Error:", e)
    except KeyboardInterrupt:
        print("\nPassword generation aborted.")

if __name__ == "__main__":
    main()
