# Define a function to count occurrences of a substring in a given string
def count_substring(string, sub_string):
    count = 0  # Initialize a counter to keep track of occurrences
    for i in range(len(string)):
        # Check if the substring matches the current slice of the string
        if sub_string in string[i:i+len(sub_string)]:
            count += 1  # Increment the counter when a match is found
    return count  # Return the final count

# Main program
if __name__ == '__main__':
    # Get the input string and substring from the user
    string = input().strip()
    sub_string = input().strip()
    
    # Call the count_substring function to get the count of occurrences
    count = count_substring(string, sub_string)
    
    # Print the final count
    print(count)
