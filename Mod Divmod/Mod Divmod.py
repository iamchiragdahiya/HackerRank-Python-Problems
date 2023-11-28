# Enter your code here. Read input from STDIN. Print output to STDOUT
import cmath

# Read the first integer 'a' from user input
a = int(input())

# Read the second integer 'b' from user input
b = int(input())

# Perform integer division and print the result
print(a // b)

# Compute the remainder and print the result
print(a % b)

# Use divmod to get both the quotient and remainder, and print the result as a tuple
print(divmod(a, b))
