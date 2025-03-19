import re

file_name = input("Enter the file name: ")
handle = open(file_name)

numbers_list = list()
total = 0

for line in handle:
    line = line.rstrip()
    word = line.split()
    numbers = re.findall("[0-9]+", line)
    total += sum(int(num) for num in numbers)

print(total)