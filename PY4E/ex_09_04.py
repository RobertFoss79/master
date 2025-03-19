file_name = input("Enter the file name: ")
file_handle = open(file_name)

email_addresses = dict()

for line in file_handle:
    line = line.rstrip()
    words = line.split()
    if len(words) < 1 or words[0] != "From":
        continue
    email = words[1]
    email_addresses[email] = email_addresses.get(email, 0) + 1

largest = -1
email = None
for k,v in email_addresses.items():
    if v > largest:
        largest = v
        email = k

print(email, largest)
