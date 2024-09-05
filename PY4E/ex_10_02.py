file_name = input("Enter File: ")
if len(file_name) < 1:
    file_name = "mbox-short.txt"
file_handle = open(file_name)

times = dict()

for line in file_handle:
    line = line.rstrip()
    words = line.split()
    if len(words) < 1 or words[0] != "From":
        continue
    time = words[5][:2]
    times[time] = times.get(time, 0) + 1

# print(sorted([(k, v) for k, v in times.items()]))

temp = list()
for k, v in times.items():
    new_tuple = (k, v)
    temp.append(new_tuple)

temp = sorted(temp)

for k, v in temp:
    print(k , v)