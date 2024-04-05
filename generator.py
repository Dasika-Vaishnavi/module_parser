import random

# Function to generate a random binary list of length n
def generate_binary_list(n):
    return [random.choice([0, 1]) for _ in range(n)]

digits = int(input("enter the number of digits"))
# Generate 8192 binary lists of length 8
binary_lists = [generate_binary_list(8) for _ in range(digits)]

# Write the binary lists to a .txt file
with open('binary_lists.txt', 'w') as f:
    for binary_list in binary_lists:
        f.write(str(binary_list) + '\n')