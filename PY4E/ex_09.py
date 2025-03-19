file_name = input("Enter File: ")
if len(file_name) < 1: file_name = "clown.txt"
handle = open(file_name)

dictionary = dict()
for line in handle:
    line = line.rstrip()
    words = line.split()
    for word in words:
        dictionary[word] = dictionary.get(word, 0) + 1

largest = -1
the_word = None
for k,v in dictionary.items():
    if v > largest:
        largest = v
        the_word = k

print(the_word, largest)
