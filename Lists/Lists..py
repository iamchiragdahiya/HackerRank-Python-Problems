# Check if the script is being run as the main program
if __name__ == '__main__':
    # Take input for the number of operations
    N = int(input())

    # Initialize an empty list to store elements
    arr = []

    # Loop through the number of operations
    for i in range(N):
        # Take input for each operation and split it into command and variables
        com, *var = input().split()

        # Convert variable values to integers
        var = list(map(int, var))

        # Execute the corresponding operation based on the command
        if com == 'insert':
            # Insert var[1] at position var[0] in the list
            arr.insert(var[0], var[1])
        elif com == 'print':
            # Print the current list
            print(arr)
        elif com == 'remove':
            # Remove the first occurrence of var[0] from the list
            arr.remove(var[0])
        elif com == 'append':
            # Append var[0] to the end of the list
            arr.append(var[0])
        elif com == 'sort':
            # Sort the list in ascending order
            arr.sort()
        elif com == 'pop':
            # Remove and return the last element from the list
            arr.pop()
        elif com == 'reverse':
            # Reverse the elements of the list in place
            arr.reverse()
