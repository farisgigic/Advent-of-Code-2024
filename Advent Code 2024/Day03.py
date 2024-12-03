import re

# Define the relative path to your file
file_path = 'Lists/data3.txt'

with open(file_path, 'r') as file:
    text = file.read()

# Initialize variables
result = 0
enabled = True  # Mul instructions are enabled at the beginning

# Define the patterns
do_pattern = r"do\(\)"
dont_pattern = r"don't\(\)"
mul_pattern = r"mul\((\d{1,3}),(\d{1,3})\)"

# Split text into tokens to process sequentially
tokens = re.split(r'(\bdo\(\)|\bdon\'t\(\)|mul\(\d{1,3},\d{1,3}\))', text)

# Process tokens
for token in tokens:
    if re.match(do_pattern, token):
        enabled = True
    elif re.match(dont_pattern, token):
        enabled = False
    elif enabled and re.match(mul_pattern, token):
        match = re.match(mul_pattern, token)
        num1, num2 = map(int, match.groups())
        result += num1 * num2

# Print the final result
print(result)
