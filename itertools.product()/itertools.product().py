import itertools

# Take input: a list of integers 'A'
A = list(map(int, input().split()))

# Take input: a list of integers 'B'
B = list(map(int, input().split()))

# Use itertools.product to compute the Cartesian product of 'A' and 'B'
product_result = itertools.product(A, B)

# Iterate over the pairs in the Cartesian product and print each pair
for pair in product_result:
    print(pair, end=" ")
