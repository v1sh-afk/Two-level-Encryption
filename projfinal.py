# Caesar cipher encryption and decryption functions
def caesar_encrypt(text, key=3):
    li = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    encrypted_text = ""

    for char in text:
        if char.isupper():
            char = char.lower()
            new_index = (li.index(char) + key) % 26
            encrypted_text += li[new_index].upper()
        elif char.islower():
            new_index = (li.index(char) + key) % 26
            encrypted_text += li[new_index]
        else:
            encrypted_text += char

    return encrypted_text

def caesar_decrypt(text, key=3):
    li = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    decrypted_text = ""
    key = 26 - key

    for char in text:
        if char.isupper():
            char = char.lower()
            new_index = (li.index(char) + key) % 26
            decrypted_text += li[new_index].upper()
        elif char.islower():
            new_index = (li.index(char) + key) % 26
            decrypted_text += li[new_index]
        else:
            decrypted_text += char

    return decrypted_text

# XOR-based encryption and decryption functions
def simple_encrypt(data, key):
    encrypted_data = bytearray()
    for byte in data:
        encrypted_data.append(byte ^ key)
    return encrypted_data

def simple_decrypt(encrypted_data, key):
    decrypted_data = bytearray()
    for byte in encrypted_data:
        decrypted_data.append(byte ^ key)
    return decrypted_data

# Two-level encryption function
def two_level_encrypt(data, caesar_key, xor_key):
    # First, apply Caesar cipher encryption
    caesar_encrypted = caesar_encrypt(data, caesar_key)

    # Then, apply XOR encryption on the Caesar encrypted data
    xor_encrypted = simple_encrypt(caesar_encrypted.encode(), xor_key)

    return xor_encrypted

# Two-level decryption function
def two_level_decrypt(data, caesar_key, xor_key):
    # First, apply XOR decryption to get the Caesar encrypted data
    caesar_encrypted = simple_decrypt(data, xor_key)

    # Then, apply Caesar cipher decryption on the Caesar encrypted data
    decrypted_data = caesar_decrypt(caesar_encrypted.decode(), caesar_key)

    return decrypted_data

# Function to encrypt a line using the two-level encryption
def encrypt_line(line, caesar_key, xor_key):
    if isinstance(line, str):
        caesar_encrypted = caesar_encrypt(line, caesar_key)
        xor_encrypted = two_level_encrypt(caesar_encrypted, caesar_key, xor_key)
        return xor_encrypted
    else:
        return line  # Return the original data if it's not a string

# Function to decrypt a line using the two-level decryption
def decrypt_line(line, caesar_key, xor_key):
    if isinstance(line, str):
        caesar_decrypted = two_level_decrypt(line, caesar_key, xor_key)
        decrypted = caesar_decrypt(caesar_decrypted, caesar_key)
        return decrypted
    else:
        return line  # Return the original data if it's not a string

while True:
    print()
    print("*****************************")
    print("** TWO-LEVEL ENCRYPTION **")
    print("*****************************")
    print("1. ENCRYPT FILE")
    print("2. DECRYPT FILE")
    print("3. EXIT")
    opt = int(input("Enter your option: "))

    if opt == 1:
        input_file = input("Enter the input file name: ")
        output_file = input_file
        caesar_key = int(input('Enter the Caesar key: '))
        hex_input = input("Enter the XOR key in hexadecimal format (e.g., 0xAB): ")

        try:
            xor_key = int(hex_input, 16)
        except ValueError:
            print("Invalid hexadecimal input. Please enter a valid hexadecimal value.")
            continue
        """
        filename = input("Enter the file to encrypt: ")
            with open(filename, 'rb') as file:
                plaintext = bytearray(file.read())
            encrypted_data = simple_encrypt(plaintext, key)
            with open("encrypted_" + filename, 'wb') as file:
                file.write(encrypted_data)
            print("File encrypted successfully!")
        """
        with open(input_file, 'rb') as file:
            plaintext = bytearray(file.read())
        encrypted_data = simple_encrypt(plaintext, xor_key)
        with open(output_file, 'wb') as file:
            file.write(encrypted_data)
            print("File encrypted successfully!")
        """
        with open(input_file, 'r') as infile, open(output_file, 'wb') as outfile:
            for line in infile:
                encrypted_line = encrypt_line(line.strip(), caesar_key, xor_key)
                outfile.write(encrypted_line + b'\n')
        """
        print("File encrypted successfully.")

    elif opt == 2:
        input_file = input("Enter the input file name: ")
        output_file = input_file
        #output_file = input("Enter the output file name: ")
        caesar_key = int(input('Enter the Caesar key: '))
        hex_input = input("Enter the XOR key in hexadecimal format (e.g., 0xAB): ")
        """
          filename = input("Enter the file to decrypt: ")
            with open(filename, 'rb') as file:
                encrypted_data = bytearray(file.read())
            decrypted_data = simple_decrypt(encrypted_data, key)
            with open("decrypted_" + filename, 'wb') as file:
                file.write(decrypted_data)
            print("File decrypted successfully!")

        """

        try:
            xor_key = int(hex_input, 16)
        except ValueError:
            print("Invalid hexadecimal input. Please enter a valid hexadecimal value.")
            continue
        """
        with open(input_file, 'rb') as infile, open(output_file, 'wb') as outfile:
            for line in infile:
                decrypted_line = decrypt_line(line, caesar_key, xor_key)
                outfile.write(decrypted_line + b'\n')
        """
        with open(input_file, 'rb') as file:
            encrypted_data = bytearray(file.read())
        decrypted_data = simple_decrypt(encrypted_data, xor_key)
        with open(output_file, 'wb') as file:
            file.write(decrypted_data)
            

        print("File decrypted successfully.")

    else:
        print("THANK YOU")
        break
