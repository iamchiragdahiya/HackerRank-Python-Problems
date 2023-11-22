#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(c):
    # Convert the string to a list of characters for easy modification
    ST = list(c)

    # Loop through each character in the list
    for i in range(len(ST)):
        # Capitalize the first letter of the first word
        if i == 0:
            ST[i] = ST[i].upper()
            continue
        # Check if it's the last character
        if i == len(ST) - 1:
            # If the preceding character is a space, capitalize the last letter
            if ST[i - 1] == ' ':
                ST[i] = ST[i].upper()
            else:
                break
        # Check conditions for capitalizing letters
        if ST[i - 1] != ' ' and ST[i + 1] != ' ':
            continue
        if ST[i - 1] != ' ' and ST[i + 1] == ' ':
            continue
        ST[i] = ST[i].upper()

    # Join the modified list of characters into a string and return
    return ''.join(ST)

if __name__ == '__main__':
    # Open a file for writing the result
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # Read input from the user
    s = input()

    # Call the solve function with the user-provided input
    result = solve(s)

    # Write the result to the file
    fptr.write(result + '\n')

    # Close the file
    fptr.close()
