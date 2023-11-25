
# Input the number of elements in set a
n = int(input())

# Input the elements of set a
a = set(map(int, input().split()))

# Input the number of elements in set b
m = int(input())

# Input the elements of set b
b = set(map(int, input().split()))

# Find the symmetric_difference of sets a and b, and print the length (number of elements) of the resulting set
print(len(a.symmetric_difference(b)))
