# Function to convert a binary list to a hexadecimal string
def binary_list_to_hex(binary_list):
    binary_string = ''.join(str(bit) for bit in binary_list)
    hex_string = hex(int(binary_string, 2))[2:].zfill(32)
    return hex_string

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

# Read the binary lists from the .txt file
with open('binary_lists.txt', 'r') as f:
    binary_lists = [eval(line.strip()) for line in f]

# Convert the binary lists to hexadecimal strings and encrypt them
shift = 4
encrypted_texts = [caesar_encrypt(binary_list_to_hex(binary_list), shift) for binary_list in binary_lists]

# Write the encrypted hexadecimal strings to a different .txt file
with open('encrypted_direct.txt', 'w') as f:
    f.write(','.join(encrypted_texts))