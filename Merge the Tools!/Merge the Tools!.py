import collections

def merge_the_tools(string, k):
    # List to store substrings
    S = []
    # Temporary list to build each substring
    st = []
    # Counter to keep track of characters in the current substring
    count = 1

    # Iterate through each character in the input string
    for i in string:
        # Add the character to the current substring
        st.append(i)
        
        # Check if the current substring is of length k
        if count == k:
            # If yes, add the substring to the list and reset for the next substring
            S.append(st)
            st = []
            count = 1
        else:
            # If not, increment the counter
            count += 1
    
    # Iterate through the list of substrings
    for i in S:
        # Print the merged version of each substring (remove duplicate characters)
        print(''.join(list(collections.Counter(i).keys())))

if __name__ == '__main__':
    # Input the string and value of k
    string, k = input(), int(input())
    # Call the merge_the_tools function
    merge_the_tools(string, k)
