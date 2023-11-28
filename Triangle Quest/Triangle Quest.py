# Loop from 1 to the input value (exclusive)
for i in range(1, int(input())):
    # Calculate 2^i - 1, convert it to binary, and print it multiplied by i
    print(int(bin(2**i - 1)[2:]) * i)
