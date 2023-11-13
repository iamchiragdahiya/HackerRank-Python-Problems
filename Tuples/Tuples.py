# Get the number of elements as input
n = int(input())

# Take a space-separated list of integers as input and convert it to a tuple
integer_list = tuple(map(int, input().split()))

# Print the hash value of the tuple
print(hash(integer_list))
