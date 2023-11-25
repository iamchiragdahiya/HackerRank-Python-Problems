# Enter your code here. Read input from STDIN. Print output to STDOUT
# Enter your code here. Read input from STDIN. Print output to STDOUT
# Input the number of elements in set a
n = int(input())

# Input the elements of set a
a = set(map(int, input().split()))

# Input the number of elements in set b
m = int(input())

# Input the elements of set b
b = set(map(int, input().split()))

# Find the difference of sets a and b, and print the length (number of elements) of the resulting set
print(len(a.difference(b)))
