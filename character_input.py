# Exercise 1: Create a program that asks the user to enter their name and age,
# print out a message addressed to them that tell them the year that they will turn 100 years old.


name = input("Please enter your name: ")
age = input("What is your age %s: " % name)
when100 = (100 - int(age)) + 2020


print("%s, you will be 100 years old in %d" % (name, when100))
