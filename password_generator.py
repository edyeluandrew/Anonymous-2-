import random
import string

def generate_password(length=12, use_uppercase=True, use_lowercase=True, 
                     use_digits=True, use_special_chars=True):
    """
    Generate a random password with customizable options.
    
    Parameters:
    - length: Length of the password (default: 12)
    - use_uppercase: Include uppercase letters (default: True)
    - use_lowercase: Include lowercase letters (default: True)
    - use_digits: Include digits (default: True)
    - use_special_chars: Include special characters (default: True)
    
    Returns:
    - A random password string
    """
    # Define character sets
    chars = ""
    
    if use_uppercase:
        chars += string.ascii_uppercase
    if use_lowercase:
        chars += string.ascii_lowercase
    if use_digits:
        chars += string.digits
    if use_special_chars:
        chars += string.punctuation
    
    # Ensure at least one character set is selected
    if not chars:
        raise ValueError("At least one character set must be enabled")
    
    # Generate password
    password = ''.join(random.choice(chars) for _ in range(length))
    
    return password

if __name__ == "__main__":
    # Example usage
    print("Default password (12 chars, all character types):")
    print(generate_password())
    
    print("\nLonger password (16 chars):")
    print(generate_password(length=16))
    
    print("\nDigits-only password (8 chars):")
    print(generate_password(8, False, False, True, False))
    
    print("\nPassword without special characters:")
    print(generate_password(use_special_chars=False))
    
    print("\nCustom password:")
    length = int(input("Enter password length: "))
    use_upper = input("Include uppercase letters? (y/n): ").lower() == 'y'
    use_lower = input("Include lowercase letters? (y/n): ").lower() == 'y'
    use_digits = input("Include digits? (y/n): ").lower() == 'y'
    use_special = input("Include special characters? (y/n): ").lower() == 'y'
    
    try:
        password = generate_password(length, use_upper, use_lower, use_digits, use_special)
        print(f"\nYour custom password: {password}")
    except ValueError as e:
        print(f"Error: {e}")