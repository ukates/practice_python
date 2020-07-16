# Return a list that contains only the elements that are common between lists without duplicates
import random


random_one = [random.randint(0, 100) for i in range(0, 20)]
random_two = [random.randint(0, 100) for j in range(0, 20)]

new_list = []


def overlap(a, b):
    for item in b:
        if item in a and item not in new_list:
            new_list.append(item)
    return new_list


print(random_one)
print(random_two)
print(overlap(random_one, random_two))
