def print_formatted(n):
    # Determine the width needed for formatting based on the binary representation of n
    l = len(bin(n)[2:])
    
    # Loop from 1 to n (inclusive)
    for i in range(1, n + 1):
        # Print formatted representations for decimal, octal, hexadecimal, and binary values
        print(
            str(i).rjust(l),          # Decimal representation
            oct(i)[2:].rjust(l),     # Octal representation (remove '0o' prefix)
            hex(i)[2:].upper().rjust(l),  # Hexadecimal representation (remove '0x' prefix, convert to uppercase)
            bin(i)[2:].rjust(l)      # Binary representation (remove '0b' prefix)
        )

if __name__ == '__main__':
    # Read an integer input from the user
    n = int(input())
    
    # Call the print_formatted function with the user-provided input
    print_formatted(n)
