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

