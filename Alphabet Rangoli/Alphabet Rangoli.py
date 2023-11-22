def print_rangoli(n):
    import string

    # Get lowercase alphabets
    al = string.ascii_lowercase
    chota_al = al[:n]
    chota_ulta_al = chota_al[::-1]

    # Print the upper part of the rangoli
    for i in range(n):
        ar = []

        # Build the list of characters for each line in the upper part
        for j in range(i + 1):
            ar.append(chota_ulta_al[j])
        for j in range(i - 1, -1, -1):
            ar.append(chota_ulta_al[j])

        # Print the line, centering it within the specified width
        print('-'.join(ar).center(((n - 1) * 4) + 1, '-'))

    # Print the lower part of the rangoli
    for i in range(n - 2, -1, -1):
        ar = []

        # Build the list of characters for each line in the lower part
        for j in range(i + 1):
            ar.append(chota_ulta_al[j])
        for j in range(i - 1, -1, -1):
            ar.append(chota_ulta_al[j])

        # Print the line, centering it within the specified width
        print('-'.join(ar).center(((n - 1) * 4) + 1, '-'))

if __name__ == '__main__':
    # Read an integer input from the user
    n = int(input("Enter the size of the rangoli: "))

    # Call the print_rangoli function with the user-provided input
    print_rangoli(n)
