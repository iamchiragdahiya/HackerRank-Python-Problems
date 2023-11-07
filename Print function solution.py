# Check if the Python script is being run as the main program
if __name__ == '__main__':
    # Prompt the user to enter an integer value and convert it to an integer
    num = int(input())
    
    # Initialize variables for 'power' and 'number'
    power = num  # 'power' starts with the input value
    number = 0   # 'number' starts at 0

    # Loop from 0 to 'num' (inclusive)
    for i in range(num + 1):
        # Calculate the next part of the number by adding 'i' multiplied by 10^'power'
        number = number + i * (10 ** power)
        # Reduce the power by 1 in each iteration to move to the next decimal place

    # Print the final 'number' after the loop
    print(number)
