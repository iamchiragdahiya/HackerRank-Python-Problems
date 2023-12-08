import itertools

# Take input: a string 'st' and an integer 'k'
st, k = input().split()

# Initialize an empty list to store combinations
lst = []

# Generate combinations of lengths 1 to 'k' from the characters of the string 'st'
for i in range(1, int(k) + 1):
    # Use itertools.combinations to generate combinations of length 'i'
    temp = list(itertools.combinations(st, int(i)))

    # Initialize a temporary list to store sorted combinations
    temp2 = []

    # Convert each combination tuple to a list, sort it, and add it to temp2
    for i in temp:
        t = list(i)
        t.sort()
        temp2.append(t)

    # Sort temp2 and add its contents to the main list 'lst'
    temp2.sort()
    lst.extend(temp2)

# Print each combination
for i in lst:
    print(''.join(i))

