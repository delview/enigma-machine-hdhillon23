# Start Enigma Machine with Phone Characters

# Encrypt function

# Decrypt function

# Greet the user and ask for their name and explain the program
user_name = input("What is your name before we get this program started?")
print(f"Greetings {user_name}! This is an engima machine program\
 that converts phone number characters into letters!\n")

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
            encrypted_message = encrypt_message(message)
            print(f"Encrypted message: {encrypted_message}\n")
    
    # Decrypt the message
    elif choice == 'd':
        message = input("Enter the message you want to decrypt (Type numbers only): ").strip()
        while not all(char.isdigit() or char.isspace() for char in message):
            message = input("Invalid input. Please enter a message containing numbers and spaces only: ").strip()
        decrypted_message = decrypt_message(message)
        print(f"Decrypted message: {decrypted_message}")

    # Ask the user if they want to play again (y/n)
    play_again = input("Do you want to encrypt or decrypt another message? (y/n): ").strip().lower()
    if play_again !='y':
        print(f"Thanks for playing {user_name}, goodbye! Hope to see you again soon!") # said goodbye if user chooses 'n' to stop using the program
        break
    