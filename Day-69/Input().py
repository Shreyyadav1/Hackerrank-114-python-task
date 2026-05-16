# Step 1: Read x and k
x, k = map(int, input().split())

# Step 2: Read polynomial
polynomial = input()

# Step 3: Evaluate polynomial
result = eval(polynomial)

# Step 4: Compare with k
if result == k:
    print(True)
else:
    print(False)