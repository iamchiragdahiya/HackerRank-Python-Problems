import math

# Read the lengths of sides AB and BC from user input
ab = int(input("Enter the length of side AB: "))
bc = int(input("Enter the length of side BC: "))

# Calculate the angle C in degrees using the arctangent
C = round(math.degrees(math.atan(ab / bc)))

# Print the result
print(f"The angle C is approximately {C}\u00b0.")
