def h_line():
    print(" ---" * user_size)


def v_line():
    print("|   " * (user_size + 1))


if __name__ == "__main__":
    user_size = int(input("What size would you like the map? : "))

    for index in range(user_size):
        h_line()
        v_line()
        h_line()