# Step 1: Read main set A
A = set(map(int, input().split()))

# Step 2: Read number of other sets
n = int(input())

# Step 3: Assume answer is True initially
is_strict_superset = True

# Step 4: Process each set
for i in range(n):

    # Read another set
    other_set = set(map(int, input().split()))

    # Step 5: Check strict superset condition
    if not A.issuperset(other_set) or A == other_set:
        is_strict_superset = False

# Step 6: Print result
print(is_strict_superset)