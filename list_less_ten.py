# Take a list and write a program that prints out all elements of the list that are less than 5
# Extra: make new list that has all elements and print out list, write in one line, ask user for number to check less


a_list = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
num = int(input('Please enter number to check less than: '))

for a in a_list:
    if a < num:
        print(a)

b_list = [a for a in a_list if a < num]

print(b_list)
