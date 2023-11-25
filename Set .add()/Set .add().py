# Read the number of input lines
n = int(input())

# Initialize an empty set to store unique input strings
s = set()

# Loop through each line of input
for i in range(n):
    # Add each input string to the set
    s.add(input())

# Print the number of unique strings in the set
print(len(s))
