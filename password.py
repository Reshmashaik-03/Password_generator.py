import random
import string
def generate_password(length=12, include_uppercase=True, include_lowercase=True, include_digits=True, include_symbols=True):
    characters = ""
    if include_uppercase:
        characters += string.ascii_uppercase
    if include_lowercase:
        characters += string.ascii_lowercase
    if include_digits:
        characters += string.digits
    if include_symbols:
        characters += string.punctuation 
    if not characters:
        return "Error: Please select at least one character type (uppercase, lowercase, digits, or symbols)."
    password_parts = []
    if include_uppercase:
        password_parts.append(random.choice(string.ascii_uppercase))
    if include_lowercase:
        password_parts.append(random.choice(string.ascii_lowercase))
    if include_digits:
        password_parts.append(random.choice(string.digits))
    if include_symbols:
        password_parts.append(random.choice(string.punctuation))
    if length < len(password_parts):
        return f"Error: Password length ({length}) is too short to include at least one of each selected character type ({len(password_parts)} required)."
    remaining_length = length - len(password_parts)
    password_parts.extend(random.choice(characters) for _ in range(remaining_length))
    random.shuffle(password_parts)
    return "".join(password_parts)
if __name__ == "__main__":
    while True:
        print("--- Strong Password Generator ---")
        while True:
            try:
                length = int(input("Enter desired password length (e.g., 15): "))
                if length <= 0:
                    print("Length must be a positive number.")
                    continue
                break
            except ValueError:
                print("Invalid input. Please enter a number.")
        include_uppercase = input("Include uppercase letters (A-Z)? (yes/no): ").lower() == 'yes'
        include_lowercase = input("Include lowercase letters (a-z)? (yes/no): ").lower() == 'yes'
        include_digits = input("Include digits (0-9)? (yes/no): ").lower() == 'yes'
        include_symbols = input("Include symbols (!@#$%^&*...)? (yes/no): ").lower() == 'yes'
        password = generate_password(length, include_uppercase, include_lowercase, include_digits, include_symbols)
        print(f"\nGenerated Password: {password}")
        print("\n--- Another Password? ---")
        while True:
            again = input("Generate another password? (yes/no): ").lower()
            if again == 'yes':
                break
            elif again == 'no':
                print("Exiting password generator. Goodbye!")
                exit()
            else:
                print("Invalid input. Please enter 'yes' or 'no'.")
