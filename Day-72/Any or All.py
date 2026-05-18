# Step 1: Read number of integers
n = int(input())

# Step 2: Read list of integers as strings
arr = input().split()

# Step 3: Check if all integers are positive
all_positive = all(int(x) > 0 for x in arr)

# Step 4: Check if any integer is palindrome
has_palindrome = any(x == x[::-1] for x in arr)

# Step 5: Print final result
print(all_positive and has_palindrome)