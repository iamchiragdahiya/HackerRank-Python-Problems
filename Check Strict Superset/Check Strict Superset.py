# Read the elements of the superset 'ss' from user input
ss = set(map(int, input().split()))

# Read the number of subsets 'n' from user input
n = int(input())

# Initialize a variable 'tok' as False to keep track of the result
tok = False

# Initialize a counter 'c' to count subsets that are supersets of 'ss'
c = 0

# Iterate through each subset
for i in range(n):
    # Read the elements of the current subset 'sub' from user input
    sub = set(map(int, input().split()))

    # Check if 'ss' is a superset of the current subset 'sub'
    if ss.issuperset(sub):
        c += 1

# Check if all subsets are supersets of 'ss'
if c == n:
    # If all subsets are supersets of 'ss', print True
    print(True)
else:
    # If not all subsets are supersets of 'ss', print the initial value of 'tok' (False)
    print(tok)
