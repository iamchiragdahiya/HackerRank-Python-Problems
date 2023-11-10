# Initialize empty lists to store records and names
record = []        # To store name and score pairs
names = []         # To store names of students with the second lowest score
score_record = []  # To store scores for later processing

# Loop to input records
for i in range(int(input())):
    name = input()          # Input student name
    score = float(input())  # Input student score
    score_record.append(score)  # Add score to the score_record list
    record.append([name, score])  # Add name and score pair to the record list

# Sort the score_record list in ascending order
score_record.sort()

# Check if there is more than one student with the lowest score
if score_record.count(score_record[0]) > 1:
    # Loop through records to find students with the second lowest score
    for i in record:
        if i[1] == score_record[score_record.count(score_record[0])]:
            names.append(i[0])  # Add names of students with the second lowest score to the names list
else:
    # Loop through records to find students with the second lowest score
    for i in record:
        if i[1] == score_record[1]:
            names.append(i[0])  # Add names of students with the second lowest score to the names list

# Sort the names list in alphabetical order
names.sort()

# Print the names of students with the second lowest score
for x in names:
    print(x)
