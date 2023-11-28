# Read the base 'a' from user input
a = int(input())

# Read the exponent 'b' from user input
b = int(input())

# Read the modulus 'm' from user input
m = int(input())

# Calculate and print a^b
print(pow(a, b))

# Calculate and print (a^b) % m
print(pow(a, b, m))
