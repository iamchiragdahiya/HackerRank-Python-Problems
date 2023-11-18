# Import the itertools module for combinations
import itertools

# Initialize an empty list to store user inputs
S = []

# Get user inputs for x, y, z, and n
x = int(input("Enter value for x: "))
y = int(input("Enter value for y: "))
z = int(input("Enter value for z: "))
n = int(input("Enter value for n: "))

# Append the user inputs to the list S
S.append(x)
S.append(y)
S.append(z)

# Initialize empty lists N and L to store intermediate values
N = []
L = []

# Initialize the list to store the final combinations
comb1 = []

# Loop through each element in S
for i in S:
    # Generate a list of values from 0 to i (inclusive) and append it to N
    for j in range(i + 1):
        N.append(j)
    # Append the list N to L
    L.append(N)
    # Reset N to an empty list for the next iteration
    N = []

# Generate all possible combinations using the product of lists in L
comb = list(set(itertools.product(*L)))

# Loop through each combination in comb
for i in comb:
    # Check if the sum of the combination is not equal to n
    if sum(i) != n:
        # Append the combination to comb1
        comb1.append(list(i))

# Sort the final combinations
comb1.sort()

# Print the result
print("Resulting Combinations:", comb1)
