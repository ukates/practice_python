def file_as_lists(file_name):
    return_list = []
    with open(file_name, 'r') as file:
        line = file.readline()
        while line:
            return_list.append(int(line))
            line = file.readline()
    return return_list


prime_list = file_as_lists("primenumbers.txt")
happy_list = file_as_lists("happynumbers.txt")

overlap_list = [item for item in prime_list if item in happy_list]

with open("overlap.txt", 'w') as overlap_file:
    for item in overlap_list:
        overlap_file.write(str(item) + "\n")
