# Write one line of python that takes a list and makes a new list that has only the even elements of the list


a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

new_list = [item for item in a if item % 2 == 0]

print(new_list)
