# Define a function called 'is_leap' that takes a single argument 'year'.
def is_leap(year):
    # Initialize a boolean variable 'leap' to 'False'.
    leap = False
    
    # Check if the 'year' is divisible by 4.
    if year % 4 == 0:
        # If it's divisible by 4, check if it's also divisible by 400.
        if year % 400 == 0:
            # If it's divisible by 400, set 'leap' to 'True' indicating it's a leap year.
            leap = True
        else:
            # If it's not divisible by 400, do nothing and keep 'leap' as 'False'.
            pass

    # Return the value of 'leap' (either 'True' for leap year or 'False' for non-leap year).
    return leap

# Prompt the user to input an integer value for 'year' and convert it to an integer.
year = int(input())

# Call the 'is_leap' function with the provided 'year' as an argument, and print the result.
print(is_leap(year))
