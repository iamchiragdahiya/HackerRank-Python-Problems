# Read input for the size of the welcome mat
k, l = map(int, input().split())

# Print the upper part of the welcome mat
for i in range(1, k, 2):
    # Print dashes on both sides of the pattern
    print('-' * (((k * 3) - (3 * i)) // 2), end='')
    # Print the pattern with dots and pipes
    print('.|.' * i, end='')
    # Print dashes on both sides of the pattern
    print('-' * (((k * 3) - (3 * i)) // 2), end='')
    print()

# Print the middle line with the "WELCOME" message
print('-' * ((((k * 3) - 7)) // 2), end='')
print('WELCOME', end='')
print('-' * ((((k * 3) - 7)) // 2), end='\n')

# Print the lower part of the welcome mat
for i in range(k - 2, 0, -2):
    # Print dashes on both sides of the pattern
    print('-' * (((k * 3) - (3 * i)) // 2), end='')
    # Print the pattern with dots and pipes
    print('.|.' * i, end='')
    # Print dashes on both sides of the pattern
    print('-' * (((k * 3) - (3 * i)) // 2), end='')
    print()
