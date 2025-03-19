file_name = input("Enter file name: ")
file_handle = open(file_name)
sorted_lines = list()
for line in file_handle:
    words = line.split()
    for word in words:
        if word not in sorted_lines:
            sorted_lines.append(word)

sorted_lines.sort()

print(sorted_lines)