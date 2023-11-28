# Read the number of test cases
n = int(input())

# Iterate through each test case
for i in range(n):
    # Read the size of set A and its elements
    a = int(input())
    A = set(map(int, input().split()))

    # Read the size of set B and its elements
    b = int(input())
    B = set(map(int, input().split()))

    # Check if set A is a subset of set B and print the result
    print(A.issubset(B))
