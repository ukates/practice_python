# remake of list_overlap using list comprehension


import random

random_one = [random.randint(0, 100) for i in range(0, 20)]
random_two = [random.randint(0, 100) for j in range(0, 20)]


def overlap(a, b):
    new_list = [item for item in a if item in b]
    return new_list


print(random_one)
print(random_two)
print(overlap(random_one, random_two))
