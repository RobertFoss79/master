file_name = input("Enter File: ")
if len(file_name) < 1: file_name = "clown.txt"
handle = open(file_name)

dictionary = dict()
for line in handle:
    line = line.rstrip()
    words = line.split()
    for word in words:
        dictionary[word] = dictionary.get(word, 0) + 1

temp = list()
for k, v in dictionary.items():
    new_tuple = (v , k)
    temp.append(new_tuple)

temp = sorted(temp, reverse=True)

for v, k in temp[:5]:
    print(k , v)