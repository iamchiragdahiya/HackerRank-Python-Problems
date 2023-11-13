# Import the itertools module for working with iterators
import itertools

# Take input for the number of lists (K) and a constant (M)
K, M = map(int, input().split())

# Initialize an empty list to store K lists of integers
arr = []

# Loop to input K lists of integers and square each element
for i in range(K):
    # Map each element to its square, starting from the second element
    arr.append(list(map(lambda x: x**2, list(map(int, input().split()))[1:])))

# Use itertools.product to get the Cartesian product of all lists
arr2 = itertools.product(*arr)

# Initialize an empty list to store the sum modulo M for each combination
arr3 = []

# Loop to calculate the sum modulo M for each combination
for i in arr2:
    arr3.append(sum(i) % M)

# Print the maximum value from the list of sums modulo M
print(max(arr3))
