# Step 1: Read number of English subscribers
n = int(input())

# Step 2: Read English roll numbers
english = set(map(int, input().split()))

# Step 3: Read number of French subscribers
m = int(input())

# Step 4: Read French roll numbers
french = set(map(int, input().split()))

# Step 5: Find students subscribed to only one newspaper
result = english.symmetric_difference(french)

# Step 6: Print total count
print(len(result))