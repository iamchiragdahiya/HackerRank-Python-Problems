if __name__ == '__main__':
    # Get input from the user
    s = input()

    # Check if there is at least one alphanumeric character
    alphanumeric_token = False
    for i in s:
        if i.isalnum():
            alphanumeric_token = True
            break
    print("Alphanumeric token present:", alphanumeric_token)

    # Check if there is at least one alphabetical character
    alphabetical_token = False
    for i in s:
        if i.isalpha():
            alphabetical_token = True
            break
    print("Alphabetical token present:", alphabetical_token)

    # Check if there is at least one digit
    digit_token = False
    for i in s:
        if i.isdigit():
            digit_token = True
            break
    print("Digit token present:", digit_token)

    # Check if there is at least one lowercase character
    lowercase_token = False
    for i in s:
        if i.islower():
            lowercase_token = True
            break
    print("Lowercase token present:", lowercase_token)

    # Check if there is at least one uppercase character
    uppercase_token = False
    for i in s:
        if i.isupper():
            uppercase_token = True
            break
    print("Uppercase token present:", uppercase_token)
