# Define a function named print_full_name that takes two parameters: first and last names.
def print_full_name(first, last):
    # Print a formatted greeting message using the provided first and last names.
    print('Hello ', first, ' ', last, '! You just delved into python.', sep='')

# Check if the script is being run as the main program.
if __name__ == '__main__':
    # Prompt the user to enter their first name and store it in the variable first_name.
    first_name = input()
    
    # Prompt the user to enter their last name and store it in the variable last_name.
    last_name = input()
    
    # Call the print_full_name function with the provided first and last names.
    print_full_name(first_name, last_name)
