
filehandle = open("mbox-short.txt")

for line in filehandle:
    ss_line = line.rstrip()
    print(ss_line.upper())
