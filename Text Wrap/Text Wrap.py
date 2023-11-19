import textwrap

# Define a function 'wrap' that takes a string and maximum width as input
def wrap(string, max_width):
    # Use the textwrap.fill function to wrap the input string to the specified width
    return textwrap.fill(string, width=max_width)

# Check if the script is being run as the main program
if __name__ == '__main__':
    # Get user input for the string to be wrapped and the maximum width
    string = input("Enter the string: ")
    max_width = int(input("Enter the maximum width: "))
    
    # Call the 'wrap' function with the user inputs
    result = wrap(string, max_width)
    
    # Print the wrapped string
    print(result)
