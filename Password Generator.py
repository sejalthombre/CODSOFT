import random
import string

def generate_password(length, use_digits=False, use_special=False, use_number=False):
    characters = string.ascii_letters
    if use_digits:
        characters += string.digits
    if use_special:
        characters += string.punctuation
    if use_number:
        characters += string.digits  # Corrected from string.number to string.digits

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    length = int(input("Enter the desired length for the password: "))
    use_digits = input("Include digits? (yes/no): ").lower() == 'yes'
    use_special = input("Include special characters? (yes/no): ").lower() == 'yes'
    use_number = input("Include numbers? (yes/no): ").lower() == 'yes'
    
    password = generate_password(length, use_digits, use_special, use_number)
    print(f"Generated Password: {password}")

if __name__ == "__main__":
    main()
