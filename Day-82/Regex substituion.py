import re

# Step 1: Read number of lines
n = int(input())

# Step 2: Process each line
for i in range(n):

    # Read one line of text
    line = input()

    # Replace && with and
    # only when space exists before and after
    line = re.sub(r'(?<= )&&(?= )', 'and', line)

    # Replace || with or
    # only when space exists before and after
    line = re.sub(r'(?<= )\|\|(?= )', 'or', line)

    # Print modified line
    print(line)