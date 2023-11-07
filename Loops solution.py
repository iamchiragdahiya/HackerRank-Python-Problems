# Check if the Python script is being run as the main program
if __name__ == '__main__':
    # Prompt the user to enter an integer value for 'n' and convert it to an integer
    n = int(input())

    # Iterate through numbers from 0 to (n-1) using a 'for' loop
    for i in range(n):
        # Calculate the square of the current number 'i' and print the result
        print(i * i)
