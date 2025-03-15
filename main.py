# Start Enigma Machine with Phone Characters

# Function to encrypt a message using phone characters
def encrypt_message(message):
    phone_dict = { # Phone characters mapping
     'A': '2', 'B': '22', 'C': '222',
     'D': '3', 'E': '33', 'F': '333',
     'G': '4', 'H': '44', 'I': '444',
     'J': '5', 'K': '55', 'L': '555',
     'M': '6', 'N': '66', 'O': '666',
     'P': '7', 'Q': '77', 'R': '777', 'S': '7777',
     'T': '8', 'U': '88', 'V': '888',
     'W': '9', 'X': '99', 'Y': '999', 'Z': '9999',
    }

    # Generate encrypted message by interacting through the input message
    # If a character is in the dictionary, map it to its corresponding number
    encrypted_text = ''.join(phone_dict[char.upper()] for char in message if char.upper() in phone_dict)
    
    # Return the encrypted text to the caller
    return encrypted_text

# Function to decrypt a message back to text
def decrypt_message(encrypted_text):
    reverse_dict = { # Reverse mapping of numbers to letters
     '2': 'A', '22': 'B', '222': 'C',
     '3': 'D', '33': 'E', '333': 'F',
     '4': 'G', '44': 'H', '444': 'I',
     '5': 'J', '55': 'K', '555': 'L',
     '6': 'M', '66': 'M', '666': 'O',
     '7': 'P', '77': 'Q', '777': 'R', '7777': 'S',
     '8': 'T', '88': 'U', '888': 'V',
     '9': 'W', '99': 'X', '999': 'Y', '9999': 'Z',

    }

    # Split the input encrypted_text into chunks and map each chunk to its corresponding letter
    return ''.join(reverse_dict.get(chunk, '?') for chunk in encrypted_text.split())

# Greet the user and ask for their name and explain the program
user_name = input("What is your name before we get this program started? ").strip() # Strip spaces from the user's input
print(f"Greetings {user_name}! This is an engima machine program\
 that converts phone number characters into letters!\n") # Greet the user and explain the program

while True:
    # Ask the user if they want to encrypt or decrypt
    choice = input(f"{user_name} would you like to encrypt or decrypt a message? (e/d): ").strip().lower()
    while choice not in ['e','d']: # Validate input (must be 'e' or 'd')
        choice = input("Invalid choice. Please choose 'e' for encrypt or 'd' for decrypt: ").strip().lower()

    # Encrypt the message
    if choice == 'e':
        message = input("Enter the message you want to encrypt (Type letters and spaces only): ").strip()
        while not all(char.isalpha() or char.isspace() for char in message): # Validate input (letters/spaces only)
            message = input("Invalid input. Please enter a message containing letters and spaces only: ").strip()
        encrypted_message = encrypt_message(message) # Encrypt the message
        print(f"Encrypted message: {encrypted_message}\n") # Display the encrypted message
    
    # Decrypt the message
    elif choice == 'd':
        encrypted_text = input("Enter the message you want to decrypt (Type numbers and spaces only): ").strip()
        while not all(char.isdigit() or char.isspace() for char in encrypted_text): # Validate input (numbers/spaces only)
            encrypted_text = input("Invalid input. Please enter a message containing numbers and spaces only: ").strip()
        decrypted_message = decrypt_message(encrypted_text) # Decrypt the message
        print(f"Decrypted message: {decrypted_message}") # Display the decrypted message

    # Ask the user if they want to play again (y/n)
    play_again = input("Do you want to encrypt or decrypt another message? (y/n): ").strip().lower()
    if play_again !='y': # Exit if the user doesn't want to continue
        print(f"Thanks for playing {user_name}, goodbye! Hope to see you again soon!") # Goodbye message
        break
    