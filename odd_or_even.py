# Ask user for num, depending on whether the num is odd or even, print out appropriate message to user.

num = int(input("Please input a number: "))
check = int(input("Please input a second number: "))

if num % 4 == 0:
    print("Multiple of four")

print("even") if num % 2 == 0 else print("odd")

print("divides evenly") if num % check == 0 else print("does not divide evenly")
