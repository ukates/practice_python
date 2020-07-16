# Exercise 1: Create a program that asks the user to enter their name and age,
# print out a message addressed to them that tell them the year that they will turn 100 years old.


name = input("Please enter your name: ")
age = int(input("What is your age %s: " % name))
when100 = (100 - age) + 2020
num = int(input("Please enter a number: "))


print("%s, you will be 100 years old in %d\n" % (name, when100) * num)
