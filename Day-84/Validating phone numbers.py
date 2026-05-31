import re

# Read number of test cases
n = int(input())

# Process each mobile number
for i in range(n):

    mobile = input()

    # Check valid format
    if re.match(r'^[789]\d{9}$', mobile):
        print("YES")
    else:
        print("NO")