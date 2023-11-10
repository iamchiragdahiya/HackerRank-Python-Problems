# Check if the Python script is being run as the main program
if __name__ == '__main__':
    # Prompt the user to enter an integer 'n' representing the size of the array
    n = int(input())

    # Prompt the user to enter 'n' space-separated integers and convert them to a list
    arr = list(map(int, input().split()))

    # Sort the list 'arr' in descending order
    arr.sort(reverse=True)

    # Check if the count of the highest element is greater than 1
    if arr.count(arr[0]) > 1:
        # Print the second highest element in the sorted list
        print(arr[arr.count(arr[0])])
    else:
        # If all elements are the same, print the second element
        print(arr[1])
