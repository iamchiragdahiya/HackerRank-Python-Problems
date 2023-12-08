import itertools

# Take input: a string 'st' and an integer 'k'
st, k = input().split()

# Generate all permutations of length 'k' from the characters of the string 'st'
lst = list(itertools.permutations(st, int(k)))

# Sort the list of permutations
lst.sort()

# Print each permutation
for i in lst:
    print(''.join(i))
