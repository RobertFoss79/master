import sys, csv, tabulate


if len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")
elif len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")

if ".csv" not in sys.argv[1]:
    sys.exit("Not a CSV file")

try:
    file = open(sys.argv[1], "r")
except FileNotFoundError:
    sys.exit("File does not exist")


reader = csv.reader(file, delimiter=',')
headers: any = next(reader)

tables: list[any] = [r for r in reader]
result: str = tabulate.tabulate(tables, headers, tablefmt="grid")

print(result)
