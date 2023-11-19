# Define a function to mutate a string at a specified position with a given character
def mutate_string(string, position, character):
    # Convert the input string to a list of characters to allow modification
    nstring = list(string)
    
    # Update the character at the specified position in the list
    nstring[position] = character
    
    # Join the list of characters back into a string
    return ''.join(nstring)

# Main block of code
if __name__ == '__main__':
    # Prompt the user to enter a string
    s = input()
    
    # Prompt the user to enter a position and character separated by a space
    i, c = input().split()
    
    # Call the mutate_string function to create a new string with the mutation
    s_new = mutate_string(s, int(i), c)
    
    # Print the resulting mutated string
    print(s_new)
