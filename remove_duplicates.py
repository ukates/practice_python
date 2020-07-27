# take a list and return a new list that contains all the elements of the first list minus all the duplicates


import random

list_one = [random.randint(0, 10) for i in range(0, 20)]


def with_lists(li):
    new_list = []
    for i in li:
        if i not in new_list:
            new_list.append(i)
    return new_list


def with_sets(li):
    return list(set(li))


print(with_lists(list_one))
print(with_sets(list_one))
