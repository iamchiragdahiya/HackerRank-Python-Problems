# Read the size of the first set M and initialize the set m
M = int(input())
m = set(map(int, input().split()))

# Read the size of the second set N and initialize the set n
N = int(input())
n = set(map(int, input().split()))

# Initialize an empty set l to store the symmetric difference
l = set()

# Update the set l with elements that are in either set, but not in both
l.update(m.difference(n))
l.update(n.difference(m))

# Convert the set to a list k and sort it
k = list(l)
k.sort()

# Print the sorted symmetric difference
for i in k:
    print(i)
