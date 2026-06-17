import re

# Read number of test cases
t = int(input())

for i in range(t):

    # Read UID
    uid = input()

    # Condition 1: Exactly 10 characters
    if len(uid) != 10:
        print("Invalid")
        continue

    # Condition 2: Only alphanumeric characters
    if not uid.isalnum():
        print("Invalid")
        continue

    # Condition 3: No repeated characters
    if len(set(uid)) != 10:
        print("Invalid")
        continue

    # Condition 4: At least 2 uppercase letters
    upper_count = len(re.findall(r'[A-Z]', uid))

    if upper_count < 2:
        print("Invalid")
        continue

    # Condition 5: At least 3 digits
    digit_count = len(re.findall(r'\d', uid))

    if digit_count < 3:
        print("Invalid")
        continue

    # If all conditions pass
    print("Valid")