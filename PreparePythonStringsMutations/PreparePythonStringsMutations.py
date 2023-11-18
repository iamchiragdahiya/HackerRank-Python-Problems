def mutate_string(string, position, character):
    # Convert the input string to a list of characters
    nstring = list(string)
    
    # Replace the character at the specified position with the new character
    nstring[position] = character
    
    # Join the list of characters back into a string
    return ''.join(nstring)

if __name__ == '__main__':
    # Get the input string from the user
    s = input()
    
    # Get the position and character for mutation from the user
    i, c = input().split()
    
    # Call the mutate_string function to create the mutated string
    s_new = mutate_string(s, int(i), c)
    
    # Print the mutated string
    print(s_new)
