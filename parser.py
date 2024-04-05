# Function to convert a binary list to a hexadecimal string
def binary_list_to_hex(binary_list):
    binary_string = ''.join(str(bit) for bit in binary_list)
    hex_string = hex(int(binary_string, 2))[2:].zfill(32)
    return hex_string

# Read the binary lists from the .txt file
with open('binary_lists.txt', 'r') as f:
    binary_lists = [eval(line.strip()) for line in f]

# Convert the binary lists to hexadecimal strings
hex_strings = [binary_list_to_hex(binary_list) for binary_list in binary_lists]

# Write the hexadecimal strings to a different .txt file
with open('hex_strings.txt', 'w') as f:
    for hex_string in hex_strings:
        f.write(hex_string + '\n')