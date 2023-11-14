from flask import Flask, request, render_template
import os

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'filename' not in request.files:
        return 'No file part'

    file = request.files['filename']
    print(file.filename)
    print(type(file.filename))
    file1 = file.filename
    if file1 == '':
        return 'No selected file'

    # Access the selected option
    enc_or_dec = request.form['encordec']
    print(enc_or_dec)

    # Access the encryption key
    encryption_key = request.form['encryption_key']
    print(encryption_key)
    print(type(encryption_key))
    upload_folder = r'C:\Users\visha\OneDrive\Documents\Vishal 3rd year\OS lab\osproj'

    if enc_or_dec == 'decryption':  
        output_file=file1
        try:
            xor_key = int(encryption_key, 16)
        except ValueError:
            print("Invalid hexadecimal input. Please enter a valid hexadecimal value.")

        output_file_path = os.path.join(upload_folder, file1.strip('.txt') + '_decrypted' + '.txt')
        print(output_file_path)
        '''
        with open(file1, 'rb') as infile, open(output_file_path, 'wb') as outfile:
            for line in infile:
                print(line)
                print(type(line))
                print(str(line))
                decrypted_line = decrypt_line(line, 3, xor_key)
                print()
                print(decrypted_line)
                outfile.write(decrypted_line + b'\n')'''
        
        with open(file1, 'rb') as infile:
            encrypted_data = infile.read()
        decrypted_data = two_level_decrypt(encrypted_data,3, xor_key)
        with open(output_file, 'w') as outfile:
            
            outfile.write(decrypted_data)

        print("File decrypted successfully.")
        print(output_file_path)

        return 'File decrypted successfully'

    elif enc_or_dec == 'encryption':
        output_file=file1
        try:
            xor_key = int(encryption_key, 16)
        except ValueError:
            print("Invalid hexadecimal input. Please enter a valid hexadecimal value.")

        output_file_path = os.path.join(upload_folder, file1.strip('.txt') + '_encrypted' + '.txt')
        print(output_file_path)
        '''
        with open(file1, 'rb') as infile:
            for line in infile:
                print(line)
                print(type(line))
                print(str(line))
                encrypted_line = encrypt_line(str(line), 3, xor_key)
                print()
                print(encrypted_line)
                outfile.write(encrypted_line + b'\n')

                '''
        
        with open(file1,'rb') as infile:
            plaintext=bytearray(infile.read())
        #encrypted_data = two_level_encrypt(plaintext,3,xor_key)
        print(plaintext)
        encrypted_data = two_level_encrypt(plaintext,3,xor_key)

        with open(output_file,'wb') as outfile:
            outfile.write(encrypted_data)
            print('Encryption successful!')

        print("File encrypted successfully.")
        print(output_file_path)

        return 'File encrypted successfully' 

# # Function to encrypt a line using the two-level encryption
# def encrypt_line(line, caesar_key, xor_key):
#     if isinstance(line, str):
#         caesar_encrypted = caesar_encrypt(line, caesar_key)
#         xor_encrypted = two_level_encrypt(caesar_encrypted, caesar_key, xor_key)
#         return xor_encrypted
#     else:
#         return line  # Return the original data if it's not a string


# Two-level encryption function
def two_level_encrypt(data, caesar_key, xor_key):
    # First, apply Caesar cipher encryption
    print(data.decode('utf-8'))
    caesar_encrypted = caesar_encrypt(data.decode('utf-8'), caesar_key)

    # Then, apply XOR encryption on the Caesar encrypted data
    print('ENCODE')
    print(caesar_encrypted.encode())
    xor_encrypted = simple_encrypt(caesar_encrypted.encode(), xor_key)

    return xor_encrypted

# XOR-based encryption and decryption functions
def simple_encrypt(data, key):
    encrypted_data = bytearray()
    for byte in data:
        encrypted_data.append(byte ^ key)
    return encrypted_data


# Caesar cipher encryption and decryption functions
def caesar_encrypt(text, key=3):
    li = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    encrypted_text = ""

    for char in text:
        if char.isalpha():
            if char.isupper():
                char = char.lower()
                new_index = (li.index(char) + key) % 26
                encrypted_text += li[new_index].upper()
            elif char.islower():
                new_index = (li.index(char) + key) % 26
                encrypted_text += li[new_index]
            else:
                encrypted_text += char
        else:
            encrypted_text += char
    print('ENCRYPTED TEXT AND ITS TYPE')
    print(encrypted_text)
    print(type(encrypted_text))
    return encrypted_text

# # Function to decrypt a line using the two-level decryption
# def decrypt_line(line, caesar_key, xor_key):
#     if isinstance(line, str):
#         caesar_decrypted = two_level_decrypt(line, caesar_key, xor_key)
#         decrypted = caesar_decrypt(caesar_decrypted, caesar_key)
#         return decrypted
#     else:
#         return line  # Return the original data if it's not a string

# Two-level decryption function
def two_level_decrypt(data, caesar_key, xor_key):
    # First, apply XOR decryption to get the Caesar encrypted data
    print(data)
    xor_decrypted = simple_decrypt(data, xor_key)

    # Then, apply Caesar cipher decryption on the Caesar encrypted data
    print('XOR DECRUPTED')
    print(xor_decrypted.decode('utf-8'))
    caesar_decrypted = caesar_decrypt(xor_decrypted.decode('utf-8'), caesar_key)

    return caesar_decrypted


def simple_decrypt(encrypted_data, key):
    decrypted_data = bytearray()
    for byte in encrypted_data:
        decrypted_data.append(byte ^ key)

    print(decrypted_data)
    return decrypted_data

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
    print(decrypted_text)
    return decrypted_text



if __name__ == '__main__':
    app.run(debug=True)
