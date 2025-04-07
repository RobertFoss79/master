file_name = input("Enter the file name: ")
file_handle = open(file_name)

count = 0
email_addresses = []

for line in file_handle:
    line = line.rstrip()
    words = line.split()
    if len(words) < 3 or words[0] != "From":
        continue
    email_addresses.append(words[1])
    count += 1

for email in email_addresses:
    print(email)

print("There were", count, "lines in the file with From as the first word")
