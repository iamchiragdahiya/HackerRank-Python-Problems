# Read the number of elements in set A
n = int(input())

# Read the elements of set A
A = set(map(int, input().split()))

# Read the number of commands
c = int(input())

# Iterate through the commands
for i in range(c):
    # Initialize a list to store the command and temporary set
    com = []
    temp = []

    # Read the command and store it in the list
    com = list(map(str, input().split()))

    # Perform the corresponding set operation based on the command
    if com[0] == 'intersection_update':
        temp = set(map(int, input().split()))
        A.intersection_update(temp)
    elif com[0] == 'update':
        temp = set(map(int, input().split()))
        A.update(temp)
    elif com[0] == 'symmetric_difference_update':
        temp = set(map(int, input().split()))
        A.symmetric_difference_update(temp)
    elif com[0] == 'difference_update':
        temp = set(map(int, input().split()))
        A.difference_update(temp)

# Print the sum of the elements in the updated set A
print(sum(A))
