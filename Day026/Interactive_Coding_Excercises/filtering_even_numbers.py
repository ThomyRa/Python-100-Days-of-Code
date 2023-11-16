list_of_strings = input("Insert a list of values. Ex: '1, 2, 3, 4, 5, 6': ").split(',')
# 🚨 Do  not change the code above

# TODO: Use list comprehension to convert the strings to integers 👇:
int_list = [int(string) for string in list_of_strings]

# TODO: Use list comprehension to filter out the odd numbers
# and store the even numbers in a list called "result"
result = [item for item in int_list if item % 2 == 0]

# Write your code 👆 above:
print(result)
