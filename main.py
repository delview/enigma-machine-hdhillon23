# Start Enigma Machine with Phone Characters

# Function to encrypt a message
def encrypt_message(message):
    # Mapping letters to numbers (phone style)
    phone_dict = {
        'A': '2', 'B': '22', 'C': '222',
        'D': '3', 'E': '33', 'F': '333',
        'G': '4', 'H': '44', 'I': '444',
        'J': '5', 'K': '55', 'L': '555',
        'M': '6', 'N': '66', 'O': '666',
        'P': '7', 'Q': '77', 'R': '777', 'S': '7777',
        'T': '8', 'U': '88', 'V': '888',
        'W': '9', 'X': '99', 'Y': '999', 'Z': '9999',
        ' ': '0'
    }
    # Convert letters to numbers
    encrypted = ""
    for char in message.upper():
        encrypted += phone_dict.get(char, '') + " "
    return encrypted.strip()

# Function to decrypt a message
def decrypt_message(encrypted_text):
    # Mapping numbers back to letters
    reverse_dict = {
        '2': 'A', '22': 'B', '222': 'C',
        '3': 'D', '33': 'E', '333': 'F',
        '4': 'G', '44': 'H', '444': 'I',
        '5': 'J', '55': 'K', '555': 'L',
        '6': 'M', '66': 'N', '666': 'O',
        '7': 'P', '77': 'Q', '777': 'R', '7777': 'S',
        '8': 'T', '88': 'U', '888': 'V',
        '9': 'W', '99': 'X', '999': 'Y', '9999': 'Z',
        '0': ' '
    }
    # Split the input into chunks
    words = encrypted_text.split()
    decrypted = ""
    for word in words:
        if word in reverse_dict:
            decrypted += reverse_dict[word]  # Map to a letter
        else:
            return None  # Return None to indicate an invalid chunk
    return decrypted

# Main Program
user_name = input("What is your name before we get this program started? ").strip()  # Get user's name
print(f"Greetings {user_name}! This is an enigma machine program that converts phone number characters into letters!\n")

while True:
    # Ask the user if they want to encrypt or decrypt
    choice = input(f"{user_name}, would you like to encrypt or decrypt a message? (e/d): ").strip().lower()
    while choice not in ['e', 'd']:  # Validate input
        choice = input("Invalid choice. Please choose 'e' for encrypt or 'd' for decrypt: ").strip().lower()

    if choice == 'e':  # Encrypt the message
        while True:  # Loop until valid input is provided
            message = input("Enter the message you want to encrypt (Type letters and spaces only): ").strip()
            if all(char.isalpha() or char.isspace() for char in message):  # Validate input
                encrypted_message = encrypt_message(message)  # Encrypt the message
                print(f"Encrypted message: {encrypted_message}\n")
                break  # Exit loop after successful encryption
            else:
                print("Invalid input. Please enter a message containing letters and spaces only.")

    elif choice == 'd':  # Decrypt the message
        while True:  # Loop until valid input is provided
            encrypted_text = input("Enter the message you want to decrypt (Type numbers and spaces only): ").strip()
            if all(char.isdigit() or char.isspace() for char in encrypted_text):  # Validate input
                decrypted_message = decrypt_message(encrypted_text)  # Decrypt the message
                if decrypted_message is not None:
                    print(f"Decrypted message: {decrypted_message}\n")
                    break  # Exit loop after successful decryption
                else:
                    print("Invalid input. One or more chunks do not match any letter. Please try again.")
            else:
                print("Invalid input. Please enter a message containing numbers and spaces only.")

    # Ask the user if they want to play again
    play_again = input("Do you want to encrypt or decrypt another message? (y/n): ").strip().lower()
    if play_again != 'y':  # Exit if the user doesn't want to continue
        print(f"Thanks for playing {user_name}, goodbye! Hope to see you again soon!")
        break
