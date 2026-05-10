# Enter your code here. Read input from STDIN. Print output to STDOUT
# Step 1: Number of test cases
t = int(input())

# Step 2: Process each test case
for i in range(t):

    # Step 3: Read size of set A
    n = int(input())

    # Step 4: Read elements of set A
    A = set(map(int, input().split()))

    # Step 5: Read size of set B
    m = int(input())

    # Step 6: Read elements of set B
    B = set(map(int, input().split()))

    # Step 7: Check subset condition
    result = A.issubset(B)

    # Step 8: Print result
    print(result)