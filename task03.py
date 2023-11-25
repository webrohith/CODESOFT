import random
import string

def generate_password(length):
    # Ensure the length is at least 4 to include all types of characters
    if length < 4:
        print("Password length should be at least 4")
        return

    # Define the characters that will be used to generate the password
    lowercase_letters = string.ascii_lowercase
    uppercase_letters = string.ascii_uppercase
    digits = string.digits
    punctuation = string.punctuation

    # Generate a password with at least one of each type of character
    password = [
        random.choice(lowercase_letters),
        random.choice(uppercase_letters),
        random.choice(digits),
        random.choice(punctuation),
    ]

    # Add random characters to meet the desired length
    all_characters = lowercase_letters + uppercase_letters + digits + punctuation
    for _ in range(length - 4):
        password.append(random.choice(all_characters))

    # Shuffle the characters to ensure randomness
    random.shuffle(password)

    # Convert the list of characters into a string
    password = ''.join(password)

    return password

# Prompt the user to specify the desired length of the password
length = int(input("Enter the desired length of the password: "))

# Generate the password
password = generate_password(length)

# Display the password
if password:
    print("Your generated password is: ", password)