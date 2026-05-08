# Step 1: Take input
n = int(input())

# Step 2: Loop from 1 to n-1
for i in range(1, n):

    # Step 3: Create repeating 1's
    # Example:
    # i = 3 -> 111
    repeated_ones = (10**i - 1) // 9

    # Step 4: Multiply by current number
    # Example:
    # 3 * 111 = 333
    result = i * repeated_ones

    # Step 5: Print result
    print(result)