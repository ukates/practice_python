# Write a program that takes a list of nums and makes a new list with only first and last elem of given list


import random


def list_end(li):
    new_a = [li[0], li[len(li) - 1]]
    print(new_a)


a = [random.randint(0, 100) for i in range(0, 20)]

list_end(a)

