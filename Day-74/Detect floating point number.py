import re

# Step 1: Read number of test cases
t = int(input())

# Step 2: Process each string
for i in range(t):

    s = input()

    # Step 3: Check valid floating point format
    pattern = r'^[+-]?\d*\.\d+$'

    # Step 4: Print result
    if re.match(pattern, s):
        print(True)
    else:
        print(False)