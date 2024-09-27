numbers = input("Enter number separated by spaces: ")

numbers_list = numbers.split()
number_list = map(int, numbers_list)

number_tuple = tuple(numbers_list)

number_hash = hash(number_tuple)

print(number_hash)
