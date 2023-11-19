# Replace all ______ with rjust, ljust, or center.

thickness = int(input())  # This must be an odd number
c = 'H'  # Character to be printed

# Top Cone
for i in range(thickness):
    # Print a line with 'c' characters, where each side is padded with spaces
    print((c * i).rjust(thickness - 1) + c + (c * i).ljust(thickness - 1))

# Top Pillars
for i in range(thickness + 1):
    # Print 'c' characters centered between two sets of 'c' characters
    print((c * thickness).center(thickness * 2) + (c * thickness).center(thickness * 6))

# Middle Belt
for i in range((thickness + 1) // 2):
    # Print a line with 'c' characters repeated 5 times, centered within a larger width
    print((c * thickness * 5).center(thickness * 6))

# Bottom Pillars
for i in range(thickness + 1):
    # Print 'c' characters centered between two sets of 'c' characters
    print((c * thickness).center(thickness * 2) + (c * thickness).center(thickness * 6))

# Bottom Cone
for i in range(thickness):
    # Print a line with 'c' characters, where each side is padded with spaces
    # Then, the entire line is padded to the right to align with the widest part of the pattern
    print(((c * (thickness - i - 1)).rjust(thickness) + c + (c * (thickness - i - 1)).ljust(thickness)).rjust(thickness * 6))
