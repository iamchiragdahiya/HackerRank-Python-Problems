import collections

# Read the number of elements in the list
n = int(input())

# Read the elements of the list
s = list(map(int, input().split()))

# Create a Counter object to count occurrences of each element
c = collections.Counter(s)

# Iterate through the Counter items and print keys with a count of 1
for key, value in c.items():
    if value == 1:
        print(key)
