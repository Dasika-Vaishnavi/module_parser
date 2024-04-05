import click
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

def caesar_encrypt(text, shift):
    result = ""

    # Traverse text
    for i in range(len(text)):
        char = text[i]

        # Encrypt uppercase characters
        if char.isupper():
            result += chr((ord(char) + shift - 65) % 26 + 65)

        # Encrypt lowercase characters
        else:
            result += chr((ord(char) + shift - 97) % 26 + 97)

    return result

@click.command()
@click.option('--input_file', prompt='Enter the path to the input file', type=click.Path(exists=True))
@click.option('--method', prompt='Which method do you want to use (caesar/aes)?')
def cli(input_file, method):
    # Generate a random 256-bit key
    key = os.urandom(32)

    # Generate a random 128-bit IV
    iv = os.urandom(16)

    # Read the input from a file
    with open(input_file, 'r') as f:
        text = f.read().strip().split(',')

    # Create output directory if it doesn't exist
    if not os.path.exists('output'):
        os.mkdir('output')

    if method == 'caesar':
        shift = 4
        encrypted_texts = [caesar_encrypt(t, shift) for t in text]
        output_file = 'output/caesar_output.txt'
    elif method == 'aes':
        encrypted_texts = [aes_encrypt(t, key, iv) for t in text]
        output_file = 'output/aes_output.txt'
    else:
        click.echo('Invalid method. Please choose either "caesar" or "aes".')
        return

    # Write the encrypted text to the specified output file, each string separated by a comma
    with open(output_file, 'w') as f:
        f.write(','.join(encrypted_texts))

if __name__ == '__main__':
    cli()