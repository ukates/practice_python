with open('Training_01.txt', 'r') as open_file:
    line = open_file.readline().split("/")
    category = line[2]
    count = 1
    while line:
        line = open_file.readline().split("/")
        if len(line) == 1:
            break
        if line[2] == category:
            count = count + 1
        else:
            print("There are " + str(count) + " items in the " + category + " category.")
            count = 1
        category = line[2]


open_file.close()
