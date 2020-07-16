# Create program to ask user for num and print out list of all divisors of that num


num = int(input('Please enter a number to display divisors: '))

check_list = range(1, num + 1)

divisors = [div for div in check_list if num % div == 0]

print(divisors)


