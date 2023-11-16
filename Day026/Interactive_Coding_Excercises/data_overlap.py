with open("file1.txt", "r") as f1:
    file1 = f1.readlines()

with open("file2.txt", "r") as f2:
    file2 = f2.readlines()

file1 = [int(data1.strip()) for data1 in file1]
file2 = [int(data2.strip()) for data2 in file2]
result = [data for data in file1 if data in file2]

# Write your code above 👆
print(result)
