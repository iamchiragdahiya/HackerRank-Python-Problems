def average(array):
    # Convert the array to a set to get unique elements
    unique_elements = set(array)
    
    # Calculate the average of unique elements
    average_value = sum(unique_elements) / len(unique_elements)
    
    # Round the result to 3 decimal places
    rounded_average = round(average_value, 3)
    
    return rounded_average

if __name__ == '__main__':
    # Input the length of the array
    n = int(input())
    
    # Input the array elements
    arr = list(map(int, input().split()))
    
    # Call the average function and print the result
    result = average(arr)
    print(result)
