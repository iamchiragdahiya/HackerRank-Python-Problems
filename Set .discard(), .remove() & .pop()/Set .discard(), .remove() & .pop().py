# Input the number of elements in the set
n = int(input())

# Input the elements of the set
s = set(map(int, input().split()))

# Input the number of operations
o = int(input())

# Iterate through the operations
for i in range(o):
    # Input the operation and value (if applicable) as a list of strings
    cmvd = list(map(str, input().split()))

    # Check the operation type and perform the corresponding action on the set
    if cmvd[0].lower() == 'pop':
        s.pop()
    elif cmvd[0].lower() == 'discard':
        s.discard(int(cmvd[1]))
    elif cmvd[0].lower() == 'remove':
        s.remove(int(cmvd[1]))

# Print the sum of the elements in the set after the operations
print(sum(s))
