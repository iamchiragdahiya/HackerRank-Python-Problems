import itertools

# Take input: an integer 'N'
N = int(input())

# Take input: a list of 'N' elements as space-separated strings
n = list(input().split())

# Take input: an integer 'k'
k = int(input())

# Use itertools.combinations to generate all combinations of length 'k' from the list 'n'
ls = list(itertools.combinations(n, k))

# Initialize a counter variable
count = 0

# Iterate over the generated combinations
for i in ls:
    # Check if the character 'a' is present in the current combination 'i'
    if 'a' in i:
        # If 'a' is present, increment the counter
        count += 1

# Calculate the probability by dividing the count by the total number of combinations
probability = round(count / len(ls), 3)

# Print the calculated probability
print(probability)
