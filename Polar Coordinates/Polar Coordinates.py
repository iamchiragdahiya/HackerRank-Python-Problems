# Enter your code here. Read input from STDIN. Print output to STDOUT
import cmath

# Read a complex number as a string from user input
comp = input()

# Convert the input to a complex number and print its absolute value
print(abs(complex(comp)))

# Print the phase of the complex number
print(cmath.phase(complex(comp)))
