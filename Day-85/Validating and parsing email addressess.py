import re
import email.utils

# Read number of entries
n = int(input())

for i in range(n):

    # Read full line
    entry = input()

    # Extract name and email
    name, email_id = email.utils.parseaddr(entry)

    # Email validation pattern
    pattern = r'^[A-Za-z][A-Za-z0-9._-]*@[A-Za-z]+\.[A-Za-z]{1,3}$'

    # Check validity
    if re.match(pattern, email_id):

        # Print in required format
        print(email.utils.formataddr((name, email_id)))