# Start Enigma Machine with Phone Characters

# Encrypt function

# Decrypt function

# Greet the user and ask for their name and explain the program
user_name = input("What is your name before we get this program started?")
print(f"Greetings {user_name}! This is an engima machine program\
 that converts phone number characters into letters!")

while True:
    # Ask the user if they want to encrypt or decrypt
    choice = input(f"{user_name} would you like to encrypt or decrypt a message? (e/d): ").strip().lower()
    while choice not in ['e','d']:
        choice = input("Invalid choice. Please choose 'e' for encrypt or 'd' for decrypt: ").strip().lower()

    # Encrypt the message
    if choice == 'e':
        message = input("Enter the message you want to encrypt (Type letters and spaces only): ").strip()
        while not all(char.isalpha() or char.isspace() for char in message):
            message = input("Invalid input. Please enter a message containing letters and spaces only: ").strip()
            encrypted_mssage = encrypt_message(message)
            print(f"Encrypted message: {encrypt_message}")

    # Print the encrypted message

    # Decrypt the message

    # Print the encrypted message

    # Ask the user if they want to play again [y/n]

    # If "y" restart the program

    # If "n" stop/end the program

    # Say goodbye