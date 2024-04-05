import click
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.backends import default_backend
import os

# ... (your encryption functions here) ...

@click.command()
def aes_cli():
    # ... (your AES encryption code here) ...
    from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
    from cryptography.hazmat.primitives import padding
    from cryptography.hazmat.backends import default_backend
    import os

    def aes_encrypt(text, key, iv):
        # Create a cipher object
        cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())

        # Create a padder object
        padder = padding.PKCS7(128).padder()

        # Encrypt the plaintext
        encryptor = cipher.encryptor()
        ciphertext = encryptor.update(padder.update(text.encode()) + padder.finalize()) + encryptor.finalize()

        return ciphertext.hex()

    # Generate a random 256-bit key
    key = os.urandom(32)

    # Generate a random 128-bit IV
    iv = os.urandom(16)

    # test the function
    text = "0123456789ABCDEF0123456789ABCDEF" # 32-bit input in hex strings
    encrypted_text = aes_encrypt(text, key, iv)

    # read the input from a file
    with open('hex_strings.txt', 'r') as f:
        text = f.read().strip()

    encrypted_text = aes_encrypt(text, key, iv)

    # read the input from a file
    with open('hex_strings.txt', 'r') as f:
        text = f.read().strip().split(',')

    encrypted_texts = [aes_encrypt(t, key, iv) for t in text]

    # write the encrypted text to a new file, each 32-bit string separated by a comma
    with open('encrypted_aes.txt', 'w') as f:
        f.write(','.join(encrypted_texts))

@click.command()
def caesar_cli():
    # ... (your Caesar encryption code here) ...
    def caesar_encrypt(text, shift):
        result = ""

        # traverse text
        for i in range(len(text)):
            char = text[i]

            # Encrypt uppercase characters
            if (char.isupper()):
                result += chr((ord(char) + shift - 65) % 26 + 65)

            # Encrypt lowercase characters
            else:
                result += chr((ord(char) + shift - 97) % 26 + 97)

        return result

    # test the function
    text = "0123456789ABCDEF0123456789ABCDEF" # 32-bit input in hex strings
    shift = 4
    encrypted_text = caesar_encrypt(text, shift)

    # read the input from a file
    with open('hex_strings.txt', 'r') as f:
        text = f.read().strip()

    shift = 4
    encrypted_text = caesar_encrypt(text, shift)

    # # write the encrypted text to a new file
    # with open('encrypted.txt', 'w') as f:
    #     f.write(encrypted_text)

    # read the input from a file
    with open('hex_strings.txt', 'r') as f:
        text = f.read().strip().split(',')

    shift = 4
    encrypted_texts = [caesar_encrypt(t, shift) for t in text]

    # write the encrypted text to a new file, each 32-bit string separated by a comma
    with open('encrypted_caesar.txt', 'w') as f:
        f.write(','.join(encrypted_texts))



