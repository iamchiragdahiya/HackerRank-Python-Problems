def split_and_join(line):
    # The function takes a string 'line' as input and performs the following operations:
    
    # 'line.split()' splits the string into a list of words based on spaces.
    # For example, "Hello World" becomes ["Hello", "World"].
    # '-'.join(...)' joins the list of words using a hyphen (-) as a separator.
    # The resulting string is returned.
    return '-'.join(line.split())

if __name__ == '__main__':
    # This block of code is executed when the script is run.
    
    # User is prompted to input a line of text.
    line = input()
    
    # The split_and_join function is called with the user input as an argument.
    # The result is stored in the 'result' variable.
    result = split_and_join(line)
    
    # The result is printed to the console.
    print(result)
